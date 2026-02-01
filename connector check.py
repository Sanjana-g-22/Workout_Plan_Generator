'''import mysql.connector as mys
con=mys.connect(host="localhost",user="root",passwd="sql123*456",database="workout")
if con.is_connected():
    print("yes")
else:
    print("no")
    
import workpackage.check_module

workpackage.check_module.check_criteria_1()
print '''

import mysql.connector as mys
con=mys.connect(host="localhost",user="root",passwd="sql123*456",database="workout")
cur=con.cursor()
cur.execute("select * from intense")
d=cur.fetchall()
print(d)
