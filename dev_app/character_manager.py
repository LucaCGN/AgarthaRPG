from firestore_init import flatten_professions  # Import the flatten_professions function

import character_creation  # Assumes character_creation.py is in the same directory
import character_detailing  # Assumes character_detailing.py is in the same directory
import character_rolling  # Assumes character_rolling.py is in the same directory

def create_and_detail_character(db, professions, weapons, user_id, ui, assigned_stats, rolled_stats):

    character_data = {'stats': assigned_stats}
    
    # Roll and assign stats
    assigned_stats = character_rolling.assign_stats(rolled_stats)  # Removed 'ui' argument
    character_data['stats'] = assigned_stats  # Store the assigned stats
    
    # Flatten the professions data
    flattened_professions = flatten_professions(professions)

    # Select profession
    selected_profession = character_creation.select_profession(flattened_professions, ui, weapons)
    if selected_profession:
        character_data['profession'] = selected_profession  # Directly assign the string
        
        selected_weapon = character_creation.select_weapon(db, user_id, ui)  # Note the function name change
        if selected_weapon:
            character_data['Weapon'] = selected_weapon  # Now only one weapon
           
            # Fetch and display game context
            character_detailing.display_game_context(ui)
            
            # Fetch additional character details
            additional_details = character_detailing.fetch_character_details(ui)
            character_data.update(additional_details)  # Merge the additional details
            
            # Choose gameplay focus
            gameplay_focus = character_detailing.choose_gameplay_focus(ui)
            character_data['gameplay_focus'] = gameplay_focus  # Store the gameplay focus
            
            # Create the character in the database
            character_creation.create_new_character(db, user_id, character_data, selected_weapon, selected_profession, ui)
            
            # Add additional details to the character in the database
            character_detailing.detail_new_character(db, user_id, character_data, ui)
