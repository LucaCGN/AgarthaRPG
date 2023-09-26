import os
import json
from google.cloud import firestore

# Initialize Firestore
def initialize_firestore():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/Luca/Documents/GITHUB/AgarthaRPG/config/agartha-rpg-firebase.json"
    return firestore.Client()

# Load parsed data from a JSON file in the 'check' folder
def load_from_check_folder(file_name):
    check_folder_path = "C:/Users/Luca/Documents/GITHUB/AgarthaRPG/parse&load/check"
    with open(f"{check_folder_path}/{file_name}.json", 'r') as f:
        return json.load(f)

# Upload the parsed data to Firestore
def upload_to_firestore(db, parsed_data):
    doc_ref = db.collection('fixed_game_data').document('fixed_game_systems')
    sub_collection_ref = doc_ref.collection('professions_system')
    
    for doc_name, doc_data in parsed_data['professions_system'].items():
        sub_collection_ref.document(doc_name).set(doc_data)

# Main function to execute all steps
def main():
    db = initialize_firestore()
    file_name = "professtions_system"

    check_folder_path = "C:/Users/Luca/Documents/GITHUB/AgarthaRPG/parse&load/check"
    json_file_path = f"{check_folder_path}/{file_name}.json"

    if os.path.exists(json_file_path):
        user_choice = input("File already exists in check folder. Load and update the existing file? (yes/no): ")
        
        if user_choice.lower() == 'yes':
            print("Loading from check folder...")
            parsed_data = load_from_check_folder(file_name)
            
            if not parsed_data:
                print("No data loaded from check folder. Exiting...")
                return
        else:
            print("Exiting...")
            return
    else:
        print("File not found in check folder. Exiting...")
        return

    print("Uploading to Firestore...")
    upload_to_firestore(db, parsed_data)

# Execute the main function
if __name__ == "__main__":
    main()
