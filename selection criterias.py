#importing user define python pakage 
import workpackage.check_module
#connecting with sql
import mysql.connector as mys
con=mys.connect(host="localhost",user="root",passwd="sql123*456",database="workout")
cur=con.cursor()    
q1="select * from intense"
import random
# main criteria 1 (type of plan)
print("we have 3 different options for you")
print("1] Intense")
print("2] Moderate")
print("3] Beginner")


#using function from user defined module
c1=workpackage.check_module.check_criteria_1()
print(c1)


if c1==1:
    print()
    print("Intense plan")
    print()
    #criteria 2
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

elif c1==2:
    print()
    print("Moderate plan")
    #criteria 2
    print()
    print("which area do you want to focus on")
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
else:
    print()
    print("BEGINNER PLAN")
    print()
    
d=workpackage.check_module.sub_criteria()    
print(d)
#criteria 3- the time  (t)  
print ("we have 3 different timing options , please select any one from it")
print("1] 15 minutes")
print("2] 30 minutes")
print("3] 60 minutes")
print(" please enter the corresponding numer of your required timing below")
t=int(input("Enter the number here : "))
if t==1:
    ex=5
elif t==2:
    ex=10
elif t==3:
    ex=15
else:
    print("your input in invalid")
    
def output_loop():
    for i in range(1,d+1):
        print("DAY",i)
        for j in range(1,ex+1):
            n=random.randrange(1,15)
            for v in dat:
                if v[0]==n:
                    print(v[1])

output_loop()

print("not satisfied ?")
k=input("type yes (all small) to regenerate the plan -TYPE HERE :  ")

if k=='yes':
    output_loop()    
            
    
        
        
    
    
