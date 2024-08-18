import random
from datetime import datetime, timedelta

separator = "-----------------------------------------------"

# opening text
def opening() -> None:
    print(f"Hi there! \n{separator} \
        \nI've generated a random 4 digit number for you. \
        \nLet's play a bulls and cows game. \
        \n{separator} \nEnter a number: \
        \n{separator}")

# generating random number
def generate_number() -> str:

    """Function for random number with unique digits, not starting with 0"""

    number = random.sample(range(10), 4)
    while number[0] == 0:
        number = random.sample(range(10), 4)
    return ''.join(map(str, number))

# checking the entered number
def validation(tip: str) -> tuple[bool, str]:

    """
    Function that ensures that the correct number is entered.

    Returns False if the specified value is not a number, starts with a zero, 
    is not a four-digit number, or is not specified with unique digits.
    """
    if not tip.isdigit():
        return False, "Enter four-digit NUMBER "
    if tip[0] == "0":
        return False, "Enter a four-digit number that doesn't begin with a zero"
    if int(tip) not in range(1000, 10000):
        return False, "Enter a four-digit number"
    if len(set(tip)) != 4:
        return False, f"Enter a four-digit number with unique digits"
    return True, ''

# evaluation of the tip
def evaluate(tip: str, number: str) -> tuple[int, int]:

    """
    Function compares tip and number, and returns a pair of numbers:

    Bulls indicates the number of characters in the correct position.
    Cows indicates the number of correct characters in the wrong position.
    """
    bulls = sum(x == y for x, y in zip(tip, number))
    cows = sum(x in number for x in tip) - bulls
    return bulls, cows

# function for correct grammar
def result_text(bulls: int, cows: int) -> None:
    bulls_text = "bull" if bulls == 1 else "bulls"
    cows_text = "cow" if cows == 1 else "cows"
    print(f"{bulls} {bulls_text}, {cows} {cows_text} \
          \n{separator}")

# listing the result
def attempt_text(attempts: int, elapsed_time: timedelta) -> None:
    attempts_text = "attempt " if attempts == 1 else "attempts" 
    elapsed_seconds = str(elapsed_time).split(".")[0] 
    print(f"Correct! You've guessed the right number \
          \nin {attempts} {attempts_text}! Your time is: {elapsed_seconds} \
          \n{separator}")

# evaluation of the game according to the number of attempts
def assessment(attempts: int) -> None:
    if attempts == 1:
        print(f"That was amazing! \n{separator}")
    if attempts > 1 and attempts < 5:
        print(f"That was really respectable! \n{separator}")
    if attempts > 5 and attempts < 10:
        print(f"Good job! \n{separator}")
    if attempts > 10 and attempts < 15:
        print(f"Not great not terrible. \n{separator}")
    if attempts > 15:
        print(f"It is not important to win, but to participate.. \n{separator}")

# history of the results of all the games played by the player
def show_history(history: list[tuple[int, timedelta]]) -> None:
    print(f"Your game history:")
    for i, (attempts, time_taken) in enumerate(history, start=1):
        attempts_text = "attempt" if attempts == 1 else "attempts"
        time_taken_text = str(time_taken).split(".")[0]
        print(f"Game {i:<2}| {attempts_text:<8}: {attempts:<3}|" \
              f"time: {time_taken_text:<10}")
    print(separator)

# main game function
def game(history: list[tuple[int, timedelta]]) -> None:
    opening()
    number = generate_number()
    print(number) # for working version only
    attempts = 0 # variable for computing attempts
    start_time = datetime.now() # start of timing
    while True:
        tip = input(">>> ")
        attempts += 1
        valid, message = validation(tip)
        if not valid:
            print(message)
            continue
        bulls, cows = evaluate(tip, number)
        result_text(bulls, cows)
        if bulls == 4:
            end_time = datetime.now() # end of timing
            elapsed_time = end_time - start_time # calculation of game duration
            attempt_text(attempts, elapsed_time)
            assessment(attempts)
            history.append((attempts, elapsed_time)) # saving the attempt to history
            break

# function to repeat the game
def play_again() -> bool:

    """
    Function that starts the game from the beginning.

    If answer is "yes" the game starts from beginning.
    If answer is "no" the game shuts down.
    """
    while True:
        answer = input("Do you want to play again? (yes/no): ").strip().lower()
        print(f"{separator}")
        if answer == "yes":
            return True
        elif answer == "no":
            return False
        else:
            print(f"Please enter 'yes' or 'no'. \n{separator}")

if __name__ == "__main__":
    history = [] # list for the history of games
    while True:
        game(history)
        show_history(history)
        if not play_again():
            print(f"Thanks for playing! Goodbye! \n{separator}")
            break