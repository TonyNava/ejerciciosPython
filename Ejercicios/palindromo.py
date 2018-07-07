# --*- coding: utf-8 -*-
import random

def run():
    strWord = str(raw_input("Write a word: "))
    reversedWord = []

    for letter in strWord:
        reversedWord.insert(0,letter)
    
    joinWord= "".join(reversedWord)

    if strWord==joinWord:
        print("it's palindrome")
    else:
        print("not is palindrome")

if __name__ == "__main__":
    run()