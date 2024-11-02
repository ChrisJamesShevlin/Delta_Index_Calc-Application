import tkinter as tk
from tkinter import ttk
from math import sqrt

# Function to handle number pad button clicks
def button_click(value):
    # Determine which entry field is currently focused
    if vix_entry.focus_get() == vix_entry:
        current_text = vix_var.get()
        vix_var.set(current_text + value)
    elif price_entry.focus_get() == price_entry:
        current_text = price_var.get()
        price_var.set(current_text + value)
    elif ma_entry.focus_get() == ma_entry:
        current_text = ma_var.get()
        ma_var.set(current_text + value)

# Function to clear the entry field
def clear_entry():
    # Determine which entry field is currently focused
    if vix_entry.focus_get() == vix_entry:
        vix_var.set("")
    elif price_entry.focus_get() == price_entry:
        price_var.set("")
    elif ma_entry.focus_get() == ma_entry:
        ma_var.set("")

# Function to calculate delta based on user inputs
def calculate_delta():
    try:
        vix = float(vix_var.get())
        current_price = float(price_var.get())
        moving_avg = float(ma_var.get())

        # Formula calculation
        delta_formula = (vix / 100) + ((current_price - moving_avg) / moving_avg) + ((vix / 100) * sqrt(30 / 365) / 2)

        # Clamp the delta between 0.12 and 0.20
        delta = max(0.12, min(0.20, delta_formula))

        # Display the result
        result_label.config(text=f"Calculated Delta: {delta:.4f}")
    except ValueError:
        result_label.config(text="Invalid input, please enter numeric values")

# Create the main window
root = tk.Tk()
root.title("Delta Calculator")

# Set window size and modern background color
root.geometry("1024x900")
root.config(bg="#2C2C2C")  # Dark grey background

# Define styles for labels and buttons
style = ttk.Style()
style.theme_use('clam')  # Use a modern theme
style.configure("TLabel", font=("Arial", 24), background="#2C2C2C", foreground="#00BFFF")
style.configure("TButton", font=("Arial", 24), background="#3D3D3D", foreground="#00BFFF", borderwidth=0)

# Map the button hover effects
style.map("TButton", background=[("active", "#00BFFF"), ("!active", "#3D3D3D")],
          foreground=[("active", "black"), ("!active", "#00BFFF")])

# Centering frame for alignment
center_frame = tk.Frame(root, bg="#2C2C2C")
center_frame.place(relx=0.5, rely=0.5, anchor="center")

# Create separate variables for each entry field
vix_var = tk.StringVar()
price_var = tk.StringVar()
ma_var = tk.StringVar()

# Create labels and entry fields with explicit font settings
ttk.Label(center_frame, text="Enter VIX Level:").grid(row=0, column=0, padx=10, pady=(20, 10), sticky="e")
vix_entry = tk.Entry(center_frame, textvariable=vix_var, font=("Arial", 32, 'bold'), 
                     bg="#2C2C2C", fg="#00BFFF", justify='center', insertbackground="#00BFFF", width=7)
vix_entry.grid(row=0, column=1, padx=10, pady=(20, 10), ipady=10)  # Adjusted width for six digits

ttk.Label(center_frame, text="Enter Current Price:").grid(row=1, column=0, padx=10, pady=(10, 10), sticky="e")
price_entry = tk.Entry(center_frame, textvariable=price_var, font=("Arial", 32, 'bold'), 
                       bg="#2C2C2C", fg="#00BFFF", justify='center', insertbackground="#00BFFF", width=7)
price_entry.grid(row=1, column=1, padx=10, pady=(10, 10), ipady=10)  # Adjusted width for six digits

ttk.Label(center_frame, text="Enter Moving Average (MA):").grid(row=2, column=0, padx=10, pady=(10, 20), sticky="e")
ma_entry = tk.Entry(center_frame, textvariable=ma_var, font=("Arial", 32, 'bold'), 
                    bg="#2C2C2C", fg="#00BFFF", justify='center', insertbackground="#00BFFF", width=7)
ma_entry.grid(row=2, column=1, padx=10, pady=(10, 20), ipady=10)  # Adjusted width for six digits

# Create a frame for the number pad
number_pad_frame = tk.Frame(center_frame, bg="#2C2C2C")
number_pad_frame.grid(row=3, column=0, columnspan=2, pady=(20, 40))

# Number pad buttons
buttons = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0', 'C'  # C for clear
]

# Add buttons to the number pad
for i, button in enumerate(buttons):
    if button == 'C':
        action = clear_entry
    else:
        action = lambda value=button: button_click(value)
    
    btn = tk.Button(number_pad_frame, text=button, font=("Arial", 24), width=5, height=2,
                    bg="#3D3D3D", fg="#00BFFF", command=action)
    btn.grid(row=i // 3, column=i % 3, padx=5, pady=5)

# Create a calculate button
calculate_button = ttk.Button(center_frame, text="Calculate Delta", command=calculate_delta)
calculate_button.grid(row=4, column=0, columnspan=2, pady=(30, 40), ipadx=20, ipady=10)

# Create a label to display the result
result_label = ttk.Label(center_frame, text="", font=("Arial", 24), background="#2C2C2C", foreground="#00BFFF")
result_label.grid(row=5, column=0, columnspan=2, pady=20)

# Start the Tkinter event loop
root.mainloop()
