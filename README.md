Delta Calculator
The Delta Calculator is a simple technical tool that calculates the delta value based on the user’s input for the VIX level, current price, and moving average (MA). This application is built using Python and Tkinter and is designed to be intuitive and easy to use for those who want to calculate delta without using more complex financial software.

Table of Contents
Overview
Parameters
Calculation
Usage
Installation
Contributing
Overview
The Delta Calculator application is designed to:

Allow users to manually input VIX, current price, and moving average values.
Automatically compute the delta using a predefined formula.
Display the calculated delta in a user-friendly interface.
Support windowed mode with resizing capabilities.
This application is perfect for users who want a simple yet effective way to calculate delta values based on their analysis.

Parameters
The Delta Calculator uses the following inputs provided by the user:

VIX Level - Value of the VIX Index
Current Price - Current price of the asset (e.g., an index like US500)
Moving Average - 30-period moving average (or another period of choice)

These parameters are manually entered by the user and are used in the calculation of the delta.

Calculation
The delta is calculated using the following steps:

User Inputs:

VIX Level: The VIX value is divided by 100.
Current Price and Moving Average: The current price is compared to the moving average.
Delta Formula:
The formula used to calculate delta is:
(VIX / 100) + ((current_price - moving_avg) / moving_avg) + ((VIX / 100) * sqrt(30 / 365) / 2)

Clamping Delta:
The calculated delta is then clamped between 0.12 and 0.20 to ensure stability:
delta = max(0.12, min(0.20, delta_formula))

Usage
To use the Delta Calculator:

Run the Application: Launch the Delta Calculator application.
Enter Values: Input the VIX level, current price, and moving average (MA) in the respective fields.
Calculate Delta: Click the Calculate Delta button to compute the delta value.
View Results: The calculated delta will be displayed below the input fields.
Installation
To install and run the Delta Calculator:

Clone the repository:
git clone https://github.com/your-username/delta-calculator.git
cd delta-calculator

Install dependencies (if needed):
sudo apt-get install python3-tk

Run the application:
python3 delta_calculator.py

Contributing
Contributions are welcome! If you have suggestions or improvements, feel free to submit a pull request or open an issue.
