#Day 10: Adapter Array

import numpy as np

#method for reading the inputs from a .txt file
def read():
    list = []
    file = open("test.txt", "r")
    row = file.readline()
    while row != "":
        list.append(int(row.rstrip()))
        row = file.readline()
    file.close()
    return list

    #part1: determining the number of 1- and 3-jolt differences
def part_one(list):
    diff1 = 0
    diff3 = 1   #as connecting the device adds a difference of 3
    jolts = 0
    for j in list:
        if j - jolts == 1:
            diff1 += 1
        elif j - jolts == 3:
            diff3 += 1
        jolts = j
    return diff1 * diff3

def main():
    list = read()
    list.sort()
    product = part_one(list)
    print("Number of 1-jolt diff multiplied by n of 3-jolt diff:", product)

    #part2
    sublists = []
    i = 0
    while i < len(list):
        s = []
        previous = list[i]
        for j in list[i:]:
            if j - previous < 3:
                s.append(j)
                previous = j
        sublists.append(s)
        i += len(s)
    print(sublists)

    ns = []
    for sub in sublists:
        if len(sub) <= 2:
            n = 1
        elif len(sub) == 3:
            n = 2
        elif len(sub) == 4:
            n = 4
        elif len(sub) == 5:
            n = 8
        ns.append(n)

    print(ns)
    product = 1
    for l in ns:
        product *= l
    print("Distinct ways to arrange the adapters:",product)


main()