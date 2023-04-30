# Import the Paramiko library, which is used to connect to Cisco switches over SSH
import paramiko

# Import the tkinter library, which is used to create the graphical user interface (GUI)
import tkinter as tk
from tkinter import ttk, messagebox

# Define a function called "ssh_configure" that connects to a Cisco switch over SSH and executes a list of commands
def ssh_configure(host, username, password, commands):
    try:
        # Create an SSH client and connect to the Cisco switch using the provided host, username, and password
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=username, password=password)

        # Execute each command in the list of commands on the Cisco switch
        for command in commands:
            ssh.exec_command(command)

        # Close the SSH connection and show a success message
        ssh.close()
        messagebox.showinfo("Success", "Commands executed successfully")
    
    # If there's an error, show an error message
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Define a function called "submit_form" that gets the values from the GUI inputs and calls the "ssh_configure" function
def submit_form():
    # Get the host, username, password, and commands from the GUI inputs
    host = host_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    commands = commands_text.get("1.0", tk.END).splitlines()

    # Call the "ssh_configure" function with the provided inputs
    ssh_configure(host, username, password, commands)

# Create a GUI window using tkinter
app = tk.Tk()
app.title("Cisco Switch Configurator")

# Create a frame to hold the GUI elements
frame = ttk.Frame(app, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Create GUI elements for the host, username, password, and commands
host_label = ttk.Label(frame, text="Host:")
host_label.grid(row=0, column=0, sticky=tk.W)
host_entry = ttk.Entry(frame)
host_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

username_label = ttk.Label(frame, text="Username:")
username_label.grid(row=1, column=0, sticky=tk.W)
username_entry = ttk.Entry(frame)
username_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

password_label = ttk.Label(frame, text="Password:")
password_label.grid(row=2, column=0, sticky=tk.W)
password_entry = ttk.Entry(frame, show="*")
password_entry.grid(row=2, column=1, sticky=(tk.W, tk.E))

commands_label = ttk.Label(frame, text="Commands:")
commands_label.grid(row=3, column=0, sticky=tk.W)
commands_text = tk.Text(frame, width=30, height=10)
commands_text.grid(row=3, column=1, sticky=(tk.W, tk.E))

# Create a "Execute" button that calls the "submit_form" function
submit_button = ttk.Button(frame, text="Execute", command=submit_form)
submit_button.grid(row=4, column=1, sticky=tk.E)

# Configure the GUI elements to be displayed correctly
frame.columnconfigure(1, weight=1)
frame.rowconfigure(3, weight=1)

# Start the GUI window and wait for user input
app.mainloop()

# NOTES:
# This code
