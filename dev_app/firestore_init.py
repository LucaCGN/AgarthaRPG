import os
import time  # Import the time module
from google.cloud import firestore

def initialize_firestore():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../config/agartha-rpg-firebase.json"
    db = firestore.Client()
    
    # Fetch professions and weapons from Firestore and store them for later use
    professions = fetch_professions_from_firestore(db)
    weapons = fetch_weapons_from_firestore(db)
    
    return db, professions, weapons

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
    
    # Validation step
    if not professions:
        print("Validation: No professions fetched.")
    else:
        print(f"Validation: Fetched professions: {professions}")
    
    time.sleep(3)  # Add a delay of 3 seconds
    
    return professions

def flatten_professions(nested_professions):
    flattened = []
    for stat, profession_list in nested_professions.items():
        for profession in profession_list:
            flattened.append({
                'name': profession['name'],
                'skills': profession['skills'],
                'description': profession['description'],
                'stat': stat
            })
    return flattened

def flatten_weapons(nested_weapons):
    flattened = []
    for weapon_name, skills in nested_weapons.items():
        for skill in skills:
            flattened_skill = {
                'weapon_name': weapon_name,
                'skill_name': skill.get('name', 'Unknown'),
                'type': skill.get('type', 'Unknown'),
                'description': skill.get('description', 'Unknown'),
                'effect': skill.get('effect', 'Unknown'),
                'ap_cost': skill.get('ap_cost', None),
                'initiative_value': skill.get('initiative_value', None),
                'interruptable': skill.get('interruptable', 'Unknown')
            }
            flattened.append(flattened_skill)
    return flattened

def fetch_weapons_from_firestore(db):
    print("Fetching weapons from Firestore...")
    weapons_ref = db.collection('fixed_game_data').document('fixed_game_systems').collection('weapons_system')
    query_snapshot = weapons_ref.stream()

    weapons = {}
    for doc in query_snapshot:
        data = doc.to_dict()  # Assume that the document data is an array of skills
        weapon_name = doc.id  # Assume the document ID is the weapon name

        # Create an empty list for each new weapon
        if weapon_name not in weapons:
            weapons[weapon_name] = []

        # Append the array of skills to the weapon
        weapons[weapon_name] = data

    # Validation step
    if not weapons:
        print("Validation: No weapons fetched.")
    else:
        print(f"Validation: Fetched weapons: {weapons}")

    time.sleep(3)  # Add a delay of 3 seconds

    return weapons
