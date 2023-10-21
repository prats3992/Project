import random
from utils import generate_rand_list

"""
[[ABCDE],[FGHIJ],[KLMNO],[PQRST],[VWXYZ]]
[[abcde],[fghij],[klmno],[pqrst],[vwxyz]]
[[123],[456],[789]]
 ~!@#$%^&*()_+{}|:"<>?`-=[]\;',./
"""
# square matrix of 10
# list no==row , inside list index==col
# FOR EXPLANATION VISIT https://www.geeksforgeeks.org/bifid-cipher-in-cryptography/

rand_list = generate_rand_list()
print(len(rand_list))


def Bifid(string: str) -> (str, list[list[str]]):
    string += " " if len(string) % 2 != 0 else ""
    row = col = output = ""
    for i in string:
        for j in rand_list:
            if i in j:
                row += f"{rand_list.index(j)}"
                col += f"{j.index(i)}"
    row_split, col_split = [], []
    for i in range(0, len(col), 2):
        col_split.append(col[i:i+2])
        row_split.append(row[i:i+2])
    final_list = []
    for i in range(len(row_split)):
        final_list.append(row_split[i]+col_split[i])
    for i in final_list:
        a, b, c, d = int(i[0]), int(i[1]), int(i[2]), int(i[3])
        output += rand_list[a][b]
        output += rand_list[c][d]
    return output, rand_list


def Bifid_Rev(output: str, rev_list: list[list[str]]) -> str:
    y = []
    for i in range(0, len(output), 2):
        p = output[i]+output[i+1]
        for j in rev_list:
            if output[i] in j:
                y.append(str(rev_list.index(j))+str(j.index(output[i])))
        for j in rev_list:
            if output[i+1] in j:
                y.append(str(rev_list.index(j))+str(j.index(output[i+1])))
    row_split, col_split = [], []
    for i in range(0, len(y), 2):
        row_split.append(y[i])
        col_split.append(y[i+1])
    row = col = ""
    for i in range(len(row_split)):
        row += row_split[i]
        col += col_split[i]
    rev = ""
    for i in range(len(col)):
        rev += rev_list[int(row[i])][int(col[i])]
    rev = rev.rstrip() if rev.endswith(
        " ") == True and len(rev.strip()) % 2 != 0 else rev
    return rev


def main():
    plaintext = input("Enter plaintext: ")
    ciphertext, rand_list = Bifid(plaintext)
    print(f"Ciphertext: {ciphertext}")
    print(f"Random List: {rand_list}")
    decrypted_text = Bifid_Rev(ciphertext, rand_list)
    print(f"Decrypted Text: {decrypted_text}")


if __name__ == "__main__":
    main()
