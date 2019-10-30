from enum import Enum, auto

class Moves(Enum):
    ROCK    = auto()
    PAPER   = auto()
    SCISSOR = auto()

class Outcome(Enum):
    TIE  = auto()
    WON  = auto()
    LOST = auto()

MOVES_BEATEN_BY = {
    Moves.ROCK:     [Moves.SCISSOR],
    Moves.PAPER:    [Moves.ROCK],
    Moves.SCISSOR:  [Moves.PAPER]
}