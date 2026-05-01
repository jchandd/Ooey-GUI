#TIP CALCULATOR
#Able to calculate tip from total bill
#Calculates and adds up tip and total bill
#Allows user to select tip percentage by typing in a number


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
#Create and place the entry field for the total bill
entry = tk.Entry(root)
entry.pack(pady=10)

#Create somewhere to type in your tip percentage (no slider)
tip_entry = tk.Entry(root)
tip_entry.pack(pady=10)

#replace the slider with the entry field for tip percentage
#Create and place the calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack(pady=10)

#Create and place the label to display the result




