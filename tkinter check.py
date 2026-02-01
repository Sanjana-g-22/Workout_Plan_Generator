import tkinter as tk
from tkinter import messagebox
import csv

#creating a nested list containing username and password of members
l=[]
f=open("login_det.csv",'r')
x=csv.reader(f)
for i in x:
    l.append(i)
f.close()

def check_login():
    user = entry_username.get()
    p = entry_password.get()
    check=0
    for q in range(len(l)):
        if user == l[q][0] and str(p) ==l[q][1]:
            messagebox.showinfo(title='login detail',message='you have loged in successfully  WELCOME '+user+' ! ')
            check=1
            root1.destroy()
    if check==0:
        messagebox.showerror("Login Failed", "Incorrect username or password")
        print("please enter the correct user name or password , if new (not a member) Register and try signing in ")
        root1.destroy()
        call()
    else:
        pass

def check_login2():
    user = entry_username.get()
    p = entry_password.get()
    check=0
    for q in range(len(l)):
        if user == l[q][0] and str(p) ==l[q][1]:
            messagebox.showinfo(title='login detail',message='you have loged in successfull')
            print('WELCOME '+user+' ! ')
            check=1
            root2.destroy()
entry_username=''
entry_password= ''
root2=None

def call():
    global root2
    root2 = tk.Tk()
    root2.title("Login again")
    window_width = 310
    window_height = 200
    screen_width = root2.winfo_screenwidth()
    screen_height = root2.winfo_screenheight()
    root2.geometry(f"{window_width}x{window_height}")
    root2.resizable(False,False)
    label1=tk.Label(root2,text="please LOGIN here ")
    label1.grid(row=0, column=2, padx=10,pady=10)
    label_username = tk.Label(root2, text="Username:")
    label_username.grid(row=1, column=1, padx=20, pady=5)
    global entry_username
    entry_username = tk.Entry(root2)
    entry_username.grid(row=1, column=2, padx=10, pady=5)
    label_password = tk.Label(root2, text="Password:")
    label_password.grid(row=2, column=1, padx=20, pady=5)
    global entry_password 
    entry_password = tk.Entry(root2, show="*")
    entry_password.grid(row=2, column=2, padx=10, pady=5)
    login_button = tk.Button(root2, text="Login", command=check_login2)
    login_button.grid(row=4, column=2,columnspan=2, padx=25, pady=20)
    root2.mainloop()

root1 = tk.Tk()
root1.title("Login")
window_width = 310
window_height = 200
screen_width = root1.winfo_screenwidth()
screen_height = root1.winfo_screenheight()
root1.geometry(f"{window_width}x{window_height}")
root1.resizable(False,False)
label1=tk.Label(root1,text="please LOGIN here ")
label1.grid(row=0, column=2, padx=10,pady=10)
label_username = tk.Label(root1, text="Username:")
label_username.grid(row=1, column=1, padx=20, pady=5)
entry_username = tk.Entry(root1)
entry_username.grid(row=1, column=2, padx=10, pady=5)  
label_password = tk.Label(root1, text="Password:")
label_password.grid(row=2, column=1, padx=20, pady=5) 
entry_password = tk.Entry(root1, show="*")  
entry_password.grid(row=2, column=2, padx=10, pady=5)
login_button = tk.Button(root1, text="Login", command=check_login)
login_button.grid(row=4, column=2,columnspan=2, padx=25, pady=20)

root1.mainloop()
