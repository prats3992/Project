import random


def generate_rand_list():
    characters = r"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 ~!@#$%^&*()_+{}|:\"<>?`-=[]\\;',./"
    rand_list = [list(characters[i:i+10])
                 for i in range(0, len(characters), 10)]
    random.shuffle(rand_list)
    return rand_list
