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

# Set the window to be resizable, windowed mode (not full screen)
root.geometry("800x600")  # You can change the size as needed
root.resizable(True, True)  # Allow the window to be resizable

# Create and place labels and entry fields
tk.Label(root, text="Enter VIX Level:", font=("Arial", 20)).grid(row=0, column=0, padx=20, pady=20)
vix_entry = tk.Entry(root, font=("Arial", 20))
vix_entry.grid(row=0, column=1, padx=20, pady=20)

tk.Label(root, text="Enter Current Price:", font=("Arial", 20)).grid(row=1, column=0, padx=20, pady=20)
price_entry = tk.Entry(root, font=("Arial", 20))
price_entry.grid(row=1, column=1, padx=20, pady=20)

tk.Label(root, text="Enter Moving Average (MA):", font=("Arial", 20)).grid(row=2, column=0, padx=20, pady=20)
ma_entry = tk.Entry(root, font=("Arial", 20))
ma_entry.grid(row=2, column=1, padx=20, pady=20)

# Create a calculate button
calculate_button = tk.Button(root, text="Calculate Delta", font=("Arial", 20), command=calculate_delta)
calculate_button.grid(row=3, column=0, columnspan=2, pady=20)

# Create a label to display the result
result_label = tk.Label(root, text="", font=("Arial", 20))
result_label.grid(row=4, column=0, columnspan=2, pady=20)

# Start the Tkinter event loop
root.mainloop()
