class Game:

    def __init__(self, number_of_rounds: int, players):
        self._number_of_rounds   = number_of_rounds
        self._players            = players

    def start(self):

        for round in range(self._number_of_rounds):
            print(round)

    def end(self):
        pass


class Round:

    def __init__(self, round_number: int, players):
        self._round_number   = round_number
        self._players        = players

    def start(self):
        for player in self._players:
            player.choose()

    def end(self):
        pass

class Rules:
    def apply(players):
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