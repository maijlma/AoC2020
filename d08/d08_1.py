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
    lista = read()
    indeksit = [0] * len(lista)
    accumulator = 0
    i = 0

    while True:
        #growing accumulator, finding next index
        if indeksit[i] == 0:
            indeksit[i] += 1
            palat = lista[i].split(" ")
            if palat[0] == "nop":
                i += 1
            elif palat[0] == "acc":
                accumulator += int(palat[1])
                i += 1
            elif palat[0] == "jmp":
                i += int(palat[1])
        #breaks when returns to an index that has been visited before
        else:
            break

    print("Value of the accumulator: ", accumulator)

main()