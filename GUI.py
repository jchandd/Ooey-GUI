#TIP CALCULATOR
#Able to calculate tip from total bill
#Calculates and adds of tip and total bill

import tkinter as tk

#Calculate tip and total function
def calculate():
    bill = float(entry.get()) #Get the total bill from the entry field

    tip_percent = slider.get() #Get the tip percentage from the slider

    tip = bill * (tip_percent / 100) #Calculate the tip amount

    total = bill + tip #Calculate the total amount (bill + tip)

    result.config(text=f"Tip: ${tip:.2f}\nTotal: ${total:.2f}") #Update the result label with the calculated tip and total

#Create the main application window
root = tk.Tk()
root.title("Tip Calculator")

#Create and place the widgets
label = tk.Label(root, text="Enter the total bill:")

entry = tk.Entry(root)
entry.pack(pady=5)
