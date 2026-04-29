#TIP CALCULATOR
#Able to calculate tip from total bill
#Calculates and adds of tip and total bill

import tkinter as tk

#Calculate tip and total function
def calculate():
    bill = float(entry.get()) #Get the total bill from the entry field

    tip_percent = slider.get() #Get the tip percentage from the slider