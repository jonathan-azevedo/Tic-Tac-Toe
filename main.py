import random
import time

def boardprinter(values):
    print("                                                                                                           ")
    print("                                  |       |        ")
    print("                              {}   |   {}   |   {}    ".format(values[0],values[1],values[2]))
    print("                           _______|_______|_______ ")
    print("                                  |       |        ")
    print("                              {}   |   {}   |   {}    ".format(values[3],values[4],values[5]))
    print("                           _______|_______|_______ ")
    print("                                  |       |        ")
    print("                              {}   |   {}   |   {}    ".format(values[6],values[7],values[8]))
    print("                                  |       |        ")
    print("                                                                                                           ")

def boardfilled():
    for i in boardvalues:
         if i == "-":
            return False
    return True

def checkVictory():
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for x in wins:
        if all(y in players[current_player] for y in x):
            return True
    return False

#Game loop
def GameInit():
    global current_player
    while True:
        boardprinter(boardvalues)
        #Check if board is filled
        if boardfilled():
            print("The game TIED. Play again!")
            time.sleep(2)
            break
        #Try to take user movement
        try:
            print("Player " + f"{current_player}, " "it's your turn. Which box do you chose?")
            move = int(input())
        except ValueError:
            print("This is not a valid box. Try again!")
            time.sleep(1)
            continue
        if move<1 or move>9:
            print("This is not a valid box. Try again!")
            time.sleep(1)
            continue
        if boardvalues[move-1] != "-":
                 print("This box is already filled. Try again!")
                 time.sleep(1)
                 continue
        #Update the board and store the player movement
        boardvalues[move-1] = current_player
        players[current_player].append(move)
        #Checks if the player won
        if checkVictory():
            boardprinter(boardvalues)
            print(f"Congratulations, {current_player}, you won the game!")
            time.sleep(2)
            playAgain()
        #Switch player
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"
#Asks if user wants to play again
def playAgain():
    choice = input("Do you want to play again? (y/n)")
    if choice == "y" or choice == "Y":
        global boardvalues, players
        boardvalues = ["-","-","-","-","-","-","-","-","-"]
        players = {"X":[], "O":[]}
        GameInit()
    elif choice == "n" or choice == "N":
        print(logo)
        print("\n")
        print("Thanks for playing!")
        time.sleep(3)
        exit()
    else:
        print("Choose y or n")
        time.sleep(1)
        playAgain()

boardvalues = ["-","-","-","-","-","-","-","-","-"]
players = {"X":[], "O":[]}
current_player = random.choice(["X","O"])
logo = r"""
  _______ _                 _______                    _______         
 |__   __(_)               |__   __|                  |__   __|        
    | |   _  ___   ______     | | __ _  ___   ______     | | ___   ___ 
    | |  | |/ __| |______|    | |/ _` |/ __| |______|    | |/ _ \ / _ \
    | |  | | (__              | | (_| | (__              | | (_) |  __/
    |_|  |_|\___|             |_|\__,_|\___|             |_|\___/ \___|
                                                     By Jonathan Azevedo"""

print(logo)
GameInit()
   
