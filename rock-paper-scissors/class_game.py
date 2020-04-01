from shared import Moves, Outcome, MOVES_BEATEN_BY
from class_player import Player


#: list(Player)

class Game:
    def __init__(self, number_of_rounds: int):
        # public variables

        # private variables
        self._number_of_rounds  = number_of_rounds
        self._rounds            = []
        self._players           = []

        print("Playing for {} round(s).".format(number_of_rounds))

        self._init_rounds()


    def _init_rounds(self):
        for round_number in range(self._number_of_rounds):
            # start round with 1
            round_number += 1

            round = Round(round_number, self._players)

            self._rounds.append(round)


    def addPlayer(self, player):
        self._players.append(player)


    def start(self):
        # TODO: check if players are added

        for round in self._rounds:
            print(round.round_number)
            round.start()


    def end(self):
        pass


class Round:

    def __init__(self, round_number: int, players):
        # public variables
        self.round_number   = round_number

        # private variables
        self._players       = players


    def start(self):
        for player in self._players:
            player.choose()

    def _end(self):
        pass

    def _determine_round_winner(self, player_move: Moves, computer_move: Moves):
        if computer_move in MOVES_BEATEN_BY[player_move]:
            return Outcome.WON
        elif player_move in MOVES_BEATEN_BY[computer_move]:
            return Outcome.LOST
        else:
            return Outcome.TIE
