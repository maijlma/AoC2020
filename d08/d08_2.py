import copy

#method for reading the inputs from a .txt file
def read():
    lista = []
    file = open("../../d8/inputs.txt", "r")
    row = file.readline()
    while row != "":
        lista.append(row.rstrip())
        row = file.readline()
    file.close()
    return lista

def main():
    #reading inputs, initiating lists ect
    lista = read()
    lista1 = copy.deepcopy(lista)
    indeksit = [0] * len(lista)
    accumulator = 0
    i = 0
    j = 1

    #finding the indexes of the nop and jmp commands
    vaihdanop = []
    vaihdajmp = []
    x = 0
    for item in lista:
        if item.split(" ")[0] == "nop":
            vaihdanop.append(x)
        elif item.split(" ")[0] == "jmp":
            vaihdajmp.append(x)
        x +=1
    print("nop i: ", vaihdanop)
    print("jmp i:", vaihdajmp)
    lennop = len(vaihdanop)
    lenjmp = len(vaihdajmp)

    while True:
        #finding the end and breaking loop
        if i == len(lista) - 1:
            palat = lista[i].split(" ")
            if palat[0] == "acc":
                accumulator += int(palat[1])
            print("You reached the end!")
            break
        #growing the accumulator, finding the next index
        elif indeksit[i] == 0:
            indeksit[i] += 1
            palat = lista[i].split(" ")
            if palat[0] == "nop":
                i += 1
            elif palat[0] == "acc":
                accumulator += int(palat[1])
                i += 1
            elif palat[0] == "jmp":
                i += int(palat[1])
        #if the end is not reached, a nop/jmp change made to the list
        else:
            lista = copy.deepcopy(lista1)
            indeksit = [0] * len(lista)
            accumulator = 0
            i = 0
            #exhausting nop options first
            if j <= lennop:
                palat = lista[vaihdanop[0]].split(" ")
                lista[vaihdanop[0]] = "jmp " + palat[1]
                del vaihdanop[0]
            #looking at the jmp options if changing a nop is not the solution
            elif j <= lennop + lenjmp:
                palat = lista[vaihdajmp[0]].split(" ")
                lista[vaihdajmp[0]] = "nop " + palat[1]
                del vaihdajmp[0]
            j +=1

    print("Value of the accumulator: ", accumulator)

main()