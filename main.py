print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
    chances = 10
elif difficulty == "hard":
    chances = 5

print(chances)