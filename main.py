from random import randint
from os import system, name


guess_parameters = input("Input guess parameter: ")
guess_tally = 0
correct_guess = 0


# Clears the terminal
def clear():
    # Windows check
    if name == 'nt':
        _ = system('cls')
    # Unix check
    else:
        _ = system('clear')


# Loops through until user stops
while True:
    user_num = input(f"\nInput guess between 1 and {guess_parameters}: ")


    def guesser(num):
        random_num = randint(1, int(guess_parameters))
        # \033 changes text color
        if int(num) == random_num:
            print("\nYou guessed" + "\033[1;32m correctly!\033[0;0m " + "\nThe number was " + num)
            return True
        else:
            print("\nyour guess was" + "\033[1;31m wrong\033[0;0m " + ":(")
            print(f"Your guess: {num}\nCorrect number: {random_num}")
            return False


    # Changes leaderboard tally
    guess_tally += 1
    if guesser(user_num):
        correct_guess += 1

    print("\n************************ Leader Board ************************")
    print("Total guesses: " + str(guess_tally))
    print("Total correct guesses: " + str(correct_guess))
    print("**************************************************************\n")

    # checks if user want to play again
    while True:
        answer = str(input('Run again? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("invalid input.")
    if answer == 'y':
        clear()
        continue
    else:
        print("Goodbye")
        break
