import tkinter as tk
from tkinter import ttk
from tkinter import Canvas, Frame, Scrollbar

# Function to create the profession panel
# Function to create the profession panel
def create_profession_panel(professions, ui, on_confirm, weapons):
    print("Professions before passing to create_profession_panel:", professions)  # Debugging Step 1
    print("Debugging: ", type(professions), professions)  # Print the first 3 items for brevity

    panel = ttk.Frame(ui.main_frame, padding="10")
    
    # Dropdown menu for profession selection
    ui.profession_var = tk.StringVar(panel)
    ui.profession_var.set("Alchemist")  # Set Alchemist as the default selection

    # Create the OptionMenu with an empty list initially
    profession_dropdown = ttk.OptionMenu(panel, ui.profession_var, "")
    profession_dropdown.grid(row=0, column=0, columnspan=5, sticky=tk.W + tk.E)

    # Clear the menu and add items back in
    menu = profession_dropdown['menu']
    menu.delete(0, tk.END)
    
    # Check if professions is a list of dictionaries
    if isinstance(professions, list) and all(isinstance(p, dict) for p in professions):
        sorted_professions = sorted([p['name'] for p in professions])
    else:
        print("Error: professions is not a list of dictionaries.")
        sorted_professions = []

    for p in sorted_professions:
        menu.add_command(label=p, command=lambda profession=p: ui.profession_var.set(profession))

    
    # Create Text widget for profession details
    details_text = tk.Text(panel, wrap=tk.NONE, width=150, height=40)  # Tripled the width and height
    details_text.grid(row=1, column=0, columnspan=5, sticky=tk.N+tk.S+tk.W+tk.E)
    
    # Add a horizontal scrollbar to Text widget
    h_scroll = ttk.Scrollbar(panel, orient='horizontal', command=details_text.xview)
    h_scroll.grid(row=2, column=0, columnspan=5, sticky=tk.W + tk.E)
    details_text['xscrollcommand'] = h_scroll.set
    
    def update_details(*args):
        print("Updating details for selected profession.")
        selected = ui.profession_var.get()
        print(f"Selected profession: {selected}")
        for p in professions:
            if p['name'] == selected:
                details_text.delete(1.0, tk.END)
                details_text.insert(tk.END, f"---------------------------------------\n")
                details_text.insert(tk.END, f"{p['name']}\n\n")
                details_text.insert(tk.END, f"Associated Stat: {p.get('stat', 'N/A')}\n\n")  # Safely get 'stat'
                details_text.insert(tk.END, f"{p['description']}\n\n")
                
                # Sort skills by level before displaying
                sorted_skills = sorted(p['skills'].items(), key=lambda x: x[1].get('Level', 0))
                
                for skill_name, skill in sorted_skills:
                    skill_level = skill.get('Level', 'Default Skill Level')
                    skill_type = skill.get('Type', 'Default Skill Type')
                    skill_effect = skill.get('Effect', 'Default Skill Effect')
                    
                    details_text.insert(tk.END, f"Lvl {skill_level} Skill:\n")
                    details_text.insert(tk.END, f"- Name: {skill_name}\n")
                    details_text.insert(tk.END, f"- Level: {skill_level}\n")
                    details_text.insert(tk.END, f"- Type: {skill_type}\n")
                    details_text.insert(tk.END, f"- Effect: {skill_effect}\n\n")
                
                details_text.insert(tk.END, f"---------------------------------------\n")
    
    ui.profession_var.trace_add('write', update_details)
    update_details()  # Trigger initial data load for Alchemist
    
    
    # Trigger to move to weapon selection
    def on_confirm_and_next():
        selected_profession = on_confirm()
        print(f"Debug: Selected profession is {selected_profession}")
        if selected_profession:
            print(f"Debug: The condition is met with {selected_profession}.")  # Debugging line

            # Create and register the weapon panel
            weapon_panel = create_weapon_panel(weapons, ui, on_confirm_weapon)
            ui.register_panel('weapon', weapon_panel)
            ui.show_panel("weapon")  # Show the weapon selection panel
            print("Debug: Attempted to show weapon panel.")
        else:
            print("Debug: Condition not met.")  # Debugging line    

    def on_confirm_weapon():
        selected = ui.weapon_var.get()
        if selected in weapons:
            ui.display_message(f"You have selected {selected}.")
            return selected

    ttk.Button(panel, text="Confirm", command=on_confirm_and_next).grid(row=3, column=0, columnspan=5)

    return panel


# Function to select a profession
def select_profession(professions, ui, weapons):
    # Initialize profession_var in UIManager
    ui.profession_var = tk.StringVar()
    
    def on_confirm():
        print("Debug: Confirm button clicked.")  # Debugging line
        selected = ui.profession_var.get().split(" ")[0]
        print(f"Debug: Profession to be confirmed: {selected}")  # Debugging line
        for p in professions:
            if p['name'] == selected:
                ui.display_message(f"You have selected {selected}.")
                return selected

    all_professions = professions
    profession_panel = create_profession_panel(all_professions, ui, on_confirm, weapons)

    ui.register_panel('profession', profession_panel)
    ui.show_panel('profession')


# Function to create the weapon panel
def create_weapon_panel(weapons, ui, on_confirm):
    print("Weapons before passing to create_weapon_panel:", weapons)  # Debugging Step 1
    print("Debugging: ", type(weapons), weapons)  # Debugging Step 2

    panel = ttk.Frame(ui.main_frame, padding="10")
    
    # Dropdown menu for weapon selection
    ui.weapon_var = tk.StringVar(panel)
    ui.weapon_var.set("Katana")  # Set Katana as the default selection

    # Create the OptionMenu with an empty list initially
    weapon_dropdown = ttk.OptionMenu(panel, ui.weapon_var, "")
    weapon_dropdown.grid(row=0, column=0, columnspan=5, sticky=tk.W + tk.E)

    # Clear the menu and add items back in
    menu = weapon_dropdown['menu']
    menu.delete(0, tk.END)
    sorted_weapons = sorted(weapons.keys())
    for w in sorted_weapons:
        menu.add_command(label=w, command=lambda weapon=w: ui.weapon_var.set(weapon))

    # Create Text widget for weapon details
    details_text = tk.Text(panel, wrap=tk.NONE, width=150, height=40)
    details_text.grid(row=1, column=0, columnspan=5, sticky=tk.N+tk.S+tk.W+tk.E)
    
    # Add a horizontal scrollbar to Text widget
    h_scroll = ttk.Scrollbar(panel, orient='horizontal', command=details_text.xview)
    h_scroll.grid(row=2, column=0, columnspan=5, sticky=tk.W + tk.E)
    details_text['xscrollcommand'] = h_scroll.set
    
    def update_details(*args):
        details_text.delete(1.0, tk.END)  # Clear text once at the start
        print("Updating details for selected weapon.")  # Debugging message
        selected = ui.weapon_var.get()
        print(f"Selected weapon: {selected}")  # Debugging message

        if selected in weapons:  # Check if the selected weapon exists in the weapons dictionary
            for skill in weapons[selected]['skills']:
                details_text.insert(tk.END, "-                                      \n")                   
                details_text.insert(tk.END, f"Skill Name: {skill['name']}\n")
                details_text.insert(tk.END, f"Skill Type: {skill['type']}\n")
                details_text.insert(tk.END, f"Description: {skill['description']}\n")
                details_text.insert(tk.END, f"Effect: {skill['effect']}\n")
                details_text.insert(tk.END, f"AP Cost: {skill['ap_cost']}\n")
                details_text.insert(tk.END, f"Initiative Value: {skill['initiative_value']}\n")
                details_text.insert(tk.END, f"Interruptable: {skill['interruptable']}\n")
                details_text.insert(tk.END, "-                                      \n")       
                details_text.insert(tk.END, "---------------------------------------\n")
             
            

    ui.weapon_var.trace_add('write', update_details)
    update_details()  # Trigger initial data load for Katana
    
    ttk.Button(panel, text="Confirm", command=on_confirm).grid(row=3, column=0, columnspan=5)
    
    return panel

# Function to select a weapon
def select_weapon(weapons, ui):
    # Initialize weapon_var in UIManager
    ui.weapon_var = tk.StringVar()

    def on_confirm():
        print("Debug: Confirm button clicked.")  # Debugging message
        selected = ui.weapon_var.get()
        print(f"Debug: Weapon to be confirmed: {selected}")  # Debugging message
        if selected in weapons:
            ui.display_message(f"You have selected {selected}.")
            return selected

    weapon_panel = create_weapon_panel(weapons, ui, on_confirm)
    ui.register_panel('weapon', weapon_panel)
    ui.show_panel('weapon')
