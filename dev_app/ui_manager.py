import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox
from tkinter import Canvas, Frame, Scrollbar

class UIManager:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Agartha RPG")
        
        self.main_frame = ttk.Frame(self.window, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.panels = {}
        
    def register_panel(self, name, panel):
        self.panels[name] = panel
        panel.grid_forget()
        
    def show_panel(self, name):
        for panel in self.panels.values():
            panel.grid_forget()
        self.panels[name].grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
    def get_input(self, prompt):
        return simpledialog.askstring("Input", prompt)
    
    def display_message(self, message):
        messagebox.showinfo("Information", message)
        
    def run(self):
        self.window.mainloop()

    def create_roll_stats_panel(self, rolled_stats, on_confirm):
        panel = ttk.Frame(self.main_frame, padding="10")
        ttk.Label(panel, text=f"Rolled Stats: {rolled_stats}").grid(row=0, column=0, sticky=tk.W)
        ttk.Button(panel, text="Confirm", command=on_confirm).grid(row=1, column=0)
        return panel

    def create_assign_stats_panel(self, rolled_stats, on_assign):
        panel = ttk.Frame(self.main_frame, padding="10")
        
        # Display rolled stats
        ttk.Label(panel, text=f"Rolled Stats: {rolled_stats}").grid(row=0, column=0, sticky=tk.W)
        
        ttk.Label(panel, text="Assign stats to attributes:").grid(row=1, column=0, sticky=tk.W)  # Moved to row=1 to avoid overlay
        self.attribute_dropdowns = {}  # Create a dictionary to hold dropdown variables
        attributes = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']
        row = 2  # Starting from row 2 to avoid overlay

        for attr in attributes:
            ttk.Label(panel, text=f"{attr}:").grid(row=row, column=0, sticky=tk.W)
            var = tk.StringVar(panel)
            var.set("Select")  # initial value
            dropdown = ttk.OptionMenu(panel, var, *rolled_stats)
            dropdown.grid(row=row, column=1)
            self.attribute_dropdowns[attr] = var  # Store the variable
            row += 1

        ttk.Button(panel, text="Assign", command=on_assign).grid(row=row, column=0)
        return panel

    def get_assigned_stats_from_dropdowns(self):
        assigned_stats = {}
        for attr, var in self.attribute_dropdowns.items():
            assigned_stats[attr] = int(var.get())
        return assigned_stats






