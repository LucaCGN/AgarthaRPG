import tkinter as tk
from tkinter import ttk
import firestore_init
from login_manager import login_user
import character_manager
import ui_manager
from character_rolling import roll_stats
import character_creation


class App:
    def __init__(self):
        # Initialize Firestore
        self.db, self.professions, self.weapons = firestore_init.initialize_firestore()
        
        # Initialize the UI Manager
        self.ui = ui_manager.UIManager()
        
        # Initialize user_id
        self.user_id = None

        # Roll stats once during initialization
        self.rolled_stats = roll_stats()

        # Create and register panels
        self.login_panel = self.create_login_panel()
        self.ui.register_panel("login", self.login_panel)

        self.character_creation_panel = self.create_character_creation_panel()
        self.ui.register_panel("character_creation", self.character_creation_panel)

        self.roll_stats_panel = self.ui.create_roll_stats_panel(self.rolled_stats, self.show_assign_stats_panel)
        self.ui.register_panel("roll_stats", self.roll_stats_panel)

        self.assign_stats_panel = self.ui.create_assign_stats_panel(self.rolled_stats, self.assign_stats_and_proceed)
        self.ui.register_panel("assign_stats", self.assign_stats_panel)

        # Show the first panel
        self.ui.show_panel("login")

    def create_login_panel(self):
        panel = ttk.Frame(self.ui.main_frame, padding="10")
        ttk.Label(panel, text="Email:").grid(row=0, column=0, sticky=tk.W)
        email_entry = ttk.Entry(panel, width=30)
        email_entry.grid(row=0, column=1)

        ttk.Label(panel, text="Password:").grid(row=1, column=0, sticky=tk.W)
        password_entry = ttk.Entry(panel, width=30, show="*")
        password_entry.grid(row=1, column=1)

        ttk.Button(panel, text="Login", command=lambda: self.login(email_entry.get(), password_entry.get())).grid(row=2, columnspan=2)

        return panel

    def create_character_creation_panel(self):
        panel = ttk.Frame(self.ui.main_frame, padding="10")
        ttk.Label(panel, text="Welcome to character creation!").grid(row=0, column=0, sticky=tk.W)
        ttk.Button(panel, text="Create Character", command=self.create_character).grid(row=1, column=0)

        return panel

    def login(self, email, password):
        self.user_id = login_user(self.db, email, password, self.ui)
        if self.user_id:
            self.on_successful_login()
        else:
            print("Debug: Login failed.")
            self.ui.show_panel("login")

    def create_character(self):
        if self.user_id:
            # Call character_manager to handle character creation and detailing
            character_manager.create_and_detail_character(
                self.db, self.professions, self.weapons, 
                self.user_id, self.ui, self.assigned_stats, self.rolled_stats
            )
            
            # Start the profession selection process
            character_creation.select_profession(self.professions, self.ui, self.weapons)

            
        else:
            self.ui.display_message("Please login first.")


    def on_successful_login(self):
        print("Debug: Login successful.")
        self.ui.show_panel("roll_stats")

    def show_assign_stats_panel(self):
        self.ui.show_panel("assign_stats")

    def assign_stats_and_proceed(self):
        assigned_stats = self.ui.get_assigned_stats_from_dropdowns()

        # Validation logic
        if sorted(assigned_stats.values()) != sorted(self.rolled_stats):
            self.ui.display_message("Assigned stats don't match the rolled stats. Please try again.")
            return

        if not assigned_stats:  # Validate captured stats (you can add more validations)
            self.ui.display_message("Please assign all stats before proceeding.")
            return

        # Store the assigned stats for future use or proceed to the next step
        self.assigned_stats = assigned_stats

        # Move to the next step in character creation
        # The weapons are also passed now
        character_manager.create_and_detail_character(self.db, self.professions, self.weapons, self.user_id, self.ui, self.assigned_stats, self.rolled_stats)
        
        # Show the next panel, which could be for selecting weapons or other tasks
        self.ui.show_panel("character_creation")  # or whatever the next panel is

if __name__ == "__main__":
    app = App()
    app.ui.run()
