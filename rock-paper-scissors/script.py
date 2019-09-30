# rock-paper-scissors

# rules
#
# rock beats scissors
# paper beats rock
# scissors beats paper

import sys
import random


class Player:

    wins    = 0
    losses  = 0
    choice  = ""
    name    = ""

    options = ["Rock", "Paper", "Scissors"]

    def __init__(self, name):
        self.name = name

    def addWin(self):
        self.wins += 1
        print("Player: {} won! Now has {} win(s) and {} loss(es)!".format(self.name, self.wins, self.losses))

    def addLoss(self):
        self.losses += 1
        print("Player: {} lost! Now has {} win(s) and {} loss(es)!".format(self.name, self.wins, self.losses))

    def make_random_choice(self):
        choice = random.choice(self.options)

        print("Player: {} chose: {}".format(self.name, choice))

        self.choice = choice

    def choose(self):
        print("Press R for Rock.")
        print("Press P for Paper.")
        print("Press S for Scissors.")
        print("Press Q to quit.")

        humanInput = input().lower()
        choice = ""

        if(humanInput == "r"):
            choice = self.options[0] # returns "Rock"
        elif(humanInput == "p"):
            choice = self.options[1] # returns "Paper"
        elif(humanInput == "s"):
            choice = self.options[2] # returns "Scissors"
        elif(humanInput == "q"):
            sys.exit(0)
        else:
            self.choose()

        print("Player: {} chose: {}".format(self.name, choice))
        self.choice = choice

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

        if(computer.wins == maxWins):
            winner = computer
            break

        if (human.wins == maxWins):
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