import os
import json
import re
from google.cloud import firestore

# Initialize Firestore
def initialize_firestore():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/Luca/Documents/GITHUB/AgarthaRPG/config/agartha-rpg-firebase.json"
    return firestore.Client()

# Parse the text file into a Python dictionary
def parse_file_to_json(file_path):
    parsed_data = {}
    current_doc = None
    current_field = None
    current_subfield = None
    field_data = {}
    in_example_items = False

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return parsed_data
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return parsed_data

    for index, line in enumerate(lines):
        # Capture Document Name
        doc_match = re.match(r"│   ├── (.+) \(Document\)", line)
        if doc_match:
            if current_doc:
                if in_example_items:
                    parsed_data['Example_Items'][current_doc] = {'item_details': field_data}
                else:
                    parsed_data[current_doc][current_field] = field_data

            current_doc = doc_match.groups()[0]
            field_data = {}
            current_field = None
            current_subfield = None
            in_example_items = False
            continue

        # Detect if in the Example_Items sub-collection
        if "Example_Items" in line:
            in_example_items = True
            parsed_data['Example_Items'] = {}
            continue

        # Capture Field Name
        field_match = re.match(r"│   │   └── (.+) \(Fields\)", line)
        if field_match:
            current_field = field_match.groups()[0]
            parsed_data[current_doc] = {}
            continue

        # Capture String Fields
        string_match = re.match(r"│   │       ├── (.+) \(String\) - \"(.+)\"", line)
        if string_match:
            key, value = string_match.groups()
            field_data[key] = value
            continue

        # Capture Number Fields
        number_match = re.match(r"│   │       ├── (.+) \(Number\) - (.+)", line)
        if number_match:
            key, value = number_match.groups()
            field_data[key] = int(value)
            continue

        # Capture Map Fields
        map_match = re.match(r"│   │       ├── (.+) \(Map\)", line)
        if map_match:
            current_subfield = map_match.groups()[0]
            field_data[current_subfield] = {}
            continue

        # Capture Elements in Maps
        map_element_match = re.match(r"│   │       │   ├── (.+) \(String\) - \"(.+)\"", line)
        if map_element_match:
            key, value = map_element_match.groups()
            field_data[current_subfield][key] = value
            continue

        # Capture Array of Strings
        array_str_match = re.match(r"│   │       ├── (.+) \(Array of Strings\) - \[(.+)\]", line)
        if array_str_match:
            array_name, array_values_str = array_str_match.groups()
            array_values = array_values_str.split(", ")
            field_data[array_name] = array_values
            continue

        # Capture Array of Maps
        array_map_match = re.match(r"│   │       └── (.+) \(Array of Maps\)", line)
        if array_map_match:
            array_name = array_map_match.groups()[0]
            field_data[array_name] = []
            continue

        # Capture Elements in Array of Maps
        array_map_element_match = re.match(r"│   │           ├── { \"name\": \"(.+)\", \"effect\": \"(.+)\" }", line)
        if array_map_element_match:
            name, effect = array_map_element_match.groups()
            field_data[array_name].append({
                "name": name,
                "effect": effect
            })

    # Save the last document
    if current_doc:
        if in_example_items:
            parsed_data['Example_Items'][current_doc] = {'item_details': field_data}
        else:
            parsed_data[current_doc][current_field] = field_data

    return parsed_data

    
# Save parsed data to a JSON file in the 'check' folder
def save_to_check_folder(parsed_data, file_name):
    check_folder_path = "C:/Users/Luca/Documents/GITHUB/AgarthaRPG/parse&load/check"
    with open(f"{check_folder_path}/{file_name}.json", 'w') as f:
        json.dump(parsed_data, f, indent=4)

# Load parsed data from a JSON file in the 'check' folder
def load_from_check_folder(file_name):
    check_folder_path = "C:/Users/Luca/Documents/GITHUB/AgarthaRPG/parse&load/check"
    with open(f"{check_folder_path}/{file_name}.json", 'r') as f:
        return json.load(f)

# Upload the parsed data to Firestore
def upload_to_firestore(db, parsed_data):
    doc_ref = db.collection('fixed_game_data').document('fixed_game_systems')
    sub_collection_ref = doc_ref.collection('weapons_system')
    
    for doc_name, doc_data in parsed_data.items():
        sub_collection_ref.document(doc_name).set(doc_data)

# Main function to execute all steps
# Main function to execute all steps
def main():
    db = initialize_firestore()
    file_name = "weapons_system"
    file_path = "C:/Users/Luca/Documents/GITHUB/AgarthaRPG/misc_dev_reference_files/core_systems/Final/Core Systems/weapons_system.txt"

    check_folder_path = "C:/Users/Luca/Documents/GITHUB/AgarthaRPG/parse&load/check"
    json_file_path = f"{check_folder_path}/{file_name}.json"

    if os.path.exists(json_file_path):
        user_choice = input("File already exists in check folder. Skip parsing and update the existing file? (yes/no): ")
        
        if user_choice.lower() == 'yes':
            print("Loading from check folder...")
            parsed_data = load_from_check_folder(file_name)
            
            if not parsed_data:
                print("No data loaded from check folder. Exiting...")
                return
        else:
            print("Parsing file...")
            parsed_data = parse_file_to_json(file_path)
            
            if not parsed_data:
                print("No data parsed. Exiting...")
                return
            
            print("Saving to check folder...")
            save_to_check_folder(parsed_data, file_name)
    else:
        print("Parsing file...")
        parsed_data = parse_file_to_json(file_path)
        
        if not parsed_data:
            print("No data parsed. Exiting...")
            return
        
        print("Saving to check folder...")
        save_to_check_folder(parsed_data, file_name)

    print("Uploading to Firestore...")
    upload_to_firestore(db, parsed_data)

# Execute the main function
if __name__ == "__main__":
    main()


# Execute the main function
if __name__ == "__main__":
    main()