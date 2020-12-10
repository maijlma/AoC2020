#Day 10: Adapter Array

#method for reading the inputs from a .txt file
def read():
    list = []
    file = open("inputs.txt", "r")
    row = file.readline()
    while row != "":
        list.append(int(row.rstrip()))
        row = file.readline()
    file.close()
    return list

def main():
    list = read()
    list.sort()
    diff1 = 0
    diff3 = 1   #as connecting the device adds a difference of 3
    jolts = 0

    #Part1: determining the number of 1- and 3-jolt differences
    for j in list:
        if j - jolts == 1:
            diff1 += 1
        elif j - jolts == 3:
            diff3 += 1
        jolts = j
    print("Number of 1-jolt diff multiplied by n of 3-jolt diff:", diff1 * diff3)


main()