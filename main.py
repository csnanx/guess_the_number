import random

def check_guess(answer, number):
    if answer == number:
        return True
    elif number < answer:
        print("Too low.")
    else:
        print("Too high.")

def check_difficulty(difficulty):
    if difficulty == "easy":
        return 10
    elif difficulty == "hard":
        return 5

def guess_the_number():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    chances = check_difficulty(difficulty)

    computer_choice = random.randint(1, 100)

    while chances:
        print(f"You have {chances} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        is_right = check_guess(computer_choice, guess)
        if is_right:
            chances = 0
            print("Congrats!\nYou are absolutely RIGHT.")
        else:
            chances -= 1
            if chances != 0:
                print("Guess again.")

    print(f"The right answer was: {computer_choice}")

play_again = "yes"

while play_again == "yes":
    guess_the_number()
    play_again = input("Do you want to play again? (yes/no): ").lower()
