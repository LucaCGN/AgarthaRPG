import os
from google.cloud import firestore

# Initialize Firestore
def initialize_firestore():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/Luca/Documents/GITHUB/AgarthaRPG/config/agartha-rpg-firebase.json"
    return firestore.Client()

def fetch_generic_structure(reference, depth=0):
    structure = []
    prefix = "  " * depth
    
    # Fetch all documents in the reference
    documents = reference.stream()
    for document in documents:
        structure.append(f"{prefix}Document: {document.id}")
        
        # Fetch all subcollections in the document
        subcollections = document.reference.collections()
        for subcollection in subcollections:
            structure.append(f"{prefix}  Subcollection: {subcollection.id}")
            structure.extend(fetch_generic_structure(subcollection, depth + 2))
    return structure

def fetch_structure_with_fields(reference, depth=0):
    structure = []
    prefix = "  " * depth
    
    # Fetch all documents in the reference
    documents = reference.stream()
    for document in documents:
        structure.append(f"{prefix}Document: {document.id}")
        
        # Print fields in the document
        for field, value in document.to_dict().items():
            structure.append(f"{prefix}  Field: {field} - Value: {value}")
        
        # Fetch all subcollections in the document
        subcollections = document.reference.collections()
        for subcollection in subcollections:
            structure.append(f"{prefix}  Subcollection: {subcollection.id}")
            structure.extend(fetch_structure_with_fields(subcollection, depth + 2))
    return structure

def save_to_file(data, filename):
    check_folder_path = "C:/Users/Luca/Documents/GITHUB/AgarthaRPG/parse&load/check"
    with open(f"{check_folder_path}/{filename}.txt", 'w') as f:
        for line in data:
            f.write(f"{line}\n")

if __name__ == "__main__":
    db = initialize_firestore()
    
    # Fetch data only for the 'fixed_game_data' collection
    fixed_game_data_ref = db.collection('fixed_game_data')
    
    # Fetch generic structure and save to file
    generic_structure = fetch_generic_structure(fixed_game_data_ref)
    save_to_file(generic_structure, "generic_structure")
    
    # Fetch structure with fields and save to file
    structure_with_fields = fetch_structure_with_fields(fixed_game_data_ref)
    save_to_file(structure_with_fields, "structure_with_fields")
