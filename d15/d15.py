#Day 15: Rambunctious Recitation

#asking user for input & processing it for use
def process_inputs():
    csv = input("What is your puzzle input?\n")
    list = csv.split(",")
    for i in range(len(list)):
        list[i] = int(list[i])
    return list

def main():
    list = process_inputs()
    i = len(list) - 1

    #reciting numbers
    while len(list) < 2020:
        number = list[-1]
        #determining next when number hasn't been spoken before
        if list.count(number) == 1:
            next = 0
        #finding next if number has already been spoken by using indexes
        else:
            number_i = list.index(number)
            next = len(list) - (number_i + 1)
            list[number_i] = -1
        list.append((next))

    print("The 2020th number spoken is:", list[-1])

main()