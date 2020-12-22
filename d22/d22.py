#Day 22: Crab Combat Part 1

#find player1 and player2 decks
def read_cards():
    file = open("../../../test.txt", "r")
    try:
        lst = file.readlines()
        file.close()
    except OSError:
        print("Could not read the input!")
    i = lst.index("\n")
    player1 = [int(x.rstrip()) for x in lst[1:i]]
    player2 = [int(x.rstrip()) for x in lst[i + 2:]]
    return player1, player2

#see which player wins
def play(player1, player2):
    while len(player1) > 0 and len(player2) > 0:
        #p1 wins
        if player1[0] > player2[0]:
            player1.append(player1[0])
            player1.append(player2[0])
        #p2 wins
        else:
            player2.append(player2[0])
            player2.append(player1[0])
        #remove from top
        del player1[0]
        del player2[0]
    #return winner
    if len(player1) > 0:
        return player1
    else:
        return player2

#calculate winner's score
def score(winner):
    n = len(winner)
    score = 0
    for x in winner:
        score += x * n
        n -= 1
    print("The winning player's score is:", score)

def main():
    player1, player2 = read_cards()

    #Part 1
    winner = play(player1, player2)
    score(winner)


main()