from random import randint


logo = """
   _   _   _   _   _     _   _   _     _   _   _   _   _   _  
  / \ / \ / \ / \ / \   / \ / \ / \   / \ / \ / \ / \ / \ / \ 
 ( G | u | e | s | s ) ( t | h | e ) ( n | u | m | b | e | r )
  \_/ \_/ \_/ \_/ \_/   \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/ \_/ 
"""
HARD_TURNS = 5
EASY_TURNS = 10


def guess_the_number():
    print("Welcome to the Number Guessing Game!\n"
           "I'm thinking of a number between 1 and 100.")
    guessed_number = randint(1, 100)
    def choose_difficulty_level():
        difficulty_level = input(
            "Choose a difficulty. Type 'easy' or 'hard': "
        ).lower()
        if difficulty_level == "easy":
            return EASY_TURNS
        elif difficulty_level == "hard":
            return HARD_TURNS
        else:
            print("You've typed in a wrong word")
            return choose_difficulty_level()
    attempts = choose_difficulty_level()
    for attempt in range(attempts):
        print(f"You have {attempts-attempt} remaining to guess the number")
        your_guess = int(input("Make a guess: "))
        if your_guess == guessed_number:
            print(f"Congrats! You win! The answer was {guessed_number}")
            return
        elif your_guess < guessed_number:
            print("Too low")
        else:
            print("Too high")
    print("You've run out of guesses. You lose.")


if __name__ == "__main__":
    guess_the_number()

