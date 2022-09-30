import datetime
import time
import os
import dencrypt
from random import randint
def recaptcha():
    d=chr(randint(97,122))+chr(randint(65,90))+chr(randint(48,57))+chr(randint(48,57))+chr(randint(97,122))+chr(randint(65,90))
    #"aZ23zA"
    return d
user=input("Enter USER/Sender: ")
chat2=input("Enter Reciever: ")
secode=recaptcha()
print("Your Security Code is:",secode)
timenow=datetime.datetime.now()
##open("","w").write(str(timenow)[:19:])
with open("user.txt","w") as sender:
    sender.write("")
with open("reciever.txt","w") as recside:
    recside.write("")
with open("thirdparty.txt","w") as thirdparty:
    thirdparty.write("")
with open("backup.txt","w") as backup:
    backup.write("")
userside,recside,thirdparty,backup=open("user.txt","a"),open("reciever.txt","a"),open("thirdparty.txt","a"),open("backup.txt","a")
#pass for jo if wrong send to encrypted
###os.startfile("ksp.txt")             IMP
##if message only contains """bye""" break loop and note end time
##ram shyam
##ram,shyam-:po.txt
##jo:lp.txt(encrypted of po)
messagecheck=""
i=0
print("Chat starting")
while "bye" not in messagecheck:
    if i%2==0:
        message=input("{}: ".format(user))
        
    else:
        message=input("{}: ".format(chat2))
    time.sleep(1)
    messagecheck=message.lower()
    i+=1
print("")
print("✨"*10)
print("")
print("MENU")
menuchoose="yes"
while menuchoose=="yes":
    option=input("1. View chat\n2. Delete chat\n3. Continue chat\n4. Update backup\n5. View backup\n(Enter only number): ")
    if option=="1":
        checker=input("Enter security code: ")
        if checker==secode:
            name_check=input("
    elif option=="2":
        p
    elif option=="3":
        p
