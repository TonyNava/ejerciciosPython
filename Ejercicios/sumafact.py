# -*- coding: utf-8 -*-

def sumafact(num):
    if num == 0:
        return 0

    return num + sumafact(num-1)
    
if __name__ == "__main__":
    num = int(raw_input("Give me a number: "))
    suma = sumafact(num)
    print("The sum fact. is : {}".format(suma))