#Day 6: Custom Customs Part 2

import string

#counting the questions to which everyone answered "yes"
def tarkista(lista, n):
    x = 0
    mjono = string.ascii_lowercase
    for char in mjono:
        if lista.count(char) == n:
            x +=1
    return x

def main():
    summa = 0
    lista = []
    n = 0

    file = open("inputs.txt", "r")
    row = file.readline()
    while row != "":
        #reading rows of customs declarations
        if row != "\n":
            row = row.rstrip()
            for char in row:
                lista.append(char)
            n += 1
        #finding the count for each group
        else:
            x = tarkista(lista, n)
            summa += x
            lista = []
            n = 0
        row = file.readline()
    file.close()

    print("Counting sum of questions to which everyone answered 'yes':", summa)

main()