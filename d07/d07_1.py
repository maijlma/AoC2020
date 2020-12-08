#Day 7: Handy Haversacks Part 1

#reading the inputs from a .txt file
def read():
    list = []
    file = open("inputs.txt", "r")
    row = file.readline()
    while row != "":
        list.append(row.rstrip())
        row = file.readline()
    file.close()
    return list

#extracting information from a single row
def kasittelerivi(mjono):
    palat = mjono.split(" ")
    ulommainen = palat[0] + palat[1]
    sisalla = []
    i = 4
    while i < len(palat):
        if palat[i] != "no":
            vari = palat[i+1] + palat[i+2]
            sisalla.append(vari)
        i += 4
    return ulommainen, sisalla

def main():
    lista = read()
    varitsisaltaa = []
    laukut = {}

    #adding bags to a dictionary
    for line in lista:
        ulommainen, sisalla = kasittelerivi(line)
        laukut[ulommainen] = sisalla
        #finding the bags including a shiny gold bag inside
        for vari in sisalla:
            if vari == "shinygold":
                if ulommainen not in varitsisaltaa:
                    varitsisaltaa.append(ulommainen)

    #going through the bags to find those that can include a shiny gold one
    all = varitsisaltaa
    while True:
        ulommaiset = []
        for key in laukut:
            lista = laukut[key]
            for item in lista:
                if item in varitsisaltaa:
                    if key not in all:
                        ulommaiset.append(key)
        #..until there are no more
        if len(ulommaiset) == 0:
            break
        all += ulommaiset
        varitsisaltaa = ulommaiset

    #removing duplicates
    newall = list(dict.fromkeys(all))

    print("This many colors can contain a shiny gold bag:", len(newall))

main()