# This GUI program is built using tkinter and python users are 
# asked to select a person then a company and verify is they match 
# they only match if the person works for that company 

import tkinter as tk 

# Creating a set of list and dictionaries to hold the employees and their employers
company = {"JSN Bank":"Kim Anderson", "Kingston Industrial":"Andrew Peterson", 
            "Amazon Jamaica":"Stephen Jones", "Ministry of Health":"Roy Simpson", 
            "Whole Foods":"Keisha Tolcut", "Daily Radio":"John Anderson", 
            "ABN Enterprises":"Yvonne Bryan", "PLB Planet":"Rick Grant", 
            "JM Tech":"Dave Peters", "Sams Restaurant":"Kelly Zan"}


# By using set comprehensions to populate the employee 
# and company sets we only have to update the company dictionary 
employee_names = {emp for emp in company.values()}
# employee ={"John Anderson","Kim Anderson", "Rick Grant", "Dave Peters", "Andrew Peterson", 
#             "Yvonne Bryan", "Kelly Zan", "Stephen Jones", "Roy Simpson", "Keisha Tolcut"}

company_names = {comp for comp in company.keys()}
# employer ={"PLB Planet", "JM Tech", "JSN Bank", "Sams Restaurant", "Kingston Industrial", 
#             "ABN Enterprises", "Amazon Jamaica", "Daily Radio", "Ministry of Health", 
#             "Whole Foods"}

# A sub dictionary to store the selected items of each listbox 
sub_dict={}

def check_match(even=None): 
    boxItem1 = workplace_listbox.get(workplace_listbox.curselection())
    boxItem2 = person_listbox.get(person_listbox.curselection())

    # Populating the sub dictionary with the name of a workplace and an employee
    sub_dict[boxItem1]=boxItem2
    # Checks if the sub dictionary is a subset of the company dictionary
    result = sub_dict.items() <= company.items()
    
    # Checks if result is true and prints the appropriate response 
    if result == True: 
        answer_entry["text"] = "Correct"
    else: 
        answer_entry["text"] = "Incorrect"
    # clears the sub dictionary of any previous employee information
    sub_dict.clear()

window = tk.Tk()

# defining the main window and its elements 
window.title("Company Match")
window.minsize(220, 350)
window.resizable(0, 0)

# Creating the frame that'll hold the listboxs 
list_frame = tk.Frame(master=window)
list_frame.grid()

# Creating the label and listbox for the employees 
person_label = tk.Label(master=list_frame, text="Person")
person_label.grid(row=1, column=3, padx=20, pady=10)
person_listbox = tk.Listbox(master=list_frame, relief=tk.SUNKEN, borderwidth=5, exportselection=0)
person_listbox.grid(row=2, column=3, padx=20, pady=10)

# Creating the label and listbox for the employers 
workplace_label = tk.Label(master=list_frame, text="Workplace")
workplace_label.grid(row=1, column=4, padx=20, pady=10)
workplace_listbox = tk.Listbox(master=list_frame, relief=tk.SUNKEN, borderwidth=5, exportselection=0)
workplace_listbox.grid(row=2, column=4, padx=20, pady=10)

# Populate both listboxes with data 
for items in employee_names: 
    person_listbox.insert(tk.END, items)

for items in company_names:
    workplace_listbox.insert(tk.END, items )

# Defining the frame that'll hold the buttons and answer label
button_frame = tk.Frame(master=window)
button_frame.grid()

# Defining the button that'll check if the data selected in the listbox match
check_btn = tk.Button(master=button_frame, text="Check Match", command=check_match)
check_btn.grid(row=3, column=2, pady=10, sticky="nsew")
check_btn.bind("<Button-1>", check_match)

# Defining the entry and answer entry labels 
entry_lbl = tk.Label(master=button_frame, text="Answer:")
entry_lbl.grid(row=4, column=1, stick="e")

answer_entry = tk.Label(master=button_frame, width=25,)
answer_entry.grid(row=4, column=2)

window.mainloop()