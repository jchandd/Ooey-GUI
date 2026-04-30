# TIP CALCULATOR
# Able to calculate tip from total bill
# Calculates and adds of tip and total bill

import tkinter as tk


# Calculate tip and total function
def calculate():
    bill = float(entry.get())  # Get the total bill from the entry field

    tip_percent = slider.get()  # Get the tip percentage from the slider

    tip_amount = bill * (tip_percent / 100)  # Calculate the tip amount

    total_amount = bill + tip_amount  # Calculate the total amount
    tip_label.config(
        text=f"Tip Amount: ${tip_amount:.2f}"
    )  # Update the tip amount label
    total_label.config(
        text=f"Total Amount: ${total_amount:.2f}"
    )  # Update the total amount label


# Create the main application window
root = tk.Tk()
root.title("Tip Calculator")
root.geometry("300x200")

# Create and place the widgets
label = tk.Label(root, text="Enter Total Bill:")
label.pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)
