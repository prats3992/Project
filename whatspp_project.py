# '''include input name and check if robot by recaptcha to let access file for BACKUP(update and clear) DONE!!
# if trying tkinter windows more than ONCE screens get mixed up,somtimes at first time too  ASKED!! SOLVED ig!!
# continue access using Sequest & do some "i accept things" then input some personal info to be used as confirmation for forgot secode if possible DONE!! & DONE!!
# in CSV order to be [a,q,send,rec] and never del DONE!!
# BIG LOOP to b changed something wrong?????? XX FIXED!!!
# solve menu problems DONE!!
# csv read lines miss change window methods DONE!!
# something to force exit chat DONE!!
# remove all lines except no.1 in keys.txt DONE!!
# Can set a rating system window at end to inc lines DONE!!
# ADD APPROPIATE COMMENTS'''
import array
from random import *
import datetime
import time
import os
import csv
from tkinter import *
from tkinter.ttk import *
import dencrypt
import re
DIGITS = [str(i) for i in range(10)]
LOCASE = [chr(i) for i in range(ord('a'), ord('z')+1)]
UPCASE = [chr(i) for i in range(ord('A'), ord('Z')+1)]
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?',
           '.', '/', '|', '~', '>', '*', '(', ')', '<']


def enterxp():
    if im1 == 1:
        return 1
    elif im2 == 1:
        return 2
    elif im3 == 1:
        return 3
    elif im4 == 1:
        return 4
    elif im5 == 1:
        return 5
    else:
        return None


def Click():
    global result
    result = input_result.get()


def Over(event):
    time.sleep(5)
    root.destroy()


def openNewWindow():
    global randomiser, result, n1, n2, success_check, sentence
    new = Toplevel(root)
    Click()
    if (randomiser == 0 and result == str(n1+n2)) or (randomiser == 1 and result == str(n1-n2)):
        new.title("Access Granted")
        new.geometry("200x200+{}+{}".format(center_x//2, center_y//2))
        sentence = Label(new, text="Successful", font=(
            "Arial", 30), foreground="green")
        success_check = "ok"
    else:
        new.title("Access Denied")
        new.geometry("200x200+{}+{}".format(center_x//2, center_y//2))
        sentence = Label(new, text="Try Again", font=(
            "Arial", 30), foreground="green")
        success_check = "no"
    sentence.bind("<Enter>", Over)
    sentence.pack()
# PASSWORD GENERATOR FOR SECURITY CODE


def recaptcha():
    MAX_LEN = 12
    COMBINED_LIST = DIGITS+UPCASE+LOCASE+SYMBOLS
    temp_pass = choice(DIGITS)+choice(UPCASE)+choice(LOCASE)+choice(SYMBOLS)
    for x in range(MAX_LEN-4):
        temp_pass = temp_pass+choice(COMBINED_LIST)
        temp_pass_list = array.array('u', temp_pass)
        shuffle(temp_pass_list)
    password = ""
    for x in temp_pass_list:
        password += x
    return password


print("\n\nTerms of the Service:\nYour chat data will be completely removed from our files upon termination of the services")
for yip in range(5):
    Allowr = input("Do you agree to the Terms of the services(YES/NO): ")
    if Allowr.lower() == "yes":
        # INPUT USER,RECIEVER,SECURITY Q/A
        user = input("Enter USER/Sender: ")
        chat2 = input("Enter Reciever: ")
        q1, q2, q3, q4, q5 = "Name of your pet", "Name of your favorite city", "Your dream job", "Your favorite subject", "Your mother tongue"
        Sequest = input(
            f"For Security purposes answer any 1 of the following questions in the given format\nAnswer,Question number\n1. {q1}\n2. {q2}\n3. {q3}\n4. {q4}\n5. {q5}\n: ")
        Sequest = Sequest.split(",")
        secode = recaptcha()
# INCLUDE APPROPOS DATA INTO LIST FOR ENTERING INTO .csv
        Sequest += [f"{user}", f"{chat2}", f"{secode}"]
        file = open("data.csv", "a", newline="")
        writer = csv.writer(file)
        writer.writerow(Sequest)
        file.close()
# Change once Bifid Corrected
        encrylevel = randint(1, 2)
        print(f"Your Security Code is: {secode}")
# GET CHAT START TIME AND ENTER ON ALL RELEVENT FILES
        timenow = str(datetime.datetime.now())
        with open("user.txt", "w") as sender:
            sender.write(f"Chat starting at {(timenow)[:19:]}\n")
        with open("thirdparty.txt", "w", encoding="utf-8") as thirdparty:
            thirdparty.write("{}\n".format(dencrypt.Encrypt(
                f"Chat starting at {(timenow)[:19:]}", encrylevel, "no")))
        with open("backup.txt", "w") as backup:
            backup.write(f"Original Back Up started at {(timenow)[:19:]}\n")
        userside, thirdparty, backup = open("user.txt", "a"), open(
            "thirdparty.txt", "a", encoding="utf-8"), open("backup.txt", "a")
        messagecheck = ""
        count_up = 0
        bye_lines = []
        i = 0
        print("\nChat Starting\nNote: To force exit chat ONLY Enter-> EXIT on message input prompt")
        while count_up != 1:
            if i % 2 == 0:
                message = input("{}: ".format(user))
                if message.strip() == "EXIT":  # FORCE exit CHAT
                    count_up = 1
                else:
                    userside.write("{} : {}".format(user, message))
                    backup.write("{} : {}".format(user, message))
                    thirdparty.write("{} : {}".format(dencrypt.Encrypt(
                        user, encrylevel, "no"), dencrypt.Encrypt(message, encrylevel, "no")))
            else:
                message = input("{}: ".format(chat2))
                if message.strip() == "EXIT":  # FORCE exit CHAT
                    count_up = 1
                else:
                    userside.write("{} : {}".format(chat2, message))
                    backup.write("{} : {}".format(chat2, message))
                    thirdparty.write("{} : {}".format(dencrypt.Encrypt(
                        chat2, encrylevel, "no"), dencrypt.Encrypt(message, encrylevel, "no")))
            backup.write("\n")
            userside.write("\n")
            thirdparty.write("\n")
            time.sleep(1)  # PAUSE BEFORE NEXT INPUT
            messagecheck = message.lower()
            if "bye" in messagecheck:
                bye_lines.append(i)
# IF bye IS SENT CONSECUTIVELY BY BOTH USERS THEN EXIT CHAT
            if len(bye_lines) > 1:
                if bye_lines[-1]-bye_lines[-2] == 1:
                    count_up = 1
            i += 1
        print("\n☺ Chat Ended ☺")
        userside.close()  # now closing all files
        thirdparty.close()
        backup.close()
        print(("✨"*10)+"\n")
        print("MENU")
# ACCESS CURRENT USERS' SECURITY Q/A FOR FOLLOWING ACCESS ALLOWANCES {CSV}

        def FindQ():
            file = open("data.csv", "r", newline="")
            r = csv.reader(file)
            entre = []
            for ii in r:
                entre.append(ii[1])
            file.close()
            return int(entre[-1])

        def GiveQ(q):
            if q == 1:
                return q1
            elif q == 2:
                return q2
            elif q == 3:
                return q3
            elif q == 4:
                return q4
            elif q == 5:
                return q5
        menuchoose = "yes"
        while menuchoose == "yes" or "y" in menuchoose:
            option = input(
                "1. View chat\n2. Delete chat\n3. Continue chat\n4. Update backup\n5. View backup\n6. Clear backup\n(Enter only number): ")
            if option == "1":
                time_check_start = datetime.datetime.now()
                timer = time_check_start+datetime.timedelta(seconds=50)
                a = input("Enter Security code: ")
                if datetime.datetime.now() < timer:  # TIME LIMIT OF 2 MIN TO ANSWER SENSITIVE INFO
                    pass
                else:
                    a = ""
                    print("Too slow")
                if a == secode:
                    os.startfile("user.txt")  # OPEN .txt IN NOTEPAD
                else:
                    for i in range(3):
                        print("Try Again")
                        time_check_start = datetime.datetime.now()
                        timer = time_check_start+datetime.timedelta(seconds=50)
                        a = input("Enter Security code: ")
                        if datetime.datetime.now() < timer:  # TIME LIMIT OF 2 MIN TO ANSWER SENSITIVE INFO
                            pass
                        else:
                            a = ""
                            print("Too slow")
                        if a == secode:
                            # OPEN .txt IN NOTEPAD
                            os.startfile("thirdparty.txt")
                            break
                        else:
                            print("Access Denied")
            elif option == "2":
                time_check_start = datetime.datetime.now()
                timer = time_check_start+datetime.timedelta(seconds=50)
                a = input("Enter Security code: ")
                if datetime.datetime.now() < timer:  # TIME LIMIT OF 2 MIN TO ANSWER SENSITIVE INFO
                    pass
                else:
                    a = ""
                    print("Too slow")
                if a == secode:
                    qno = FindQ()
                    j = input(f"Answer the following\n{GiveQ(qno)} is : ")
                    if j == Sequest[0]:
                        open("user.txt", "w").write("")
                        open("thirdparty.txt", "w").write("")
                        open("user.txt", "w").close()
                        open("thirdparty.txt", "w").close()
                    else:
                        print("Try Again Later")
                else:
                    print("ERROR\nYou are not the authorized user")
            elif option == "3":
                time_check_start = datetime.datetime.now()
                timer = time_check_start+datetime.timedelta(seconds=50)
                a = input("Enter Security code: ")
                if datetime.datetime.now() < timer:  # TIME LIMIT OF 2 MIN TO ANSWER SENSITIVE INFO
                    pass
                else:
                    a = ""
                    print("Too slow")
                if a == secode:
                    chat_cont = open("user.txt", "a")
                    thirdparty = open("thirdparty.txt", "a", encoding="utf-8")
                    time_cont = str(datetime.datetime.now())[:19:]
                    chat_cont.write(f"\nChat Continued at {time_cont}\n")
                    thirdparty.write("{}\n".format(dencrypt.Encrypt(
                        f"Chat Continued at {(time_cont)[:19:]}", encrylevel, "no")))
                    messagecheck = ""
                    count_up = 0
                    bye_lines = []
                    i = 0
                    print("Chat Continuing")
                    while count_up != 1:
                        if i % 2 == 0:
                            message = input("{}: ".format(user))
                            if message.strip() == "EXIT":
                                count_up = 1
                            else:
                                chat_cont.write(
                                    "{} : {}".format(user, message))
                                thirdparty.write("{} : {}".format(dencrypt.Encrypt(
                                    user, encrylevel, "no"), dencrypt.Encrypt(message, encrylevel, "no")))
                        else:
                            message = input("{}: ".format(chat2))
                            if message.strip() == "EXIT":
                                count_up = 1
                            else:
                                chat_cont.write(
                                    "{} : {}".format(chat2, message))
                                thirdparty.write("{} : {}".format(dencrypt.Encrypt(
                                    chat2, encrylevel, "no"), dencrypt.Encrypt(message, encrylevel, "no")))
                        chat_cont.write("\n")
                        thirdparty.write("\n")
                        time.sleep(1)
                        messagecheck = message.lower()
                        if "bye" in messagecheck:
                            bye_lines.append(i)
                        if len(bye_lines) > 1:
                            if bye_lines[-1]-bye_lines[-2] == 1:
                                count_up = 1
                        i += 1
                    chat_cont.close()
                    thirdparty.close()
                else:
                    print("Try Again Later")
            elif option == "4":
                time_check_start = datetime.datetime.now()
                timer = time_check_start+datetime.timedelta(seconds=50)
                a = input("Enter Security code: ")
                if datetime.datetime.now() < timer:  # TIME LIMIT OF 2 MIN TO ANSWER SENSITIVE INFO
                    pass
                else:
                    a = ""
                    print("Too slow")
                if a == secode:
                    randomiser = randint(0, 1)
                    n1, n2 = randint(0, 999), randint(0, 999)
                    root = Tk()  # OPEN TK WINDOW
                    root.title("Login Reqd")
                    center_x, center_y = root.winfo_screenwidth(), root.winfo_screenheight()
                    root.geometry(
                        "300x300+{}+{}".format(center_x//2, center_y//2))
                    if randomiser == 0:
                        greeting = Label(
                            text="{}+{}".format(n1, n2), font=("Arial", 30), foreground="red")
                    else:
                        greeting = Label(
                            text="{}-{}".format(n2, n1), font=("Arial", 30), foreground="cyan")
                    greeting.pack()
                    sentence = Label(
                        text="Enter the Result below\n", foreground="green")
                    sentence.pack()
                    input_result = Entry()  # FOR TEXT INPUT ON TK WINDOW
                    result = ""
                    input_result.pack()
                    Label(text="\n").pack()
                    success_check = ""
                    btn = Button(root, text="Enter", command=openNewWindow)
                    btn.pack()
                    mainloop()
                    if success_check == "ok":
                        usertxt = open("user.txt")
                        backupp = open("backup.txt", mode="a")
                        backupp.write(
                            f"New Backup at {str(datetime.datetime.now())[:19:]}\n")
                        use = usertxt.readlines()
                        for u in use:
                            if u == "\n" or "Chat starting at" in u or "Chat Continued at" in u:  # FOR SKIPPING UNWANTED LINES
                                pass
                            else:
                                backupp.write(u)
                        backupp.close()
                        usertxt.close()
                    else:
                        print("Try Again Later")
                else:
                    print("Access Denied")
            elif option == "5":
                time_check_start = datetime.datetime.now()
                timer = time_check_start+datetime.timedelta(seconds=50)
                a = input("Enter Security code: ")
                if datetime.datetime.now() < timer:  # TIME LIMIT OF 2 MIN TO ANSWER SENSITIVE INFO
                    pass
                else:
                    a = ""
                    print("Too slow")
                if a == secode:
                    randomiser = randint(0, 1)
                    n1, n2 = randint(0, 999), randint(0, 999)
                    root = Tk()  # OPEN TK WINDOW
                    root.title("Login Reqd")
                    center_x, center_y = root.winfo_screenwidth(), root.winfo_screenheight()
                    root.geometry(
                        "300x300+{}+{}".format(center_x//2, center_y//2))
                    if randomiser == 0:
                        greeting = Label(
                            text="{}+{}".format(n1, n2), font=("Arial", 30), foreground="red")
                    else:
                        greeting = Label(
                            text="{}-{}".format(n2, n1), font=("Arial", 30), foreground="cyan")
                    greeting.pack()
                    sentence = Label(
                        text="Enter the Result below\n", foreground="green")
                    sentence.pack()
                    input_result = Entry()  # FOR TEXT INPUT ON TK WINDOW
                    result = ""
                    input_result.pack()
                    Label(text="\n").pack()
                    success_check = ""
                    btn = Button(root, text="Enter", command=openNewWindow)
                    btn.pack()
                    mainloop()
                    if success_check == "ok":
                        os.startfile("backup.txt")  # OPEN .txt IN NOTEPAD
                    else:
                        print("Try Again Later")
                else:
                    print("Access Denied")
            elif option == "6":
                time_check_start = datetime.datetime.now()
                timer = time_check_start+datetime.timedelta(seconds=50)
                a = input("Enter Security code: ")
                if datetime.datetime.now() < timer:  # TIME LIMIT OF 2 MIN TO ANSWER SENSITIVE INFO
                    pass
                else:
                    a = ""
                    print("Too slow")
                if a == secode:
                    randomiser = randint(0, 1)
                    n1, n2 = randint(0, 999), randint(0, 999)
                    root = Tk()  # OPEN TK WINDOW
                    root.title("Login Reqd")
                    center_x, center_y = root.winfo_screenwidth(), root.winfo_screenheight()
                    root.geometry(
                        "300x300+{}+{}".format(center_x//2, center_y//2))
                    if randomiser == 0:
                        greeting = Label(
                            text="{}+{}".format(n1, n2), font=("Arial", 30), foreground="red")
                    else:
                        greeting = Label(
                            text="{}-{}".format(n2, n1), font=("Arial", 30), foreground="cyan")
                    greeting.pack()
                    sentence = Label(
                        text="Enter the Result below\n", foreground="green")
                    sentence.pack()
                    input_result = Entry()  # FOR TEXT INPUT ON TK WINDOW
                    result = ""
                    input_result.pack()
                    Label(text="\n").pack()
                    success_check = ""
                    btn = Button(root, text="Enter", command=openNewWindow)
                    btn.pack()
                    mainloop()
                    if success_check == "ok":
                        qno = FindQ()
                        j = input(f"Answer the following\n{GiveQ(qno)} is : ")
                        if j == Sequest[0]:
                            open("backup.txt", "w").write("")
                            open("backup.txt", "w").close()
                        else:
                            print("Try Again Later")
                    else:
                        print("Try Again Later")
                else:
                    print("ERROR")
                    print("You are not the authorized user")
            menuchoose = input("Do you want to continue ?(yes/no) : ")
            menuchoose = menuchoose.lower()
        print("Thank You for using our Services")
        root = Tk()  # OPEN TK WINDOW
        Label(text="How was your Experience ?\nPlease click on the numbered star then submit").pack()
        im1, im2, im3, im4, im5 = 0, 0, 0, 0, 0
        # FOR EXPERIENCE VALUE SELECTED=1 , OTHERS=0

        def image1():
            global im1, im2, im3, im4, im5
            im1, im2, im3, im4, im5 = 1, 0, 0, 0, 0

        def image2():
            global im2, im1, im3, im4, im5
            im2, im1, im3, im4, im5 = 1, 0, 0, 0, 0

        def image3():
            global im3, im1, im2, im4, im5
            im3, im1, im2, im4, im5 = 1, 0, 0, 0, 0

        def image4():
            global im4, im1, im2, im3, im5
            im4, im1, im2, im3, im5 = 1, 0, 0, 0, 0

        def image5():
            global im5, im1, im2, im3, im4
            im5, im1, im2, im3, im4 = 1, 0, 0, 0, 0
# BUTTON LOOKS LIKE A PHOTO
        rate1 = PhotoImage(file=r"images/star1.png")
        img1 = Button(root, image=rate1, command=image1)
        # img1.grid(row,col)
        img1.pack(side=LEFT)
        rate2 = PhotoImage(file=r"images/star2.png")
        img2 = Button(root, image=rate2, command=image2)
        img2.pack(side=LEFT)
        rate3 = PhotoImage(file=r"images/star3.png")
        img3 = Button(root, image=rate3, command=image3)
        img3.pack(side=LEFT)
        rate4 = PhotoImage(file=r"images/star4.png")
        img4 = Button(root, image=rate4, command=image4)
        img4.pack(side=LEFT)
        rate5 = PhotoImage(file=r"images/star5.png")
        img5 = Button(root, image=rate5, command=image5)
        img5.pack(side=LEFT)
        # ON SELECTION OF SUBMIT WINDOW CLOSES
        p = Button(root, text="Submit", command=root.destroy)
        p.pack()
        root.mainloop()
# ENTER EXP INTO .csv LIKE WE DO IN .txt AS BEING ENTERED SEPRATELY
        with open("data.csv") as f:
            global d
            d = f.readlines()
        for i in range(len(d)):
            if i == len(d)-1:
                pp = d[i]
                z = ""
                for j in range(len(pp)):
                    if j == pp.index("\n")-1:
                        if im1 == 1:
                            z += ",1"
                        elif im2 == 1:
                            z += ",2"
                        elif im3 == 1:
                            z += ",3"
                        elif im4 == 1:
                            z += ",4"
                        elif im5 == 1:
                            z += ",5"
                        else:
                            pass
                    else:
                        z += pp[j]
                d.pop()
                d.append(z)
            else:
                pass
        p = open("data.csv", "w")
        p.writelines(d)
        p.close()
# SINCE encrylevel(3) USES BIFID CIPHR AND LIST USED FOR ALL ENCRYPTION IS SAME THE XTRA LINES ARE REMOVED
        if encrylevel == 3:
            with open("keys.txt", "r", encoding="utf-8") as deleter:
                global rem
                rem = deleter.readlines()
            with open("keys.txt", "w", encoding="utf-8") as deleter:
                deleter.write(rem[0][:-1:])
        with open("user.txt", "w") as dodo:
            dodo.write("")
        with open("backup.txt", "w") as dodo:
            dodo.write("")
        with open("thirdparty.txt", "w") as dodo:
            dodo.write("")
        break
    else:
        # WAIT BEFORE CONTINUING LOOP
        time.sleep(30)
    if yip == 4:
        print("Bye Thank You for Visiting Us")
        DIR = os.getcwd()
        for i in os.listdir(DIR):
            if re.search(r"txt", i):
                os.remove(i)
    else:
        pass
