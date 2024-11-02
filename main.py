import tkinter as tk
from math import sqrt

# Function to calculate delta based on user inputs
def calculate_delta():
    try:
        vix = float(vix_entry.get())
        current_price = float(price_entry.get())
        moving_avg = float(ma_entry.get())

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

# Set window size and dark background color
root.geometry("800x600")
root.config(bg="#1c1c1c")  # Dark background

# Modern font configuration
label_font = ("Roboto", 18, "bold")
entry_font = ("Roboto", 18)
result_font = ("Roboto", 20, "bold")
button_font = ("Roboto", 18)

# Function for button hover effect
def on_enter(event):
    calculate_button.config(bg="#00BFFF", fg="black")  # Bright blue on hover

def on_leave(event):
    calculate_button.config(bg="#333", fg="#00BFFF")   # Dark button, bright blue text

# Create and place labels and entry fields
tk.Label(root, text="Enter VIX Level:", font=label_font, bg="#1c1c1c", fg="#00BFFF").grid(row=0, column=0, padx=20, pady=20)
vix_entry = tk.Entry(root, font=entry_font, bg="#333", fg="#00BFFF", insertbackground="#00BFFF", relief="flat")
vix_entry.grid(row=0, column=1, padx=20, pady=20)

tk.Label(root, text="Enter Current Price:", font=label_font, bg="#1c1c1c", fg="#00BFFF").grid(row=1, column=0, padx=20, pady=20)
price_entry = tk.Entry(root, font=entry_font, bg="#333", fg="#00BFFF", insertbackground="#00BFFF", relief="flat")
price_entry.grid(row=1, column=1, padx=20, pady=20)

tk.Label(root, text="Enter Moving Average (MA):", font=label_font, bg="#1c1c1c", fg="#00BFFF").grid(row=2, column=0, padx=20, pady=20)
ma_entry = tk.Entry(root, font=entry_font, bg="#333", fg="#00BFFF", insertbackground="#00BFFF", relief="flat")
ma_entry.grid(row=2, column=1, padx=20, pady=20)

# Create a calculate button with color and hover effect
calculate_button = tk.Button(root, text="Calculate Delta", font=button_font, bg="#333", fg="#00BFFF", relief="flat", command=calculate_delta)
calculate_button.grid(row=3, column=0, columnspan=2, pady=20)
calculate_button.bind("<Enter>", on_enter)
calculate_button.bind("<Leave>", on_leave)

# Create a label to display the result
result_label = tk.Label(root, text="", font=result_font, bg="#1c1c1c", fg="#00BFFF")
result_label.grid(row=4, column=0, columnspan=2, pady=30)

# Start the Tkinter event loop
root.mainloop()
