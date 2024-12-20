import tkinter as tk
from tkinter import ttk
from math import sqrt

# Function to calculate delta based on user inputs
def calculate_delta():
    try:
        vix = float(vix_var.get())
        current_price = float(price_var.get())
        moving_avg = float(ma_var.get())

        # Formula calculation
        delta_formula = (vix / 100) + ((current_price - moving_avg) / moving_avg) + ((vix / 100) * sqrt(30 / 365) / 2)

        # Clamp the delta between 0.16 and 0.20
        delta = max(0.16, min(0.20, delta_formula))

        # Display the result
        result_label.config(text=f"Calculated Delta: {delta:.4f}")
    except ValueError:
        result_label.config(text="Invalid input, please enter numeric values")

# Create the main window
root = tk.Tk()
root.title("Delta Calculator")

# Set window size and modern background color
root.geometry("500x400")
root.config(bg="#2C2C2C")  # Dark grey background

# Define styles for labels and buttons
style = ttk.Style()
style.theme_use('clam')  # Use a modern theme
style.configure("TLabel", font=("Arial", 16), background="#2C2C2C", foreground="#00BFFF")
style.configure("TButton", font=("Arial", 16), background="#3D3D3D", foreground="#00BFFF", borderwidth=0)

# Map the button hover effects
style.map("TButton", background=[("active", "#00BFFF"), ("!active", "#3D3D3D")],
          foreground=[("active", "black"), ("!active", "#00BFFF")])

# Create separate variables for each entry field
vix_var = tk.StringVar()
price_var = tk.StringVar()
ma_var = tk.StringVar()

# Create labels and entry fields
ttk.Label(root, text="Enter VIX Level:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
vix_entry = tk.Entry(root, textvariable=vix_var, font=("Arial", 16), bg="#2C2C2C", fg="#00BFFF",
                     justify='center', insertbackground="#00BFFF", width=10)
vix_entry.grid(row=0, column=1, padx=10, pady=10)

ttk.Label(root, text="Enter Current Price:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
price_entry = tk.Entry(root, textvariable=price_var, font=("Arial", 16), bg="#2C2C2C", fg="#00BFFF",
                       justify='center', insertbackground="#00BFFF", width=10)
price_entry.grid(row=1, column=1, padx=10, pady=10)

ttk.Label(root, text="Enter Moving Average (MA):").grid(row=2, column=0, padx=10, pady=10, sticky="e")
ma_entry = tk.Entry(root, textvariable=ma_var, font=("Arial", 16), bg="#2C2C2C", fg="#00BFFF",
                    justify='center', insertbackground="#00BFFF", width=10)
ma_entry.grid(row=2, column=1, padx=10, pady=10)

# Create a calculate button
calculate_button = ttk.Button(root, text="Calculate Delta", command=calculate_delta)
calculate_button.grid(row=3, column=0, columnspan=2, pady=20, ipadx=10, ipady=5)

# Create a label to display the result
result_label = ttk.Label(root, text="", font=("Arial", 16), background="#2C2C2C", foreground="#00BFFF")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()
