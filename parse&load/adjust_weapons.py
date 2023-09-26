import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialize Firebase Admin SDK
cred = credentials.Certificate("../config/agartha-rpg-firebase.json")  # Replace with your credentials file path
firebase_admin.initialize_app(cred)

# Initialize Firestore client
db = firestore.client()

def fetch_weapons_from_firestore(db):
    print("Fetching weapons from Firestore...")
    weapons_ref = db.collection('fixed_game_data').document('fixed_game_systems').collection('weapons_system')
    query_snapshot = weapons_ref.stream()
    
    weapons = {}
    
    for doc in query_snapshot:
        data = doc.to_dict()
        print(f"Raw Data: {data}")  # Print raw data for debugging
        
        # Access the nested 'weapon_details' field
        weapon_details_data = data.get('weapon_details', {})
        
        stat = weapon_details_data.get('Stat', 'Unknown')
        
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



if __name__ == "__main__":
    fetched_weapons = fetch_weapons_from_firestore(db)
    print("Fetched Weapons:")
    for stat, weapon_list in fetched_weapons.items():
        print(f"Stat: {stat}")
        for weapon in weapon_list:
            print(f"  - {weapon['Name']}")