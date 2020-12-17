#Day 13: Shuttle Search

def process_inputs():
    time = int(input("What is the earliest timestamp you could depart?\n"))
    IDs = input("Please enter the bus IDs:\n")
    IDs = IDs.split(",")
    while "x" in IDs:
        IDs.remove("x")
    for i in range(len(IDs)):
        IDs[i] = int(IDs[i])
    return time, IDs

def main():
    time, IDs = process_inputs()
    closest = time * 2
    bus = 0

    #determining the closest buss & its departure time
    for busID in IDs:
        bus_time = 0
        while bus_time < time:
            bus_time += busID
        if bus_time - time < closest - time:
            bus = busID
            closest = bus_time

    print("The earliest bus you could take is:", bus)
    print("It departs at timestamp", closest, "so you will have to wait", closest - time, "minutes")
    print("The earliest bus multiplied by the wait:", (closest - time) * bus)

main()