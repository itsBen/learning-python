# rock-paper-scissors

# rules
#
# rock beats scissors
# paper beats rock
# scissors beats paper

from class_player import Player

def main():

    # list rules

    human       = Player("Human")
    computer    = Player("Computer")

    maxWins     = 3
    winner      = Player

    print("Playing until the first player has {} wins.".format(maxWins))

    while True:
        human.choose()
        computer.make_random_choice()

        check_winner(human, computer)

        print()

        if(computer._wins == maxWins):
            winner = computer
            break

        if (human._wins == maxWins):
            winner = human
            break

        print("Next round")


    print("Player {} won the game with {} wins and {} losses!".format(winner.name, winner.wins, winner.losses))


def check_winner(human: Player, computer: Player):
    if(human.choice == computer.choice):
        print("tie")
    elif(human.choice == "Rock") and (computer.choice == "Paper"):
        computer.addWin()
        human.addLoss()
    elif(human.choice == "Rock") and (computer.choice == "Scissors"):
        computer.addLoss()
        human.addWin()
    elif(human.choice == "Paper") and (computer.choice == "Scissors"):
        computer.addWin()
        human.addLoss()
    elif(human.choice == "Paper") and (computer.choice == "Rock"):
        computer.addLoss()
        human.addWin()
    elif(human.choice == "Scissors") and (computer.choice == "Rock"):
        computer.addWin()
        human.addLoss()
    elif(human.choice == "Scissors") and (computer.choice == "Paper"):
        computer.addLoss()
        human.addWin()

    else:
        print("Unexpected")

main()