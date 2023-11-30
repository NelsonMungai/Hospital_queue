from copy import deepcopy
import tkinter as tk
from tkinter import messagebox
from hospitalPriorityQueue import HospitalQueue

# dict mapping keys to the locator of the patient
patient_locator={

}

def add_patient():
    severity = int(severity_entry.get())
    age = int(age_entry.get())
    name = name_entry.get()

    locator=hospital_queue.add_patient(severity, age, name)
    print(locator)
    patient_locator[(severity,age)]=locator
    print(patient_locator)
    update_display()

def update_display():
    display_text.config(state=tk.NORMAL)
    display_text.delete("1.0", tk.END)

    copy_queue = deepcopy(hospital_queue)
    while not copy_queue.is_empty():
        patient = copy_queue.remove_min()
        display_text.insert(tk.END, f"Next Patient: {patient[1]} (Severity: {patient[0][0]}, Age: {patient[0][1]})\n")

    display_text.config(state=tk.DISABLED)
def display_queue():
    print(display_text.get())

def remove_next_patient():
    try:
        patient = hospital_queue.remove_min()
        messagebox.showinfo("Removed Patient", f"Removed Patient: {patient[1]}")
        update_display()
    except Exception as e:
        messagebox.showwarning("Empty Queue", "The queue is empty.")

def find_patient():
    try:
        age_to_find = int(find_age_entry.get())
        severity_to_find = int(find_severity_entry.get())
        copy_queue =deepcopy(hospital_queue)
        while not copy_queue.is_empty():
            patient = copy_queue.remove_min()
            if patient[0][0] == severity_to_find and patient[0][1] == age_to_find:
                messagebox.showinfo("Patient Found", f"Patient found: {patient[1]}")
                return
        messagebox.showinfo("Patient Not Found", "No patient found with the given severity and age.")
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter valid integer values for severity and age.")

def update_patient():
    try:
        age=int(find_age_entry.get())
        severity=int(find_severity_entry.get())
        newAge=int(new_age.get())
        newSeverity=int(new_severity.get())
        for key in patient_locator.keys():
            if key==(severity,age):
                hospital_queue.update_patient(patient_locator[key],newSeverity,newAge)
        update_display()                
    except ValueError:
        messagebox.showwarning("Invalid Input","Please enter a valid integer values for severity and age")
    update_display()

def delete_patient():
    try:
        age=int(find_age_entry.get())
        severity=int(find_severity_entry.get())
        for key in patient_locator.keys():
            if key==(severity,age):
                hospital_queue.remove_patient(patient_locator[key])
        update_display()
    except ValueError:
        messagebox.showwarning("Invalid Input","Please enter a valid interger values for severity and age")


root = tk.Tk()
root.title("Hospital Priority Queue")
root.geometry("800x800")

# Input fields
severity_label = tk.Label(root, text="Severity Level")
severity_label.pack(anchor=tk.W, padx=10)
severity_entry = tk.Entry(root)
severity_entry.pack(anchor=tk.W, padx=10)

age_label = tk.Label(root, text="Age")
age_label.pack(anchor=tk.W, padx=10)
age_entry = tk.Entry(root)
age_entry.pack(anchor=tk.W, padx=10)

name_label = tk.Label(root, text="Name")
name_label.pack(anchor=tk.W, padx=10)
name_entry = tk.Entry(root)
name_entry.pack(anchor=tk.W, padx=10)

# Buttons
add_patient_button = tk.Button(root, text="Add Patient", command=add_patient)
add_patient_button.pack(anchor=tk.W, padx=10)

display_queue_button = tk.Button(root, text="Display Queue", command=display_queue)
display_queue_button.pack(anchor=tk.W, padx=10)

remove_next_button = tk.Button(root, text="Remove Next Patient", command=remove_next_patient)
remove_next_button.pack(anchor=tk.W, padx=10)

# Update patient
update_labele=tk.Label(root,text="Update the Patient Details or Delete Specific patient",font=("Arial",16,"bold"))
update_labele.pack(anchor=tk.CENTER,padx=0)
find_severity_label = tk.Label(root, text="Find Patient - Severity")
find_severity_label.pack(anchor=tk.CENTER, padx=10)
find_severity_entry = tk.Entry(root)
find_severity_entry.pack(anchor=tk.CENTER, padx=10)


find_age_label = tk.Label(root, text="Find Patient - Age")
find_age_label.pack(anchor=tk.CENTER, padx=10)
find_age_entry = tk.Entry(root)
find_age_entry.pack(anchor=tk.CENTER, padx=10)

# UPDATE SUB-TITLE
update_sub=tk.Label(root,text="Update Patient Severity",font=("Arial",14,"bold"))
update_sub.pack(anchor=tk.W,padx=10,pady=10)

new_age_label=tk.Label(root,text="New Age")
new_age_label.pack(anchor=tk.W, padx=10)
new_age=tk.Entry(root)
new_age.pack(anchor=tk.W, padx=10)

new_severity_label=tk.Label(root,text="New Severity")
new_severity_label.pack(anchor=tk.W, padx=10)
new_severity=tk.Entry(root)
new_severity.pack(anchor=tk.W, padx=10)





find_patient_button = tk.Button(root, text="Update Patient", command=update_patient)
find_patient_button.pack(anchor=tk.W, padx=10)

delete_patient_btn=tk.Button(root,text="Delete Patient",fg="red",command=delete_patient)
delete_patient_btn.pack(anchor=tk.E,padx=10)
# Display text
display_text = tk.Text(root, height=10, width=60, state=tk.DISABLED)
display_text.pack(anchor=tk.W, padx=10, pady=10)

hospital_queue = HospitalQueue()

root.mainloop()
