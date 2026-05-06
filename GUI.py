#TIP CALCULATOR #Able to calculate tip from total bill #Calculates and adds up tip and total bill #Allows user to select tip percentage by typing in a number # Have a widget to divide the bill among a number of people import tkinter as tk from unicodedata import decimal #Calculate tip and total function def calculate(): bill = float(entry.get()) #Get the total bill from the entry field tip_percent = slider.get() #Get the tip percentage from the slider tip = bill * (tip_percent / 100) #Calculate the tip amount total = bill + tip #Calculate the total amount (bill + tip) result.config(text=f"Tip: ${tip:.2f}\nTotal: ${total:.2f}") #Update the result label with the calculated tip and total #Create the main application window root = tk.Tk() root.title("Tip Calculator") root.geometry("400x300") #Create and place the entry field for total bill entry = tk.Entry(root) entry.pack(pady=10) #Create and place the label for total bill bill_label = tk.Label(root, text="Enter Total Bill:") #Create a label with the text "Enter Total Bill:" and place it in the window with some padding. bill_label.pack(pady=10) #Create and place the slider for selecting tip percentage slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, label="Tip Percentage") #Create a horizontal slider with a range from 0 to 100 and a label "Tip Percentage" slider.pack(pady=10) #Create and place the entry field for number of people to split the bill split_entry = tk.Entry(root) split_entry.pack(pady=10) #Create and place the label for the split bill split_label = tk.Label(root, text="") #Create a label to display the split bill, initially empty, and place it in the window with some padding. split_label.pack(pady=10) #Function to calculate the split bill def calculate_split(): total = float(result.cget("text").split("\n")[1].split("$")[1]) #Get the total amount from the result label people = int(split_entry.get()) #Get the number of people to split the bill from the entry field if people > 0: #Check if the number of people is greater than 0 to avoid division by zero split_amount = total / people #Calculate the amount each person has to pay split_label.config(text=f"Each person pays: ${split_amount:.2f}") #Update the split label with the calculated amount each person has to pay else: split_label.config(text="Number of people must be greater than 0") #Display an error message if the number of people is not valid #Create and place the button to calculate the split bill split_button = tk.Button(root, text="Split Bill", command=calculate_split) #Create a button with the text "Split Bill" that calls the calculate_split function when clicked, and place it in the window with some padding. split_button.pack(pady=10) #Create and place the calculate button button = tk.Button(root, text="Calculate", command=calculate) button.pack(pady=10) #Create a button with the text "Calculate" that calls the calculate function when clicked, and place it in the window with some padding. #Create and place the label to display the result result = tk.Label(root, text="") #Create a label to display the result of the calculation, initially empty, and place it in the window with some padding. result.pack(pady=10) #Start the main event loop root.mainloop()#TIP CALCULATOR
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

    result.config(text=f"Tip: ${tip:.2f}\nTotal: ${total:.2f}")

    try:
        people = int(split_entry.get())
        if people > 0:
            split_amount = total / people
            split_result.config(text=f"Each person pays: ${split_amount:.2f}")
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

