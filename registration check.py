import tkinter as tk
from tkinter import messagebox
import csv


def register():
    username = entry_username.get()
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()
    
    if not username or not password or not confirm_password:
        messagebox.showerror("Error", "Please fill in all fields")
    elif password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match")
    else:
        f=open("login_det.csv",'a',newline='')
        fw=csv.writer(f)
        fw.writerow([username,str(password)])
        f.close()
        messagebox.showinfo("Success", "Registration successful")
        clear_fields()

def clear_fields():
    root3.destroy()

# Create the main window
root3 = tk.Tk()
root3.title("Registration Page")
x=650
y=300
root3.geometry(f"{x}x{y}")
root3.resizable(False,False)


# Create labels and entry widgets using grid
label_left = tk.Label(root3, text="Resgister with your details here",font="arial 18")
label_left.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
label_username = tk.Label(root3, text="Username:",font="algerian")
label_username.grid(row=1, column=0, padx=5, pady=5)
entry_username = tk.Entry(root3,width=20,font="arial 14")
entry_username.grid(row=1, column=1,padx=5,pady=5)

label_password = tk.Label(root3, text="Password:",font="algerian")
label_password.grid(row=2, column=0,padx=5,pady=5)
entry_password = tk.Entry(root3, show="*",width=20,font="arial 14")  
entry_password.grid(row=2, column=1,padx=5,pady=5)

label_confirm_password = tk.Label(root3, text="Confirm Password:",font="algerian")
label_confirm_password.grid(row=3, column=0,padx=10,pady=5)
entry_confirm_password = tk.Entry(root3, show="*",width=20,font="arial 14")  
entry_confirm_password.grid(row=3, column=1,padx=5,pady=5)

# Create a Register button
register_button = tk.Button(root3, text="Register",font="algerian", command=register)
register_button.grid(row=6, column=1, columnspan=3,pady=20)

# Start the Tkinter main loop
root3.mainloop()
