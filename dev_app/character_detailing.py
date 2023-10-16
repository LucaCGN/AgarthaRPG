
import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox

def display_game_context(ui):
    ui.display_message("Welcome to the mystical world of Agartha.")
    ui.display_message("This is a land of endless possibilities, challenges, and rewards.")

def fetch_character_details(ui):
    additional_details = {}
    
    name = ui.get_input("Enter your character's name: ")
    additional_details['name'] = name
    
    backstory = ui.get_input("Enter your character's backstory: ")
    additional_details['backstory'] = backstory
    
    return additional_details

def choose_gameplay_focus(ui):
    focuses = ['Combat', 'Exploration', 'Roleplay']
    
    ui.display_message("Choose your gameplay focus:")
    for i, focus in enumerate(focuses):
        ui.display_message(f"{i + 1}. {focus}")
    
    while True:
        choice = int(ui.get_input("Enter the index of your gameplay focus: ")) - 1
        
        if 0 <= choice < len(focuses):
            selected_focus = focuses[choice]
            ui.display_message(f"You have selected {selected_focus} as your gameplay focus.")
            return selected_focus
        else:
            ui.display_message("Invalid choice. Try again.")

def detail_new_character(db, user_id, character_data, ui):
    # Add additional details to the character document
    character_id = character_data['character_id']
    character_ref = db.collection('characters').document(character_id)
    
    character_ref.update(character_data)
    
    ui.display_message(f"Added details to character {character_id}.")
