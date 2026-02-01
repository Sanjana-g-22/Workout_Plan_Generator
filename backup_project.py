import tkinter as tk
from tkinter import messagebox
import csv
import workpackage.check_module
import mysql.connector as mys
con=mys.connect(host="localhost",user="root",passwd="sql123*456",database="workout")
cur=con.cursor()    
q1="select * from intense"

import random

#creating a nested list containing username and password of members
l=[]
f=open("login_det.csv",'r')
x=csv.reader(f)
for i in x:
    l.append(i)
f.close()
check=0

def check_login():
    user = entry_username.get()
    p = entry_password.get()
    for q in range(len(l)):
        if user == l[q][0] and str(p) ==l[q][1]:
            messagebox.showinfo(title='login detail',message='you have loged in successfully  WELCOME '+user+' ! ')
            global check
            check=1
            root1.destroy()
            return check
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
    for q in range(len(l)):
        if user == l[q][0] and str(p) ==l[q][1]:
            messagebox.showinfo(title='login detail',message='you have loged in successfull')
            print('WELCOME '+user+' ! ')
            global check
            check=2
            root2.destroy()
            return check
            
entry_username=''
entry_password= ''
root2=None
root3=None

def call():
    global root2
    root2 = tk.Tk()
    root2.attributes('-topmost',True)
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
        global check
        check=3
        root3.destroy()
    return check

def on_select(event):
    selected_value = selected_item.get()
    print("Selected:", selected_value)
a=None
def fun():
    global a
    a=str(menu.get())
    window.destroy()




print("*******************************************************************************************************************")
print("WORKOUT PLAN GENERATOR")
print("*******************************************************************************************************************")
print()
print("Please fill the option below to proeed")
print()

con1=input("Are you a member?(y/n) : ")
while con1!='y' and con1!='n':
    print("Please fill the option below to proeed")
    print()
    con1=input("Are you a member?(y/n) : ")

if con1=='y':
    root1 = tk.Tk()
    root1.attributes('-topmost',True)
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
    


elif con1 =='n':
    
    root3 = tk.Tk()
    root3.title("Registration Page")
    x=650
    y=300
    root3.geometry(f"{x}x{y}")
    root3.resizable(False,False)
    root3.attributes('-topmost',True)
    
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

    register_button = tk.Button(root3, text="Register",font="algerian", command=register)
    register_button.grid(row=6, column=1, columnspan=3,pady=20)

    root3.mainloop()
    
print (check)
if check in [1,2,3]:
    window=tk.Tk()
    window.attributes('-topmost',True)

    label4=tk.Label(window,text="Select your level of plan you want to generate ",font="arial 14")
    label4.pack(padx=20, pady=10, ipadx=5, ipady=5)
    
    items = ["Beginner 1", "Intermediate 2", "Intense 3"]
    menu= tk.StringVar()
    menu.set("select level")

    drop= tk.OptionMenu(window,menu,*items)
    drop.pack()
    
    submit_button=tk.Button(window,text="ok",command=fun)
    submit_button.pack()
    
              
    window.mainloop()


if a=="Intense 3":
        print()
        print("Intense plan")
        print()
        
        print("which area do you want to focus on")
        print("1> Upper body")
        print("2> lower body")
        print("3> Full body")
        c2=int(input("choose any number to select the part you want to work on :  "))
        if c2==1:
            print("Upper body")
            q1="select sno,name from intense where focus_area=1"
            cur.execute(q1)
            dat=cur.fetchall()
            
        elif c2==2:
            print("Lower body")
            q2="select sno,name from intense where focus_area=2"
            cur.execute(q2)
            dat=cur.fetchall()
            
        else:
            print("Full body")
            q3="select sno,name from intense where focus_area=3"
            cur.execute(q3)
            dat=cur.fetchall()

elif a=="Intermediate 2":
        print()
        print("Moderate plan")
        #criteria 2
        print()
        print("which area do you want to focus on")
        print()
        
        print("1> Upper body")
        print("2> lower body")
        print("3> Full body")
        c2=int(input("choose anyone area to want to work on :  "))
        if c2==1:
            print("Upper body")
            q1="select sno,name from moderate where focus_area=1"
            cur.execute(q1)
            dat=cur.fetchall()
        elif c2==2:
            print("Lower body")
            q2="select sno,name from moderate where focus_area=2"
            cur.execute(q2)
            dat=cur.fetchall()
        else:
            print("Full body")
            q3="select sno,name from moderate where focus_area=3"
            cur.execute(q3)
            dat=cur.fetchall()
elif a=="Beginner 1":
    print()
    print("BEGINNER PLAN")
    q4="select * from beginner"
    cur.execute(q4)
    dat=cur.fetchall
    print()

d=int(input("Enter no of days:"))
print ("we have 3 different timing options , please select any one from it")
print("1] 15 minutes")
print("2] 30 minutes")
print("3] 60 minutes")
print(" please enter the corresponding numer of your required timing below")
t=int(input("Enter the number here : "))
if t==1:
    ex=5
elif t==2:
    ex=8
elif t==3:
    ex=12
else:
    print("your input in invalid")
di={}
nos=[]
for v in dat:
    nos.append(v[0])
    di[v[0]]=v[1]

for day in range(1,d+1):
    print("Day",day,"*************************************************************************************************************")
    for e in range(ex):
        n=random.randrange(0,len(nos)+1)
        y=nos[n]
        print(di[y])

print("not satisfied?")
o=input("enter y to regenerate plan again: ")
if o == y:
    for day in range(1,d+1):
        print("Day",day,"*************************************************************************************************************")
    for e in range(ex):
        n=random.randrange(0,len(nos)+1)
        y=nos[n]
        print(di[y])

else:
    print("thankyou for using our program")
    
        
  
    



