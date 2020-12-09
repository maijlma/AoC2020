#Day 9: Encoding Error parts 1 and 2

import copy

#method for reading the inputs from a .txt file
def read():
    list = []
    file = open("../../../d8/inputs.txt", "r")
    row = file.readline()
    while row != "":
        list.append(int(row.rstrip()))
        row = file.readline()
    file.close()
    return list


def main():
    list = read()
    list_copy = copy.deepcopy(list)
    lenght = len(list_copy)
    #change preamble depending on input (test 5/full 25)
    preamble = 25
    i = preamble
    j = 0
    k = 0
    condition = False
    faulty_sum = 0

    #part 1: find faulty sum
    while i < lenght:
        sublist = list_copy[0:preamble]
        faulty_sum = list_copy[preamble]
        #go through sublist, mark condition as true if faulty_sum is found
        for n1 in sublist:
            for n2 in sublist:
                if n1 + n2 == faulty_sum:
                    if j != k:
                        condition = True
                k += 1
            j += 1
        #if condition is not found, print and store faulty_sum
        if condition == False:
            print("The number that doesn't fulfill the property:", faulty_sum)
            break
        condition = False
        i +=1
        if len(list_copy) > 6:
            del list_copy[0]

    #part2: find the list indexes adding up to faulty sum
    i = 0
    while i < len(list):
        sum = 0
        range_list = []
        for n in list[i:len(list)]:
            range_list.append(n)
            sum += n
            #if sums match, print the answer
            if sum == faulty_sum:
                range_list.sort()
                print("The encryption weakness:", range_list[0] + range_list[-1])
                return
        i += 1


main()
