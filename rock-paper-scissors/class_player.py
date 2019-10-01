import random
import sys

class Player:

    options = ["Rock", "Paper", "Scissors"]

    def __init__(self, name: str, isHuman: bool):
        self._name      = name
        self._isHuman   = False
        self._wins      = None
        self._losses    = None

    def addWin(self):
        self._wins += 1
        print("Player: {} won! Now has {} win(s) and {} loss(es)!".format(self._name, self._wins, self._losses))

    def addLoss(self):
        self._losses += 1
        print("Player: {} lost! Now has {} win(s) and {} loss(es)!".format(self._name, self._wins, self._losses))

    def _makeRandomChoice(self):
        return random.choice(self.options)

    def choose(self):
        choice = None

        if(self._isHuman == True):
            print("Press R for Rock.")
            print("Press P for Paper.")
            print("Press S for Scissors.")
            print("Press Q to quit.")

            humanInput = input().lower()

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
        else:
            choice = self._makeRandomChoice()

        print("Player: {} chose: {}".format(self._name, choice))
        self.choice = choice
