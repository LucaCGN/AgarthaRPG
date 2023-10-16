import os
import json
from google.cloud import firestore

# Initialize Firestore
def initialize_firestore():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/Luca/Documents/GITHUB/AgarthaRPG/config/agartha-rpg-firebase.json"
    return firestore.Client()

def load_weapons_to_firestore():
    # Initialize Firestore
    db = initialize_firestore()
    
    # Load weapons data from JSON file
    weapons_file_path = "C:/Users/Luca/Documents/GITHUB/AgarthaRPG/parse&load/weapons_system.json"
    with open(weapons_file_path, 'r') as f:
        weapons_data = json.load(f)
    
    # Reference to the document where the subcollection will be added
    doc_ref = db.collection("fixed_game_data").document("fixed_game_systems")
    
    # Create or get subcollection named 'Weapons'
    weapons_collection = doc_ref.collection('weapons_system')
    
    # Iterate through weapon data and add to Firestore
    for weapon_name, skills in weapons_data.items():
        weapon_doc_ref = weapons_collection.document(weapon_name)
        weapon_doc_ref.set({"skills": skills})

if __name__ == "__main__":
    load_weapons_to_firestore()