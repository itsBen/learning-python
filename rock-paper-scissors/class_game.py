from shared import Moves, Outcome, MOVES_BEATEN_BY
from class_player import Player

class Game:
    def __init__(self, number_of_rounds: int, players: list(Player)):
        self._number_of_rounds   = number_of_rounds
        self._players            = players


    def start(self):
        for round in range(self._number_of_rounds):
            print(round)


    def end(self):
        pass


class Round:

    def __init__(self, round_number: int, players: list(Player)):
        self._round_number   = round_number
        self._players        = players

        self._start()


    def _start(self):
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
