import os
import time
from google.cloud import firestore
import login  # Assuming login.py is in the same directory
import character_creation
import character_detailing  # Assuming character_creation.py is in the same directory

def initialize_firestore():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../config/agartha-rpg-firebase.json"
    return firestore.Client()

def main():
    print("Welcome to Agartha RPG!")
    
    # Initialize Firestore
    db = initialize_firestore()
    
    user_id = None
    while user_id is None:
        user_id = login.login_user(db)
    
    while True:
        print("What would you like to do next?")
        print("1. Continue Adventure")
        print("2. Create New Character")
        
        choice = input("Enter your choice (1/2): ")
        
        if choice == '1':
            print("This feature is still in development.")
        elif choice == '2':
            character_data = {}
            
            # Roll and assign stats
            rolled_stats = character_detailing.roll_stats()
            assigned_stats = character_detailing.assign_stats(rolled_stats)
            character_data['stats'] = assigned_stats  # Store the assigned stats
            
            selected_profession = character_creation.select_profession(db)
            if selected_profession:
                character_data['profession'] = selected_profession  # Directly assign the string
                
                selected_weapons = character_creation.select_weapons(db, user_id)
                if selected_weapons:
                    character_data['Weapon1'] = selected_weapons[0]  # Directly assign the string
                    character_data['Weapon2'] = selected_weapons[1]  # Directly assign the string
                    
                    character_name = input("Enter the name of your new character: ")
                    character_data['name'] = character_name
                    
                    # Display game context
                    character_detailing.display_game_context()
                    
                    # Fetch additional character details
                    additional_details = character_detailing.fetch_character_details()
                    character_data.update(additional_details)  # Merge the additional details
                    
                    # Choose gameplay focus
                    gameplay_focus = character_detailing.choose_gameplay_focus()
                    character_data['gameplay_focus'] = gameplay_focus  # Store the gameplay focus
                    
                    character_creation.create_new_character(db, user_id, character_data, selected_weapons, selected_profession)
                    
                    # Call the detail_new_character function to add additional details
                    character_detailing.detail_new_character(db, user_id, character_data)

                    # Wait for 3 seconds to give Firestore time to create the document
                    time.sleep(3)

                    # Create the character_id based on the character name
                    character_id = 'dev_' + character_data.get('name', '')

                    # Call the calculate_resources function to update resources and debug any issues
                    character_detailing.calculate_resources(db, user_id, character_id, character_data)



if __name__ == "__main__":
    main()

