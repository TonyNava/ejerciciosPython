# -*- coding: utf-8 -*-

def run():
    counter=0
    with open("numeros.txt","r") as File : 
        for line in File:
            counter += line.count("a")
    print('a se repite {}'.format(counter))
    
if __name__ == "__main__":
    run()