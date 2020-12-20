#Day 20: Jurassic Jigsaw Part 1

#read and gather information on tiles
def read_file():
    tile_dict = {}
    try:
        row_list = []
        file = open("../../../test.txt", "r")
        row = file.readline()
        while row != "":
            if row == "\n":
                nro, sides = tile(row_list)
                tile_dict[nro] = sides
                row_list = []
            else:
                row = row.rstrip()
                row_list.append(row)
            row = file.readline()
        nro, sides = tile(row_list)
        tile_dict[nro] = sides
        file.close()
        return tile_dict
    except OSError:
        print("File not read correctly!")

#identifies the name and four sides of a tile
def tile(row_list):
    pieces = row_list[0].split(" ")
    nro = int(pieces[1][:4])
    sides = [row_list[1]]
    del row_list[0]
    left = ""
    right = ""
    for row in row_list:
        left += row[0]
        right += row[-1]
    sides.append(right)
    sides.append(row_list[-1])
    sides.append(left)
    return nro, sides

def main():
    tile_dict = read_file()

    #identify the corners for part 1
    corner_list = []
    for tile in tile_dict:
        bordering = 0
        for side in tile_dict[tile]:
            for tile2 in tile_dict:
                if tile != tile2:
                    for side2 in tile_dict[tile2]:
                        if side == side2 or side[::-1] == side2:
                            bordering += 1
        if bordering == 2:
            corner_list.append(tile)

    print("The corner IDs are:", corner_list)
    product = 1
    for corner in corner_list:
        product *= corner
    print("The product of the IDs is:", product)

main()