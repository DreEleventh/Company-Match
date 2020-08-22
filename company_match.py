# This GUI program is built using tkinter and python users are 
# asked to select a person then a company and varify is they match 
# they only match if the person works for that company 

import tkinter as tk 

# Creating a set of list and dictionaries to hold the employees and their employors
company = {"JSN Bank":"Kim Anderson", "Kingston Industrial":"Andrew Peterson", 
            "Amazon Jamaica":"Stephen Jones", "Ministry of Health":"Roy Simpson", 
            "Whole Foods":"Keisha Tolcut", "Daily Radio":"John Anderson", 
            "ABN Enterprises":"Yvonne Bryan", "PLB Planet":"Rick Grant"}

employee =["John Anderson","Kim Anderson", "Rick Grant", "Andrew Peterson", 
            "Yvonne Bryan", "Stephen Jones", "Roy Simpson", "Keisha Tolcut"]

employer =["PLB Planet", "JSN Bank", "Kingston Industrial", "ABN Enterprises", 
            "Amazon Jamaica", "Daily Radio", "Ministry of Health", "Whole Foods"]

# A sub dictionary to store the selected items of each listbox 
sub_dict={}

window = tk.Tk()

# defining the main window and its elements 
window.title("Company Match")
window.minsize(220, 350)
window.resizable(0, 0)

# Creating the frame that'll hold the listboxs 
list_frame = tk.Frame(master=window)
list_frame.grid()