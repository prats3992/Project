from random import *
import BifidCipher
pa = [i for i in range(33, 2045) if i not in range(127, 160+1) and i not in range(768, 879+1) and i not in range(888, 890+1) and i not in range(896, 899+1) and i not in range(1480, 1487+1) and i not in range(1515, 1518+1) and i not in range(1525, 1535+1) and i not in range(1970, 1983+1) and i not in range(2027, 2036) and i not in range(1958, 1969) and i not in range(1872, 1920) and i not in range(1839, 1869)
      and i not in range(1770, 1808) and i not in range(1759, 1769) and i not in range(1646, 1756) and i not in range(1523, 1633) and i not in range(1424, 1480) and i not in range(1367, 1376) and i != 1328 and i not in range(1155, 1161) and i != 930 and i != 907 and i != 909 and i not in range(688, 904) and i not in range(168, 188) and i != 1417 and i != 1416 and i != 1418 and i != 2044 and i != 1809]
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
    for2, encry, for3, key = "", "", "", ""
    # 4th layer???work later
    # if randint before half add to chr if after half sub chr from randint
    choose = choice(pa)
    indexadd = str(pa.index(choose)).zfill(4)
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
# print(Encrypt("Hi im Pratham",randint(1,3),"yes"))
# print(Decrypt("̫˸͓˸̣̆́˯̒˭̋̀̆","4FT3R08749"))
