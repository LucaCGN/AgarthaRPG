from google.cloud import firestore

def create_new_character(db, user_id, character_data, selected_weapons, selected_profession):
    # Fetch the dev_character document
    dev_character_ref = db.collection('user').document(user_id).collection('game_data').document('dev_character')
    dev_character = dev_character_ref.get()
    
    if dev_character.exists:
        # Copy the dev_character data
        new_character_data = dev_character.to_dict()
        
        # Update it with the new fields
        new_character_data.update(character_data)
        
        # Create a new document with the character name
        new_character_name = character_data['name']
        new_character_ref = db.collection('user').document(user_id).collection('game_data').document(f"{user_id}_{new_character_name}")
        
        # Set the new document with the updated data
        new_character_ref.set(new_character_data)
        
               # Create a subcollection for character_game_data
        character_game_data_ref = new_character_ref.collection('character_game_data')
        
        # Fetch and add selected weapons to the subcollection
        weapons_ref = db.collection('fixed_game_data').document('fixed_game_systems').collection('weapons_system')
        for weapon_name in selected_weapons:
            weapon_doc = weapons_ref.document(weapon_name).get()
            if weapon_doc.exists:
                character_game_data_ref.document(f"Weapon_{weapon_name}").set(weapon_doc.to_dict())
        
        # Fetch and add selected profession to the subcollection
        professions_ref = db.collection('fixed_game_data').document('fixed_game_systems').collection('professions_system')
        profession_doc = professions_ref.document(selected_profession).get()
        if profession_doc.exists:
            character_game_data_ref.document(f"Profession_{selected_profession}").set(profession_doc.to_dict())
        
        print(f"New character {new_character_name} created!")
    else:
        print("No dev_character found.")

stats = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']

def fetch_professions_from_firestore(db):
    print("Fetching professions from Firestore...")
    professions_ref = db.collection('fixed_game_data').document('fixed_game_systems').collection('professions_system')
    query_snapshot = professions_ref.stream()
    
    professions = {}
    
    for doc in query_snapshot:
        data = doc.to_dict()
        stat = data.get('Associated_Stat', 'Unknown')
        
        if stat not in professions:
            professions[stat] = []
        
        professions[stat].append({
            'name': doc.id,
            'description': data.get('Description', 'No description available'),
            'skills': data.get('Skills', {})
        })
        
    return professions

def select_stat():
    print("Select a stat:")
    for i, stat in enumerate(stats):
        print(f"{i+1}. {stat}")
    choice = int(input("Enter your choice (or 0 to go back): "))
    if choice == 0:
        return None
    return stats[choice - 1]

def select_profession_from_stat(professions, selected_stat):
    print("##")
    print(f"Professions under {selected_stat}:")
    for i, prof in enumerate(professions[selected_stat]):
        print(f"{i+1}. {prof['name']}")
    print("##")
    choice = int(input("Enter your choice (or 0 to go back): "))
    if choice == 0:
        return None
    selected_prof = professions[selected_stat][choice - 1]
    print("##")
    print(f"Profession Chose: {selected_prof['name']}")
    print("##")
    print(f"Description: {selected_prof['description']}")
    print("##")
    print("Skills:")
    
    # Sort skills by their levels
    sorted_skills = sorted(selected_prof['skills'].items(), key=lambda x: x[1]['Level'])
    
    for skill, details in sorted_skills:
        print(f"{skill}({details['Level']}): {details['Effect']}")
    print("##")
    confirm = input("Do you want to confirm this as your choice?(yes,no): ")
    if confirm.lower() == 'yes':
        return selected_prof['name']
    return None

def select_profession(db):
    professions = fetch_professions_from_firestore(db)
    selected_profession = None
    while True:
        selected_stat = select_stat()
        if selected_stat is None:
            break
        if selected_stat in professions:
            selected_profession = select_profession_from_stat(professions, selected_stat)
            if selected_profession:
                return selected_profession

def fetch_weapons_from_firestore(db):
    print("Fetching weapons from Firestore...")
    weapons_ref = db.collection('fixed_game_data').document('fixed_game_systems').collection('weapons_system')
    query_snapshot = weapons_ref.stream()
    
    weapons = {}
    
    for doc in query_snapshot:
        data = doc.to_dict()
        weapon_details_data = data.get('weapon_details', {})
        
        stat = weapon_details_data.get('Stat', 'Unknown')
        
        # Skip over documents that are not weapons
        if stat == 'Unknown':
            continue
        
        if stat not in weapons:
            weapons[stat] = []
        
        weapon_details = {
            'Name': weapon_details_data.get('Name', 'Unknown'),
            'Description': weapon_details_data.get('Description', 'Unknown'),
            'Base_damage': weapon_details_data.get('Base_damage', None),
            'Passive': weapon_details_data.get('Passive', None),
            'Actions': weapon_details_data.get('Actions', [])
        }
        
        weapons[stat].append(weapon_details)
        
    return weapons


def select_weapon_from_stat(weapons, selected_stat):
    print("##")
    print(f"Weapons under {selected_stat}:")
    for i, weapon in enumerate(weapons[selected_stat]):
        print(f"{i+1}. {weapon['Name']}")
    print("##")
    choice = int(input("Enter your choice (or 0 to go back): "))
    if choice == 0:
        return None
    selected_weapon = weapons[selected_stat][choice - 1]
    print("##")
    print(f"Weapon Chose: {selected_weapon['Name']}")
    print("##")
    print(f"Description: {selected_weapon['Description']}")
    print("##")
    
    if 'Base_damage' in selected_weapon:
        print(f"Base Damage: {selected_weapon['Base_damage']}")
    elif 'Passive' in selected_weapon:
        print(f"Passive: {selected_weapon['Passive']['Name']} ({selected_weapon['Passive']['Effect']})")
    
    print("##")
    print("Actions:")
    
    for action in selected_weapon['Actions']:
        print(f"{action['name']}: {action['effect']}")
        if 'damage' in action:
            print(f"Damage: {action['damage']}")
    print("##")
    
    confirm = input("Do you want to confirm this as your choice?(yes,no): ")
    if confirm.lower() == 'yes':
        return selected_weapon['Name']
    return None


def select_weapons(db, user_id):
    weapons = fetch_weapons_from_firestore(db)
    selected_weapons = []
    
    for i in range(2):
        while True:
            selected_stat = select_stat()
            if selected_stat is None:
                break
            if selected_stat in weapons:
                selected_weapon = select_weapon_from_stat(weapons, selected_stat)
                if selected_weapon:
                    selected_weapons.append(selected_weapon)
                    break
    
    # Update Firestore document with selected weapons
    if len(selected_weapons) == 2:
        return selected_weapons
    else:
        print("You must select two weapons.")
        return None



