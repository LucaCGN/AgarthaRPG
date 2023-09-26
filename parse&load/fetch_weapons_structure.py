from google.cloud import firestore
from pprint import pprint
import os

def initialize_firestore():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../config/agartha-rpg-firebase.json"
    return firestore.Client()

def print_weapon_details(db, weapon_name):
    # Fetch the specific weapon document
    weapon_ref = db.collection('fixed_game_data').document('fixed_game_systems').collection('weapons_system').document(weapon_name)
    weapon_doc = weapon_ref.get()

    if weapon_doc.exists:
        print(f"Document: {weapon_name}")
        weapon_data = weapon_doc.to_dict()
        weapon_details = weapon_data.get('weapon_details', {})
        
        print("  Fields:")
        for field, value in weapon_details.items():
            print(f"    {field} - Value: ", end="")
            pprint(value)
    else:
        print(f"No document found for weapon: {weapon_name}")

if __name__ == "__main__":
    db = initialize_firestore()
    print_weapon_details(db, "Axe")
    print_weapon_details(db, "Round Shield")
