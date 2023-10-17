from random import *
import BifidCipher
pa = []
i = 33
while i < 2045:
    if i in range(127, 160+1) or i in range(768, 879+1) or i in range(888, 890+1):
        pass
    elif i in range(896, 899+1) or i in range(1480, 1487+1) or i in range(1515, 1518+1):
        pass
    elif i in range(1525, 1535+1) or i in range(1970, 1983+1) or i in range(2027, 2036):
        pass
    elif i in range(1958, 1969) or i in range(1872, 1920) or i in range(1839, 1869):
        pass
    elif i in range(1770, 1808) or i in range(1759, 1769) or i in range(1646, 1756):
        pass
    elif i in range(1523, 1633) or i in range(1424, 1480) or i in range(1367, 1376) or i == 1328:
        pass
    elif i in range(1155, 1161) or i == 930 or i == 907 or i == 909 or i in range(688, 904):
        pass
    elif i in range(168, 188) or i == 1417 or i == 1416 or i == 1418 or i == 2044 or i == 1809:
        pass
    else:
        pa.append(i)
    i += 1
# print(len(pa)/2)
with open("keys.txt", "w") as ppp:
    ppp.write("")


def Encrypt(string, n=1, keyhere="no"):
    """If keyhere=="yes" then returning order is (key,string)
n is layers of encryption max is 3
Encryption key in keys.txt"""
    if n > 3:
        n = 3
    else:
        pass
    var = open("keys.txt", "a")
    for2 = ""
    encry = ""
    for3 = ""
    key = ""
    # 4th layer???work later
    # if randint before half add to chr if after half sub chr from randint
    choose = choice(pa)
    if pa.index(choose) < 10:
        indexadd = "000"+str(pa.index(choose))
    elif pa.index(choose) < 100:
        indexadd = "00"+str(pa.index(choose))
    elif pa.index(choose) < 1000:
        indexadd = "0"+str(pa.index(choose))
    elif pa.index(choose) < 10000:
        indexadd = ""+str(pa.index(choose))
    else:
        pass
    for m in range(1):
        if pa.index(choose) <= len(pa)//2:
            key += "BeL0W"+str(indexadd)
            shift = chr(choose)
            for i in string:
                encry += chr(ord(i)+pa.index(choose))
            if n == 1:
                var.write(key+"\n")
                var.close()
                if keyhere.lower() == "yes":
                    with open("keys.txt", "r", encoding="utf-8") as op:
                        infinite = op.readlines()[-1]
                        return infinite[:-1], encry
                else:
                    return encry
                break
            elif n == 2:
                power = randint(0, 9)
                key += str(power)
                for mm in range(len(encry)):
                    for2 += chr(ord(encry[mm])+((-1)**mm)*power)
                var.write(key+"\n")
                var.close()
                if keyhere.lower() == "yes":
                    with open("keys.txt", "r", encoding="utf-8") as op:
                        infinite = op.readlines()[-1]
                        return infinite[:-1], for2
                else:
                    return for2
            elif n == 3:
                no_more = BifidCipher.Bifid(string)
                for3 = no_more[0]
                key = no_more[1]
                var.close()
                with open("keys.txt", "a", encoding="utf-8") as wb:
                    wb.write(str(key)+"\n")
                if keyhere.lower() == "yes":
                    with open("keys.txt", "r", encoding="utf-8") as op:
                        infinite = op.readlines()[-1]
                        return infinite[:-1], for3
                else:
                    return for3
        else:
            key += "4FT3R"+str(indexadd)
            shift = chr(choose)
            for i in string:
                encry += chr(-ord(i)+pa.index(choose))
            if n == 1:
                var.write(key+"\n")
                var.close()
                if keyhere.lower() == "yes":
                    with open("keys.txt", "r", encoding="utf-8") as op:
                        infinite = op.readlines()[-1]
                        return infinite[:-1], encry
                else:
                    return encry
                break
            elif n == 2:
                power = randint(0, 9)
                key += str(power)
                for mm in range(len(encry)):
                    for2 += chr(ord(encry[mm])+((-1)**mm)*power)
                var.write(key+"\n")
                var.close()
                if keyhere.lower() == "yes":
                    with open("keys.txt", "r", encoding="utf-8") as op:
                        infinite = op.readlines()[-1]
                        return infinite[:-1], for2
                else:
                    return for2
            elif n == 3:
                no_more = BifidCipher.Bifid(string)
                for3 = no_more[0]
                key = no_more[1]
                var.close()
                with open("keys.txt", "a", encoding="utf-8") as wb:
                    wb.write(str(key)+"\n")
                if keyhere.lower() == "yes":
                    with open("keys.txt", "r", encoding="utf-8") as op:
                        infinite = op.readlines()[-1]
                        return infinite[:-1], for3
                else:
                    return for3


# var.write(key+"\n")
# var.close()
# if keyhere.lower()=="yes":
# with open("keys.txt","r") as op:
# infinite=op.readlines()[-1]
# print(infinite[:-1])
# else:pass
with open("solved.txt", "w") as ppp:
    ppp.write("")


def Decrypt(encryptstring: str, key):
    for2, dencry = "", ""
    if type(key) == str:
        if len(key) == 9:
            if "BeL0W" in key:
                index = int(key[5:])
                for i in encryptstring:
                    dencry += chr(ord(i)-index)
                return dencry
            elif "4FT3R" in key:
                index = int(key[5:])
                for i in encryptstring:
                    dencry += chr(index-ord(i))
                return dencry
            else:
                raise ValueError("Key is of Incorrect Pattern")
        elif len(key) == 10:
            if "BeL0W" in key:
                index = int(key[5:-1:])
                power = int(key[-1])
                for i in encryptstring:
                    dencry += chr(ord(i)-index)
                for mm in range(len(dencry)):
                    for2 += chr(ord(dencry[mm])-((-1)**mm)*power)
                return for2
            elif "4FT3R" in key:
                index = int(key[5:-1:])
                power = int(key[-1])
                for i in encryptstring:
                    dencry += chr(index-ord(i))
                for mm in range(len(dencry)):
                    for2 += chr(ord(dencry[mm])+((-1)**mm)*power)
                return for2
            else:
                raise ValueError("Key is of Incorrect Pattern")
    elif type(key) == list:
        orig_str = BifidCipher.Bifid_Rev(encryptstring, key)
        return orig_str
    else:
        raise TypeError("Type Not Supported")
# print(Encrypt("Hi im Pratham",2,"no"))
# print(Decrypt("̫˸͓˸̣̆́˯̒˭̋̀̆","4FT3R08749"))
