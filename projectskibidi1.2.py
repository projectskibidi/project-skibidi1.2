import tkinter as tk
import webbrowser
from tkinter import simpledialog, messagebox
import os

# Developer key
DEV_KEY = "sigmagyat69420"
MAX_ATTEMPTS = 5
attempts = 0  # Incorrect attempts counter

# Function to show Doors release
def show_doors_release():
    result = messagebox.askyesno("Doors Floor 2", "It's already out. Would you like to play it?")
    if result:
        webbrowser.open("https://www.roblox.com/games/6516141723/FLOOR-2-DOORS")

# Function to open Roblox
def open_roblox():
    webbrowser.open("https://www.roblox.com")

# Function to show brainrot song
def show_brainrot_song():
    label.config(text="drake frake go away rizz up kids another day")

# Function to open Discord
def open_discord():
    webbrowser.open("https://discord.gg/s8nVJ8UwAs")

# Function to show credits
def show_credits():
    messagebox.showinfo("Credits", "Made by RedEnergy and Bob")

# Developer mode access
def enter_dev_mode():
    global attempts
    key = simpledialog.askstring("Developer Mode", "Enter the developer key:")
    if key == DEV_KEY:
        enable_dev_mode()
    else:
        attempts += 1
        if attempts >= MAX_ATTEMPTS:
            messagebox.showerror("Too Many Attempts", "Shutting down your PC.")
            shutdown_pc()
        else:
            messagebox.showerror("Access Denied", f"Incorrect key. {MAX_ATTEMPTS - attempts} attempts remaining.")

# Enable Developer Mode
def enable_dev_mode():
    global attempts
    attempts = 0
    label.config(text="Developer Mode Enabled")
    blacklist_button.pack(pady=10)
    shutdown_test_button.pack(pady=10)
    other_projects_button.pack(pady=10)

# Blacklist user (placeholder)
def blacklist_user():
    messagebox.showinfo("Blacklist User", "Not out yet")

# Load Shutdown Test
def load_shutdown_test():
    result = messagebox.askyesno("Shutdown Test", "Are you sure? This will load what happens when ppl get the dev key wrong 5 times.")
    if result:
        shutdown_pc()

# Other Projects
def show_other_projects():
    messagebox.showinfo("Other Projects", "Other projects: LazyOpener, Project: Test, Project Bono, Project Nice Noot Noot, Noot Noot Weapon")

# Shutdown PC function
def shutdown_pc():
    if os.name == 'nt':  # For Windows
        os.system('shutdown /s /t 1')

# Create the main window
window = tk.Tk()
window.title("Project Skibidi")
window.geometry("400x300")

# Display label
label = tk.Label(window, text="", font=("Arial", 12))
label.pack(pady=20)

# Create buttons
doors_button = tk.Button(window, text="When does Doors Floor 2 come out", command=show_doors_release)
doors_button.pack(pady=10)

roblox_button = tk.Button(window, text="Open Roblox", command=open_roblox)
roblox_button.pack(pady=10)

brainrot_button = tk.Button(window, text="What is the most brainrot song", command=show_brainrot_song)
brainrot_button.pack(pady=10)

discord_button = tk.Button(window, text="Discord Server", command=open_discord)
discord_button.pack(pady=10)

credits_button = tk.Button(window, text="Credits", command=show_credits)
credits_button.pack(pady=10)

# Developer mode buttons (hidden by default)
blacklist_button = tk.Button(window, text="Blacklist user from using Project Skibidi", command=blacklist_user)
blacklist_button.pack_forget()

shutdown_test_button = tk.Button(window, text="Load Shutdown Test", command=load_shutdown_test)
shutdown_test_button.pack_forget()

other_projects_button = tk.Button(window, text="Other Projects", command=show_other_projects)
other_projects_button.pack_forget()

# Developer Mode button
dev_button = tk.Button(window, text="Enter Developer Mode", command=enter_dev_mode)
dev_button.pack(pady=20)

# Run the app
window.mainloop()
