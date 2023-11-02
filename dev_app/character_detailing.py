
# Import relevant modules and libraries
import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox

# Import functions from avatar_generation
from modules.general.avatar_generation import fetch_character_details, generate_avatar_image, generate_character_description

# Initialize global cache
global_cache = {'character_details': {}}

# Function to display initial game context
def display_game_context(ui):
    # Your existing logic to display initial game context
    pass

# ========================== New Panels ==========================

# ----------------- Step 1: Game Context Panel -----------------

def create_game_context_panel(age, backstory, race, profession, weapon, ui, on_next):
    """
    Display a panel that summarizes the choices made by the player so far.
    """
    intro_text = ("It's time to expand the details of your character. In the magical elemental world of Agartha, "
                  "you are a recently turned 18 orphan who grew up in a small village on the isolated island of Ylvast, "
                  f"south of Lake Ylv. Your father left you his {weapon}, which you mastered while growing up. "
                  f"One of the other few belongings that remained from your lost family is a bag with your grandmother's {profession} items, "
                  "which you always cherished and used as inspiration as you imagined your future in this world.")
    
    # Display intro text
    label_intro = ttk.Label(ui.main_frame, text=intro_text, wraplength=400)
    label_intro.pack(pady=10)

    # Next button
    next_button = ttk.Button(ui.main_frame, text='Next', command=on_next)
    next_button.pack(pady=10)

# -------------- Step 2: Attribute Selection Panel --------------

def create_attribute_selection_panel(ui, on_confirm):
    """
    Display a panel for selecting character attributes.
    """
    # Dropdown menu for Gender
    gender_label = ttk.Label(ui.main_frame, text="Gender:")
    gender_label.pack(pady=5)
    gender_var = tk.StringVar()
    gender_dropdown = ttk.Combobox(ui.main_frame, textvariable=gender_var, values=["Male", "Female", "Non-binary"])
    gender_dropdown.pack(pady=5)
    
    # Dropdown menu for Hair Color
    hair_label = ttk.Label(ui.main_frame, text="Hair Color:")
    hair_label.pack(pady=5)
    hair_var = tk.StringVar()
    hair_dropdown = ttk.Combobox(ui.main_frame, textvariable=hair_var, values=["Black", "Brown", "Blond", "Red", "Blue", "Green", "Pink"])
    hair_dropdown.pack(pady=5)

    # Dropdown menu for Eye Color
    eye_label = ttk.Label(ui.main_frame, text="Eye Color:")
    eye_label.pack(pady=5)
    eye_var = tk.StringVar()
    eye_dropdown = ttk.Combobox(ui.main_frame, textvariable=eye_var, values=["Brown", "Blue", "Green", "Gray", "Hazel", "Amber"])
    eye_dropdown.pack(pady=5)

    # Dropdown menu for Body Type
    body_label = ttk.Label(ui.main_frame, text="Body Type:")
    body_label.pack(pady=5)
    body_var = tk.StringVar()
    body_dropdown = ttk.Combobox(ui.main_frame, textvariable=body_var, values=["Thin", "Normal", "Fat"])
    body_dropdown.pack(pady=5)

    # Confirm button
    confirm_button = ttk.Button(ui.main_frame, text='Confirm', command=on_confirm)
    confirm_button.pack(pady=10)

# ---------------- Step 3: Open Text Panel ----------------

def create_open_text_panel(ui, on_confirm):
    """
    Display a panel with text boxes for character detailing.
    """
    # Helper text for each input box
    helper_texts = {
        "Name": "Insert the name of your character (0/20 characters)",
        "Distinctive Facial Features": "Use this space to describe distinctive features you want on your avatar image (0/100 characters)",
        "Moral Values": "This is a replacement to the restrictive alignment system (0/100 characters)"
    }

    # Create text boxes with helper texts
    for key, value in helper_texts.items():
        label = ttk.Label(ui.main_frame, text=key)
        label.pack(pady=5)
        
        text_var = tk.StringVar()
        text_box = ttk.Entry(ui.main_frame, textvariable=text_var)
        
        # Set helper text as default
        text_var.set(value)
        
        text_box.pack(pady=5)

    # Confirm button
    confirm_button = ttk.Button(ui.main_frame, text='Confirm', command=on_confirm)
    confirm_button.pack(pady=10)

# Your existing event handlers and any new ones you may add for the new panels

# ---------------- Step 4: Data Collection and Storage ----------------

def collect_and_store_data():
    """
    Collect all data from the panels and store it in a global cache.
    Call OpenAI APIs to generate character description and avatar.
    Store data in Firestore.
    """
    # Collect character details from global cache
    character_details = fetch_character_details(global_cache)
    
    # Generate avatar and character description using OpenAI API
    avatar_path = generate_avatar_image(character_details)
    character_description = generate_character_description(character_details)
    
    # Store the generated avatar path and description in global_cache
    global_cache['character_details']['avatar_path'] = avatar_path
    global_cache['character_details']['character_description'] = character_description
    
    # [Your code to store the data in Firestore would go here]

# -------------- Step 5: Final Confirmation Panel --------------

def create_final_confirmation_panel(ui, on_start_game):
    """
    Display the generated character description and avatar.
    """
    # Fetch generated character description and avatar path from global_cache
    avatar_path = global_cache['character_details'].get('avatar_path', 'Path not found')
    character_description = global_cache['character_details'].get('character_description', 'Description not available')
    
    # Display generated character description and avatar
    ttk.Label(ui.main_frame, text=f"Avatar saved at: {avatar_path}").pack(pady=10)
    ttk.Label(ui.main_frame, text=f"Character Description: {character_description}").pack(pady=10)
    
    # 'Start Game' button
    start_game_button = ttk.Button(ui.main_frame, text='Start Game', command=on_start_game)
    start_game_button.pack(pady=10)



# ========================== Event Handlers ==========================

# Your existing event handlers and any new ones you may add for the new panels

# ====================================================================

# Your existing code for other functionalities