from random import *
pa=[]
i=33
while i<2045:
    if i in range(127,160+1) or i in range(768,879+1) or i in range(888,890+1) or i in range(896,899+1) or i in range(1480,1487+1) or i in range(1515,1518+1) or i in range(1525,1535+1) or i in range(1970,1983+1) or i in range(2027,2036) or i in range(1958,1969) or i in range(1872,1920) or i in range(1839,1869) or i in range(1770,1808) or i in range(1759,1769) or i in range(1646,1756) or i in range(1523,1633) or i in range(1424,1480) or i in range(1367,1376) or i==1328 or i in range(1155,1161) or i==930 or i==907 or i==909 or i in range(688,904) or i in range(168,188) or i==1417 or i==1416 or i==1418 or i==2044 or i==1809:pass
    else:pa.append(i)
    i+=1
#print(len(pa)/2)
with open("ksp.txt","w") as ppp:
    ppp.write("")
def Encrypt(string,n=1,keyhere="no"):
    """Only strings for now
n is layers of encryption max is 2
Encryption key in ksp.txt"""
    if n>2:
        n=2
    else:
        pass
    var=open("ksp.txt","a")
    for2=""
    encry=""
    key=""
    #take till 2047 from 33-[127,160]-[768,879]-[888,890]-[896,899]-[1480,1487]-[1515,1518]-[1525,1535]-[1970,1983]
    #key="BELOWAFTERindex+someno.-someno."
    #create shift word from ????-->+((-1)^index)*random(more than 33 less than 100)[all this to the shifted word]-->
    #3rd & 4th layer???work later
    #if randint before half add to chr if after half sub chr from randint
    choose=choice(pa)
    if pa.index(choose)<10:
        indexadd="000"+str(pa.index(choose))
    elif pa.index(choose)<100:
        indexadd="00"+str(pa.index(choose))
    elif pa.index(choose)<1000:
        indexadd="0"+str(pa.index(choose))
    elif pa.index(choose)<10000:
        indexadd=""+str(pa.index(choose))
    else:pass
    for m in range(1):
        if pa.index(choose)<=len(pa)//2:
            key+="BeL0W"+str(indexadd)
            shift=chr(choose)
            for i in string:
  #              print(chr(ord(i)+pa.index(choose)))
                encry+=chr(ord(i)+pa.index(choose))
            if n==1:
                print(encry)
                break
            else:
                power=randint(0,9)
                key+=str(power)
                for killer in range(len(encry)):
                    for2+=chr(ord(encry[killer])+((-1)**killer)*power)
                print(for2)
        else:
            key+="4FT3R"+str(indexadd)
            shift=chr(choose)
            for i in string:
                encry+=chr(-ord(i)+pa.index(choose))
            if n==1:
                print(encry)
                break
            else:
                power=randint(0,9)
                key+=str(power)
                for killer in range(len(encry)):
                    for2+=chr(ord(encry[killer])+((-1)**killer)*power)
                print(for2)
    var.write(key+"\n")
    var.close()
    if keyhere.lower()=="yes":
        with open("ksp.txt","r") as op:
            infinite=op.readlines()[-1]
            print(infinte[:-1])
    else:pass
#                print(chr(-ord(i)+pa.index(choose)))
    #print(shift,indexadd,key)
        #if belo then chr(ord(orig)+index) elze chr(index-ord(orig))
