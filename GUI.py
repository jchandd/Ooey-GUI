#TIP CALCULATOR
#Able to calculate tip from total bill
#Calculates and adds up tip and total bill
#Allows user to select tip percentage by typing in a number
#Have 6 widgets

import tkinter as tk

#Calculate tip and total function
def calculate():
    bill = float(entry.get()) #Get the total bill from the entry field

    tip_percent = slider.get() #Get the tip percentage from the slider

    tip = bill * (tip_percent / 100) #Calculate the tip amount

    total = bill + tip #Calculate the total amount (bill + tip)

    result.config(text=f"Tip: ${tip:.2f}\nTotal: ${total:.2f}") #Update the result label to show the calculated tip and total, formatted to 2 decimal places.

    try:
        people = int(split_entry.get()) 
        if people > 0:
            split_amount = total / people
            split_result.config(text=f"Each person pays: ${split_amount:.2f}") #Calculate the amount each person pays by dividing the total by the number of people, and update the split_result label to show this amount, formatted to 2 decimal places.
        else:
            split_result.config(text="Number must be > 0")

    except ValueError:
        result.config(text="Invalid input")


#Create the main application window
root = tk.Tk()
root.title("Tip Calculator")
root.geometry("400x300")

#Create and place the entry field for total bill
entry = tk.Entry(root)
entry.pack(pady=10)

def set_tip(value):
    slider.set(value)

menubutton = tk.Menubutton(root, text="Quick Tip %", relief="raised")
menu = tk.Menu(menubutton, tearoff=0)
menubutton.config(menu=menu)

menu.add_command(label="10%", command=lambda: set_tip(10))
menu.add_command(label="15%", command=lambda: set_tip(15))
menu.add_command(label="18%", command=lambda: set_tip(18))
menu.add_command(label="20%", command=lambda: set_tip(20))
menu.add_command(label="25%", command=lambda: set_tip(25))

menubutton.pack(pady=10)
# ----------------------------------------------------------

#Create and place the slider for selecting tip percentage
slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, label="Tip Percentage")
slider.pack(pady=10)

#Create and place the calculate button
button = tk.Button(root, text="Calculate", command=calculate)
button.pack(pady=10)

#Create something to split bill between people
split_label = tk.Label(root, text="Split between how many people?")
split_label.pack(pady=10) #Create a label asking how many people to split the bill between, and place it in the window with some padding.
split_entry = tk.Entry(root)
split_entry.pack(pady=10) #Create an entry field for the user to input the number of people to split the bill between, and place it in the window with some padding.

#Create and place the label to display the result of splitting the bill
split_result = tk.Label(root, text="")
split_result.pack(pady=10) #Create a label to display the result of splitting the bill, initially empty, and place it in the window with some padding.

#Create and place the label to display the result
result = tk.Label(root, text="")
result.pack(pady=10)
result = tk.Label(root, text="") #Create a label to display the result of the calculation, initially empty, and place it in the window with some padding.
result.pack(pady=10) 

#Start the main event loop
root.mainloop()

