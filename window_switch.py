from tkinter import *
from tkinter.ttk import *
from random import randint
import time
'''ma=Tk()
ma.title("")
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
##              INPUT NOT ACCESSIBLE
'''                    randomiser=randint(0,1)
                    n1,n2=randint(0,999),randint(0,999)
                    root=Tk()
                    root.title("Login Reqd")
                    center_x,center_y=root.winfo_screenwidth(),root.winfo_screenheight()
                    root.geometry("300x300+{}+{}".format(center_x//2,center_y//2))
                    if randomiser==0:
                        greeting=Label(text="{}+{}".format(n1,n2),font=("Arial",30),foreground="red")
                    else:
                        greeting=Label(text="{}-{}".format(n2,n1),font=("Arial",30),foreground="cyan")
                    greeting.pack()
                    sentence=Label(text="Enter the Result below\n",foreground="green")
                    sentence.pack()
                    input_result=Entry()
                    result=""
                    def Click():
                        global result
                        result=input_result.get()
                    input_result.pack()
                    Label(text="\n").pack()
                    success_check=""
                    def Over(event):
                        time.sleep(5)
                        root.destroy()
                    def openNewWindow():
                        global randomiser,result,n1,n2,success_check
                        new=Toplevel(root)
                        Click()
                        if randomiser==0:
                            if result==str(n1+n2):
                                new.title("Access Granted")
                                new.geometry("200x200+{}+{}".format(center_x//2,center_y//2))
                                sentence=Label(new,text="Successful",font=("Arial",30),foreground="green")
                                success_check="ok"
                            else:
                                new.title("Access Denied")
                                new.geometry("200x200+{}+{}".format(center_x//2,center_y//2))
                                sentence=Label(new,text="Try Again",font=("Arial",30),foreground="green")
                                success_check="no"
                        elif randomiser==1:
                            if result==str(n2-n1):
                                new.title("Access Granted")
                                new.geometry("200x200+{}+{}".format(center_x//2,center_y//2))
                                sentence=Label(new,text="Successful",font=("Arial",30),foreground="green")
                                success_check="ok"
                            else:
                                new.title("Access Denied")
                                new.geometry("200x200+{}+{}".format(center_x//2,center_y//2))
                                sentence=Label(new,text="Try Again",font=("Arial",30),foreground="green")
                                success_check="no"
                        sentence.bind("<Enter>",Over)
                        sentence.pack()
                    btn=Button(root,text="Enter",command=openNewWindow)
                    btn.pack()
                    mainloop()'''
root=Tk()
Label(text="How was your Experience ?").pack()
im1,im2,im3,im4,im5=0,0,0,0,0
def image1():
    global im1,im2,im3,im4,im5
    im1,im2,im3,im4,im5=1,0,0,0,0
def image2():
    global im2,im1,im3,im4,im5
    im2,im1,im3,im4,im5=1,0,0,0,0
def image3():
    global im3,im1,im2,im4,im5
    im3,im1,im2,im4,im5=1,0,0,0,0
def image4():
    global im4,im1,im2,im3,im5
    im4,im1,im2,im3,im5=1,0,0,0,0
def image5():
    global im5,im1,im2,im3,im4
    im5,im1,im2,im3,im4=1,0,0,0,0
rate1=PhotoImage(file="star1.png")
img1=Button(root,image=rate1,command=image1)
img1.pack()
rate2=PhotoImage(file="star2.png")
img2=Button(root,image=rate2,command=image2)
img2.pack()
rate3=PhotoImage(file="star3.png")
img3=Button(root,image=rate3,command=image3)
img3.pack()
rate4=PhotoImage(file="star4.png")
img4=Button(root,image=rate4,command=image4)
img4.pack()
rate5=PhotoImage(file="star5.png")
img5=Button(root,image=rate5,command=image5)
img5.pack()
p=Button(root,text="Submit",command=root.destroy)
p.pack(ipadx=10,ipady=10)
root.mainloop()
if im1==1:
    pass
elif im2==1:
    pass
elif im3==1:
    pass
elif im4==1:
    pass
elif im5==1:
    pass
else:
    pass