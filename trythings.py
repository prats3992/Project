import datetime
import pyotp
from tkinter import *
from tkinter.ttk import *
'''print(datetime.datetime.now())
print(type(datetime.datetime.now()))
print(str(datetime.datetime.now())[:19:])
print(type(str(datetime.datetime.now())[:19:]))
with open("keys.txt","r",encoding="utf-8") as deleter:
    global rem
    rem=deleter.readlines()
with open("keys.txt","w",encoding="utf-8") as deleter:
    deleter.write(rem[0][:-1:])
open("data.csv","a")'''
'''ma=Tk()
ma.geometry("200x200")
def openNewWindow():
    newWindow=Toplevel(ma)
    newWindow.title("New Window")
    newWindow.geometry("200x200")
    Label(newWindow,text ="This is a new window").pack()
label=Label(ma,text ="This is the main window")
label.pack(pady = 10)
btn=Button(ma,text ="Click to open a new window",command = openNewWindow)
btn.pack(pady = 10)
mainloop()'''
'''
with open("data.csv") as f:
    global d
    d=f.readlines()
for i in range(len(d)):
    if i==len(d)-1:
        pp=d[i]
        z=""
        for j in range(len(pp)):
            if j==pp.index("\n")-1:
                z+=",5"
            else:
                z+=pp[j]
        d.pop()
        d.append(z)
    else:
        pass
print(d)
p=open("data.csv","w")
p.writelines(d)
p.close()'''
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="MrRobot04",database="project")
mycursor=mydb.cursor()
mycursor.execute("SELECT * FROM emp_dept order by id desc limit 1;")
for k in mycursor:
    i=str(k).replace(",","")
    i=str(i).replace("(","")
    i=str(i).replace(")","")
    i=str(i).replace("'","")
    print(i.split())