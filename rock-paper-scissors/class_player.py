import random
import sys
from shared import Moves

class Player:

    def __init__(self, name: str, isHuman: bool):
        # public variables

        # private variables
        self._name      = name
        self._isHuman   = isHuman
        self._wins      = None
        self._losses    = None


    def addWin(self):
        self._wins += 1
        print("Player: {} won! Now has {} win(s) and {} loss(es)!".format(self._name, self._wins, self._losses))

    def addLoss(self):
        self._losses += 1
        print("Player: {} lost! Now has {} win(s) and {} loss(es)!".format(self._name, self._wins, self._losses))


    def _makeRandomChoice(self):
        return random.choice(list(Moves))

    def choose(self):

        if(self._isHuman == True):
            print("Press R for Rock.")
            print("Press P for Paper.")
            print("Press S for Scissors.")
            print("Press Q to quit.")

            humanInput = input()

            if(humanInput == "r"):
                self.choice = Moves.ROCK
            elif(humanInput == "p"):
                self.choice = Moves.PAPER
            elif(humanInput == "s"):
                self.choice = Moves.SCISSOR
            elif(humanInput == "q"):
                sys.exit(0)
            else:
                self.choose()
        else:
            self.choice = self._makeRandomChoice()

        print("Player: {} chose: {}".format(self._name, self.choice))
