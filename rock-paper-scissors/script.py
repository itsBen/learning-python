# rock-paper-scissors

# rules
#
# rock beats scissors
# paper beats rock
# scissors beats paper

from class_player import Player
from class_game import Game

def main():

    # list rules

    human       = Player("Human", False)
    computer    = Player("Computer", False)

    game        = Game(3)
    game.addPlayer(human)
    game.addPlayer(computer)
    game.start()




    #human.choose()
    #computer.choose()

    # while True:
    #     human.choose()
    #     computer.make_random_choice()

    #     check_winner(human, computer)

    #     print()

    #     if(computer._wins == maxWins):
    #         winner = computer
    #         break

    #     if (human._wins == maxWins):
    #         winner = human
    #         break

    #     print("Next round")


    # print("Player {} won the game with {} wins and {} losses!".format(winner.name, winner.wins, winner.losses))


# def check_winner(human: Player, computer: Player):
#     if(human.choice == computer.choice):
#         print("tie")
#     elif(human.choice == "Rock") and (computer.choice == "Paper"):
#         computer.addWin()
#         human.addLoss()
#     elif(human.choice == "Rock") and (computer.choice == "Scissors"):
#         computer.addLoss()
#         human.addWin()
#     elif(human.choice == "Paper") and (computer.choice == "Scissors"):
#         computer.addWin()
#         human.addLoss()
#     elif(human.choice == "Paper") and (computer.choice == "Rock"):
#         computer.addLoss()
#         human.addWin()
#     elif(human.choice == "Scissors") and (computer.choice == "Rock"):
#         computer.addWin()
#         human.addLoss()
#     elif(human.choice == "Scissors") and (computer.choice == "Paper"):
#         computer.addLoss()
#         human.addWin()

#     else:
#         print("Unexpected")



main()