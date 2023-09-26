from modules.general.dice_roller import roll_dice  # Assuming the path to dice_roller.py

def roll_stats():
    """
    Rolls 6D4 six times, drops the lowest value from each roll, and sums the remaining values.
    
    Returns:
        list: A list of six numbers representing the rolled stats.
    """
    rolled_stats = []
    for _ in range(6):
        # Roll 4D6
        result = roll_dice({'d6': 4})
        
        # Drop the lowest value and sum the rest
        rolls = result['d6']
        rolls.remove(min(rolls))
        stat_value = sum(rolls)
        
        rolled_stats.append(stat_value)
        
    return rolled_stats

def assign_stats(rolled_stats):
    """
    Allows the user to assign rolled stats to character attributes.
    
    Parameters:
        rolled_stats (list): A list of six numbers representing the rolled stats.
        
    Returns:
        dict: A dictionary mapping attributes to their assigned stats.
    """
    attributes = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']
    assigned_stats = {}
    
    print(f"Rolled stats: {rolled_stats}")
    
    for attr in attributes:
        print(f"Assign a value to {attr}:")
        
        # Display available stats in menu format
        for i, stat in enumerate(rolled_stats):
            print(f"{i + 1}. {stat}")
        
        while True:
            choice = int(input("Enter the index of the stat you want to assign: ")) - 1
            
            if 0 <= choice < len(rolled_stats):
                assigned_stats[attr] = rolled_stats.pop(choice)
                print(f"Assigned {assigned_stats[attr]} to {attr}")
                
                # Update the list of available stats
                print("Updated List:")
                for i, stat in enumerate(rolled_stats):
                    print(f"{i + 1}. {stat}")
                
                break
            else:
                print("Invalid choice. Try again.")
                
    print(f"Final assigned stats: {assigned_stats}")
    return assigned_stats

def display_game_context():
    print("\nWelcome to Agartha RPG!")
    print("------------------------------------------------")
    print("As a newly turned 18-year-old human, you embark on a journey of self-discovery and adventure.")
    print("Orphaned at a young age, you've grown up on a secluded island, armed with the legacy of your parents—two cherished weapons.")
    print("Fueled by the dream to follow in your grandfather's footsteps, you set out to forge your own destiny.")
    print("While part of your backstory is set, the canvas of your life is yet to be painted. The choices are yours to make.")
    print("------------------------------------------------\n")

def fetch_character_details():
    character_details = {}
    
    # Sex
    print("Choose your character's sex:")
    sex_menu = ['Male', 'Female']
    for i, option in enumerate(sex_menu):
        print(f"{i + 1}. {option}")
    choice = int(input("Enter your choice: ")) - 1
    character_details['sex'] = sex_menu[choice]
    
    # Facial Description
    character_details['facial_description'] = input("Describe your character's facial features (max 100 characters): ")[:100]
    
    # Physical Description
    character_details['physical_description'] = input("Describe your character's physical features (max 100 characters): ")[:100]
    
    # Personality Description
    character_details['personality_description'] = input("Describe your character's personality traits (max 100 characters): ")[:100]
    
    # Moral Values Description
    character_details['moral_values_description'] = input("Describe your character's moral values (max 100 characters): ")[:100]
    
    return character_details


def choose_gameplay_focus():
    gameplay_elements = ["Elemental Combat System", "Professions & Economy System", "Lore & Campaign System"]
    ranked_elements = []
    
    print("\nRank the gameplay elements by importance:")
    while gameplay_elements:
        for i, element in enumerate(gameplay_elements):
            print(f"{i + 1}. {element}")
        choice = int(input("Enter the index of your choice: ")) - 1
        
        if 0 <= choice < len(gameplay_elements):  # Check if choice is within valid range
            ranked_elements.append(gameplay_elements.pop(choice))
        else:
            print("Invalid choice. Please try again.")
    
    print(f"Your ranked gameplay focus is: {', '.join(ranked_elements)}\n")
    return ranked_elements



def detail_new_character(db, user_id, character_data):
    # Create a reference to the Firestore document where the character data will be stored
    character_ref = db.collection('users').document(user_id).collection('characters').document()
    
    # Create stats map
    stats = character_data.get('stats', {})
    stats_map = {
        'STR': stats.get('STR', 0),
        'DEX': stats.get('DEX', 0),
        'CON': stats.get('CON', 0),
        'INT': stats.get('INT', 0),
        'WIS': stats.get('WIS', 0),
        'CHA': stats.get('CHA', 0)
    }
    
    # Create gameplay_priority map
    gameplay_priority_map = {
        'combat': character_data.get('gameplay_focus', [])[0],
        'profession': character_data.get('gameplay_focus', [])[1],
        'campaign': character_data.get('gameplay_focus', [])[2]
    }
    
    # Prepare the data to be saved
    character_data_to_save = {
        'name': character_data.get('name', ''),
        'profession': character_data.get('profession', ''),
        'Weapon1': character_data.get('Weapon1', ''),
        'Weapon2': character_data.get('Weapon2', ''),
        'stats': stats_map,
        'sex': character_data.get('sex', ''),
        'facial_description': character_data.get('facial_description', ''),
        'physical_description': character_data.get('physical_description', ''),
        'personality_description': character_data.get('personality_description', ''),
        'moral_values_description': character_data.get('moral_values_description', ''),
        'gameplay_priority': gameplay_priority_map
    }
    
    # Save the data to Firestore
    character_ref.set(character_data_to_save)
    print("New character {} created!".format(character_data.get('name', '')))


def calculate_resources(db, user_id, character_id, character_data):
    # Debugging Step 1: Print character_data to check if it contains all necessary keys
    print("Debugging Step 1: character_data:", character_data)
    
    # Calculate resources based on stats
    stats = character_data.get('stats', {})
    
    # Debugging Step 2: Print stats to check if it contains all necessary keys
    print("Debugging Step 2: stats:", stats)
    
    # Calculate max and current resources
    max_life = int(10 + (stats.get('CON', 0) * 10))
    max_mana = int(10 + (stats.get('INT', 0) * 10))
    max_focus = int(10 + (stats.get('WIS', 0) * 10))
    current_mana = max_mana
    current_life = max_life
    current_focus = max_focus
    
    # Debugging Step 3: Print calculated resources to verify calculations
    print("Debugging Step 3: Calculated Resources - max_life:", max_life, "max_mana:", max_mana, "max_focus:", max_focus)
    
    # Create resources_level map
    resources_level = {
        'max_life': max_life,
        'max_mana': max_mana,
        'max_focus': max_focus,
        'current_mana': current_mana,
        'current_life': current_life,
        'current_focus': current_focus
    }
    
    # Debugging Step 4: Print resources_level map to verify its structure
    print("Debugging Step 4: resources_level:", resources_level)
    
    # Create a reference to the Firestore document where the character data is stored
    ### ALTERAR PARA LÓGICA PARA QUALQUER USÁRIO
    character_ref = db.collection('user').document('dev').collection('game_data').document(character_id)
    
    # Update the character document with the new resources
    character_ref.update({'resources_level': resources_level})
    
    # Debugging Step 5: Confirm that the document has been updated
    print("Debugging Step 5: Character document updated with new resources.")
