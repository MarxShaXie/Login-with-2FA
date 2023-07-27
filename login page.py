import tkinter as tk
import os

def save_credentials(username, password):
    with open("C://user_credentials.txt", "w") as file:
        file.write(f"{username},{password}")

def switch_screen():
    if signup_frame.winfo_ismapped():
        title_label.config(text="Login")
        signup_frame.grid_remove()
        login_frame.grid(row=0, column=0, padx=10, pady=10)
        switch_button.config(text="Signup")
    else:
        title_label.config(text="Signup")
        login_frame.grid_remove()
        signup_frame.grid(row=0, column=0, padx=10, pady=10)
        switch_button.config(text="Login")

def login():
    with open("C://user_credentials.txt", "r") as file:
        stored_data = file.readline().strip().split(',')
        stored_username, stored_password = stored_data

    if username_entry.get() == stored_username and password_entry.get() == stored_password:
        login_status.config(text="Login successful!")
    else:
        login_status.config(text="Login failed!")

def signup():
    username = signup_username_entry.get()
    password = signup_password_entry.get()
    save_credentials(username, password)
    signup_status.config(text="Signup successful!")

# Create the main application window
root = tk.Tk()
root.title("Login / Signup")
root.geometry("500x333")  # Set the initial window size

# Title label
title_label = tk.Label(root, text="Welcome")
title_label.grid(row=0, column=0, padx=10, pady=10)

# Frames for login and signup
login_frame = tk.Frame(root)
signup_frame = tk.Frame(root)

# Login widgets
login_username_label = tk.Label(login_frame, text="Username:")
login_username_label.grid(row=0, column=0, padx=5, pady=5)

username_entry = tk.Entry(login_frame)
username_entry.grid(row=1, column=0, padx=5, pady=5)

login_password_label = tk.Label(login_frame, text="Password:")
login_password_label.grid(row=2, column=0, padx=5, pady=5)

password_entry = tk.Entry(login_frame, show="*")
password_entry.grid(row=3, column=0, padx=5, pady=5)

login_button = tk.Button(login_frame, text="Login", command=login)
login_button.grid(row=4, column=0, padx=5, pady=5)

login_status = tk.Label(login_frame, text="")
login_status.grid(row=5, column=0, padx=5, pady=5)

# Signup widgets
signup_username_label = tk.Label(signup_frame, text="Username:")
signup_username_label.grid(row=0, column=0, padx=5, pady=5)

signup_username_entry = tk.Entry(signup_frame)
signup_username_entry.grid(row=1, column=0, padx=5, pady=5)

signup_password_label = tk.Label(signup_frame, text="Password:")
signup_password_label.grid(row=2, column=0, padx=5, pady=5)

signup_password_entry = tk.Entry(signup_frame, show="*")
signup_password_entry.grid(row=3, column=0, padx=5, pady=5)

signup_button = tk.Button(signup_frame, text="Signup", command=signup)
signup_button.grid(row=4, column=0, padx=5, pady=5)

signup_status = tk.Label(signup_frame, text="")
signup_status.grid(row=5, column=0, padx=5, pady=5)

# Set the initial content to login
login_frame.grid(row=0, column=0, padx=10, pady=10)

# Button to switch between login and signup
switch_button = tk.Button(root, text="Signup", command=switch_screen)
switch_button.grid(row=1, column=0, padx=10, pady=10, sticky="w")

# Start the main event loop
root.mainloop()