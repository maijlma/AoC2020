#Day 5: Binary Boarding parts 1 and 2

#redefining the range for the seat number
def range(lower, upper, char):
    if char == "L" or char == "F":
        range = upper - lower + 1
        upper -= range / 2
    if char == "R" or char == "B":
        range = upper - lower + 1
        lower += range/2
    return lower, upper

def main():
    list = []
    IDs = []

    #reading the .txt inputs
    file = open("inputs.txt", "r")
    row = file.readline().rstrip()
    while row != "":
        list.append(row)
        row = file.readline().rstrip()
    file.close()

    #determining the ID on each Boarding Pass
    for item in list:
        i = 0
        lower = 0
        upper = 128
        left = 0
        right = 7
        for char in item:
            if i < 7:
                lower, upper = range(lower, upper, char)
            else:
                left, right = range(left, right, char)
            i += 1
        IDs.append(int(lower) * 8 + int(left))

    IDs.sort()
    print("Highest seat ID:", IDs[-1])

    #finding which seat is missing
    previous = IDs[0] -1
    for ID in IDs:
        if ID - previous != 1:
            print("ID of my seat:", ID-1)
        previous = ID

main()