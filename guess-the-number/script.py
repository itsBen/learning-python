import random

randomNumber = random.randint(1,21)
#print(randomNumber)

print("Guess the number, good luck :)")

def is_guess_right(guessedNumber: int):
    if(guessedNumber == randomNumber):
        return True
    else:
        return False

def guess_is_too_high(guessedNumber: int):
    if(guessedNumber > randomNumber):
        print("Your guessed number is too high, guess again!")
        return True
    else:
        return False

def guess_is_too_low(guessedNumber: int):
    if(guessedNumber < randomNumber):
        print("Your guessed number is too low, guess again!")
        return True
    else:
        return False

def main():
    guessedNumber = int(input("Please enter your guess: "))
    print(guessedNumber)

    if(is_guess_right(guessedNumber)):
        print("You win")
    else:
        if (guess_is_too_high(guessedNumber)) or (guess_is_too_low(guessedNumber)):
            main()

main()