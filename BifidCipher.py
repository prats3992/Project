import random
"""
[[ABCDE],[FGHIJ],[KLMNO],[PQRST],[VWXYZ]]
[[abcde],[fghij],[klmno],[pqrst],[vwxyz]]
[[123],[456],[789]]
 ~!@#$%^&*()_+{}|:"<>?`-=[]\;',./
 """
# square matrix of 10
# list no==row , inside list index==col
# FOR EXPLANATION VISIT https://www.geeksforgeeks.org/bifid-cipher-in-cryptography/
list_hold = [["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
             ["K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"],
             ["U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d"],
             ["e", "f", "g", "h", "i", "j", "k", "l", "m", "n"],
             ["o", "p", "q", "r", "s", "t", "u", "v", "w", "x"],
             ["y", "z", "0", "1", "2", "3", "4", "5", "6", "7"],
             ["8", "9", " ", "~", "!", "@", "#", "$", "%", "^"],
             ["&", "*", "(", ")", "_", "+", "{", "}", "|", ":"],
             ['"', "<", ">", "?", "`", "-", "=", "[", "]", "\\"],
             [";", "'", ",", ".", "/", f"{chr(247)}", f"{chr(215)}", f"{chr(177)}", f"{chr(176)}", f"{chr(449)}"]]
rand_list = []
for i in range(len(list_hold)):
    k = random.choice(list_hold)
    rand_list.append(k)
    list_hold.remove(k)


def Bifid(string):
    if len(string) % 2 == 0:
        pass
    else:
        string += " "
    row = col = output = ""
    for i in string:
        for j in rand_list:
            if i in j:
                row += f"{rand_list.index(j)}"
                col += f"{j.index(i)}"
    row_split, col_split = [], []
    for i in range(0, len(col), 2):
        col_split.append(col[i]+col[i+1])
        row_split.append(row[i]+row[i+1])
    final_list = []
    for i in range(len(row_split)):
        final_list.append(row_split[i]+col_split[i])
    for i in final_list:
        a, b, c, d = int(i[0]), int(i[1]), int(i[2]), int(i[3])
        output += rand_list[a][b]
        output += rand_list[c][d]
    return output, rand_list


def Bifid_Rev(output: str, rev_list: list):
    # z=[]
    y = []
    for i in range(0, len(output), 2):
        p = output[i]+output[i+1]
        for j in rev_list:
            if output[i] in j:
                y.append(str(rev_list.index(j))+str(j.index(output[i])))
        for j in rev_list:
            if output[i+1] in j:
                y.append(str(rev_list.index(j))+str(j.index(output[i+1])))
        # z.append(p)
        # print(y)
        # print(z)
    row_split, col_split = [], []
    for i in range(0, len(y), 2):
        row_split.append(y[i])
        col_split.append(y[i+1])
    # print(row_split)
    # print(col_split)
    row = col = ""
    for i in range(len(row_split)):
        row += row_split[i]
        col += col_split[i]
    # print(row)
    # print(col)
    rev = ""
    for i in range(len(col)):
        rev += rev_list[int(row[i])][int(col[i])]
    if rev.endswith(" ") == True and len(rev.strip()) % 2 != 0:
        rev = rev.rstrip()
        return rev
    else:
        return rev

# print(Bifid("Hello Stupid"))
# print(Bifid_Rev("Fyj5o OFs'hx", [['8', '9', ' ', '~', '!', '@', '#', '$', '%', '^'], ['&', '*', '(', ')', '_', '+', '{', '}', '|', ':'], ['K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T'], ['U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd'], ['o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x'], ['e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'], [';', "'", ',', '.', '/', '÷', '×', '±', '°', 'ǁ'], ['y', 'z', '0', '1', '2', '3', '4', '5', '6', '7'], ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'], ['"', '<', '>', '?', '`', '-', '=', '[', ']', '\\']]))
