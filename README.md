# Delta Calculator GUI Application

This repository contains a simple **Delta Calculator** built with **Python** and **Tkinter**. The application calculates delta values based on user inputs for **VIX level**, **Current Price**, and a **Moving Average (MA)**. The delta value is clamped between 0.12 and 0.20 and displayed within the graphical user interface (GUI).

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Error Handling](#error-handling)
- [License](#license)

## Overview

This Python application provides a user-friendly interface for calculating the delta using the following formula:

```
delta = max(0.12, min(0.20, (VIX / 100) + ((Current Price - Moving Average) / Moving Average) + ((VIX / 100) * sqrt(30 / 365) / 2)))
```

- The delta is calculated based on **VIX**, **Current Price**, and **Moving Average** inputs provided by the user.
- The resulting delta is clamped between 0.12 and 0.20 and displayed on the GUI.

## Features

- **GUI Interface**: Built using Tkinter, with entry fields for user input and a result display.
- **Delta Calculation**: Implements a mathematical formula to calculate delta based on input values.
- **Input Validation**: Ensures numeric values are entered; displays an error message for invalid inputs.
- **Resizable Window**: The window is resizable to accommodate different screen sizes.

## Prerequisites

Before running this application, ensure you have:

- **Python 3.x** installed on your machine.
- **Tkinter** library (comes pre-installed with most Python distributions).

## Installation

1. **Clone this repository**:
   ```bash
   git clone https://github.com/your-username/delta-calculator-gui.git
   cd delta-calculator-gui
   ```

2. **Install dependencies** (optional):
   If you're using a custom environment, you might need to install Tkinter, though it's typically included with Python:
   ```bash
   pip install tk
   ```

3. **Run the application**:
   Execute the Python script to launch the Delta Calculator GUI:
   ```bash
   python delta_calculator.py
   ```

## Usage

Once the application is running, follow these steps:

1. **Enter the VIX level**:  
   Input the current VIX level (a volatility index expressed as a percentage).
   
2. **Enter the Current Price**:  
   Input the current price of the underlying asset.

3. **Enter the Moving Average (MA)**:  
   Input the moving average value you are working with (typically a 50-day or 200-day moving average).

4. **Click "Calculate Delta"**:  
   The result will be displayed on the GUI, showing the clamped delta value between 0.12 and 0.20.

### Example:

| Input Field            | Example Value |
|------------------------|---------------|
| VIX Level              | 18.5          |
| Current Price          | 1250          |
| Moving Average (MA)    | 1200          |

**Result**:  
```
Calculated Delta: 0.1648
```

## Customization

1. **Adjust Clamping Values**:  
   If you want to change the delta clamping range, modify the following lines in the code:
   ```python
   delta = max(0.12, min(0.20, delta_formula))
   ```

2. **Window Size and Layout**:  
   You can modify the window size, layout, and styling by adjusting the `geometry()` and `grid()` settings. For example, to change the window size, update:
   ```python
   root.geometry("800x600")
   ```

3. **Additional Calculations**:  
   You can enhance the formula or add additional input fields for more complex calculations.

## Error Handling

The application includes basic error handling for user input. If the user enters invalid data (e.g., non-numeric values), an error message is displayed in the result label:
```python
result_label.config(text="Invalid input, please enter numeric values")
```

This ensures the program doesn't crash and informs the user of incorrect input.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.

---

This application is a simple and intuitive tool for calculating delta based on market volatility and price action. Feel free to modify and expand the code to fit your specific use case. If you encounter any issues or have suggestions, feel free to submit a pull request or open an issue.
