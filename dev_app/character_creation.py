import tkinter as tk
from tkinter import ttk
from tkinter import Canvas, Frame, Scrollbar

# Function to create the profession panel
def create_profession_panel(professions, ui, on_confirm, weapons):
    panel = ttk.Frame(ui.main_frame, padding="10")
    
    # Dropdown menu for profession selection
    var = tk.StringVar(panel)
    var.set("Alchemist")  # Set Alchemist as the default selection

    # Create the OptionMenu with an empty list initially
    profession_dropdown = ttk.OptionMenu(panel, var, "")
    profession_dropdown.grid(row=0, column=0, columnspan=5, sticky=tk.W + tk.E)

    # Clear the menu and add items back in
    menu = profession_dropdown['menu']
    menu.delete(0, tk.END)
    all_professions = []
    for stat, prof_list in professions.items():
        all_professions.extend(prof_list)
    sorted_professions = sorted([(f"{p['name']}") for p in all_professions])


    for p in sorted_professions:
        menu.add_command(label=p, command=lambda profession=p: var.set(profession))

    
    # Create Text widget for profession details
    details_text = tk.Text(panel, wrap=tk.NONE, width=150, height=40)  # Tripled the width and height
    details_text.grid(row=1, column=0, columnspan=5, sticky=tk.N+tk.S+tk.W+tk.E)
    
    # Add a horizontal scrollbar to Text widget
    h_scroll = ttk.Scrollbar(panel, orient='horizontal', command=details_text.xview)
    h_scroll.grid(row=2, column=0, columnspan=5, sticky=tk.W + tk.E)
    details_text['xscrollcommand'] = h_scroll.set
    
    def update_details(*args):
        selected = var.get()
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
    
    var.trace_add('write', update_details)
    update_details()  # Trigger initial data load for Alchemist
    
    
    # Trigger to move to weapon selection
    def on_confirm_and_next():
        selected_profession = on_confirm()
        if selected_profession:
            # Create and register the weapon panel
            weapon_panel = create_weapon_panel(weapons, ui, on_confirm_weapon)
            ui.register_panel('weapon', weapon_panel)
            ui.show_panel("weapon")  # Show the weapon selection panel

    def on_confirm_weapon():
        selected = ui.weapon_var.get()
        if selected in weapons:
            ui.display_message(f"You have selected {selected}.")
            return selected

    ttk.Button(panel, text="Confirm", command=on_confirm_and_next).grid(row=3, column=0, columnspan=5)

    return panel


# Function to select a profession
def select_profession(professions, ui, weapons):
    def on_confirm():
        selected = ui.profession_var.get().split(" ")[0]
        for p in professions:
            if p['name'] == selected:
                ui.display_message(f"You have selected {selected}.")
                return selected

    ui.profession_var = tk.StringVar()
    all_professions = []
    for stat, prof_list in professions.items():
        all_professions.extend(prof_list)
    profession_panel = create_profession_panel(all_professions, ui, on_confirm, weapons)

    ui.register_panel('profession', profession_panel)
    ui.show_panel('profession')


# Function to create the weapon panel
def create_weapon_panel(weapons, ui, on_confirm):
    panel = ttk.Frame(ui.main_frame, padding="10")
    
    # Dropdown menu for weapon selection
    var = tk.StringVar(panel)
    var.set("Katana")  # Set Katana as the default selection

    # Create the OptionMenu with an empty list initially
    weapon_dropdown = ttk.OptionMenu(panel, var, "")
    weapon_dropdown.grid(row=0, column=0, columnspan=5, sticky=tk.W + tk.E)

    # Clear the menu and add items back in
    menu = weapon_dropdown['menu']
    menu.delete(0, tk.END)
    sorted_weapons = sorted(weapons.keys())

    for w in sorted_weapons:
        menu.add_command(label=w, command=lambda weapon=w: var.set(weapon))

    # Create Text widget for weapon details
    details_text = tk.Text(panel, wrap=tk.NONE, width=150, height=40)
    details_text.grid(row=1, column=0, columnspan=5, sticky=tk.N+tk.S+tk.W+tk.E)
    
    # Add a horizontal scrollbar to Text widget
    h_scroll = ttk.Scrollbar(panel, orient='horizontal', command=details_text.xview)
    h_scroll.grid(row=2, column=0, columnspan=5, sticky=tk.W + tk.E)
    details_text['xscrollcommand'] = h_scroll.set
    
    def update_details(*args):
        details_text.delete(1.0, tk.END)  # Clear text once at the start
        selected = var.get()
        if selected in weapons:  # Check if the selected weapon exists in the weapons dictionary
            for skill in weapons[selected]:
                details_text.insert(tk.END, f"Skill Name: {skill['name']}\n")
                details_text.insert(tk.END, f"Skill Type: {skill['type']}\n")
                details_text.insert(tk.END, f"Description: {skill['description']}\n")
                details_text.insert(tk.END, f"Effect: {skill['effect']}\n")
                details_text.insert(tk.END, f"AP Cost: {skill['ap_cost']}\n")
                details_text.insert(tk.END, f"Initiative Value: {skill['initiative_value']}\n")
                details_text.insert(tk.END, f"Interruptable: {skill['interruptable']}\n")
                details_text.insert(tk.END, "---------------------------------------\n")

    
    var.trace_add('write', update_details)
    update_details()  # Trigger initial data load for Katana
    
    ttk.Button(panel, text="Confirm", command=on_confirm).grid(row=3, column=0, columnspan=5)
    
    return panel

# Function to select a weapon
def select_weapon(weapons, ui):
    def on_confirm():
        selected = ui.weapon_var.get()
        if selected in weapons:
            ui.display_message(f"You have selected {selected}.")
            return selected

    ui.weapon_var = tk.StringVar()
    weapon_panel = create_weapon_panel(weapons, ui, on_confirm)
    ui.register_panel('weapon', weapon_panel)
    ui.show_panel('weapon')
