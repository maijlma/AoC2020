#Day 22: Crab Combat Part 1
import copy

#find player1 and player2 decks
def read_cards():
    file = open("test.txt", "r")
    try:
        lst = file.readlines()
        file.close()
    except OSError:
        print("Could not read the input!")
    i = lst.index("\n")
    player1 = [int(x.rstrip()) for x in lst[1:i]]
    player2 = [int(x.rstrip()) for x in lst[i + 2:]]
    return player1, player2

#see which player wins normal combat
def play_combat(player1, player2):
    while len(player1) > 0 and len(player2) > 0:
        player1, player2 = round(player1, player2)
        #remove from top
        del player1[0]
        del player2[0]
    #return winner
    if len(player1) > 0:
        return 1, player1
    else:
        return 2, player2

#compare the 0 index values & modify lists
def round(player1, player2):
    if player1[0] > player2[0]:
        player1.append(player1[0])
        player1.append(player2[0])
    else:
        player2.append(player2[0])
        player2.append(player1[0])
    return player1, player2

#playing the recursive game
def play_recursive(player1, player2):
    roundlist = []
    while len(player1) > 0 and len(player2) > 0:
        #check if round played before, declare winner if is
        lst = player1 + player2
        if lst not in roundlist:
            roundlist.append(lst)
            print("Appended!")
        else:
            return player1
        #check for recursion, go to subgame if found
        if player1[0] <= len(player1) - 1 and player2[0] <= len(player2) - 1:
            print("Subgame!")
            win, winner = play_combat(player1[1:player1[0] + 1], player2[1:player2[0] + 1])
            if win == 1:
                player1.append(player1[0])
                player1.append(player2[0])
            else:
                player2.append(player2[0])
                player2.append(player1[0])
        #regular combat terms
        else:
            print("Regular!")
            player1, player2 = round(player1, player2)
        #remove the played card
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
    p1 = copy.deepcopy(player1)
    p2 = copy.deepcopy(player2)

    #Part 1: play combat
    win, winner = play_combat(p1, p2)
    score(winner)

    #Part 2: play recursive combat
    winner = play_recursive(player1, player2)
    score(winner)

main()