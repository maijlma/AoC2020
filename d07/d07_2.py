#Day 7: Handy Haversacks Part 2

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
    sisimmaiset = {}
    sisalla = []
    i = 4
    while i < len(palat):
        if palat[i] != "no":
            vari = palat[i+1] + palat[i+2]
            sisimmaiset[vari] = palat[i]
            sisalla.append(vari)
        i += 4
    return ulommainen, sisimmaiset

#adding the bags in a specific bag to a list according to the rules
def nimetlistaan(laukut, laukku):
    lista = []
    dict = laukut[laukku]
    for x in dict:
        i = 0
        while i < int(dict[x]):
            lista.append(x)
            i += 1
    return lista

def main():
    #initializing lists etc, going through rows to fill the laukut dictionary
    lista = read()
    varitsisaltaa = []
    laukut = {}
    for line in lista:
        ulommainen, sisalla = kasittelerivi(line)
        laukut[ulommainen] = sisalla

    #finding all the bags within the shiny golden bag
    n = -1
    tarkasteltavat = ["shinygold"]
    while True:
        kierroksenlaukut = []
        for laukku in tarkasteltavat:
            if laukku in laukut:
                kierroksenlaukut += nimetlistaan(laukut, laukku)
        if len(kierroksenlaukut) == 0:
            n += len(tarkasteltavat)
            break
        n += len(tarkasteltavat)
        tarkasteltavat = kierroksenlaukut

    print("Bags in the Shiny Golden bag:", n)
main()