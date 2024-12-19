import random

def create_list_of_fruits():
    """Returns a list of fruit names."""
    return ["Mango", "Apple", "Banana", "Grapes", "Strawberry"]

def select_random_word(word_list):
    """Selects and returns a random word from the given list."""
    return random.choice(word_list)

def is_valid_guess(guess):
    """
    Validates the user's input.
    Returns True if the input is a single alphabetical character; otherwise, False.
    """
    return len(guess) == 1 and guess.isalpha()

def play_guessing_game():
    """Runs the fruit guessing game."""
    fruit_list = create_list_of_fruits()
    chosen_word = select_random_word(fruit_list)
    
    guess = input("Enter a single letter: ")
    
    if is_valid_guess(guess):
        print("Good guess!")
    else:
        print("Oops! That is not a valid input.")
    
    print("The chosen word was:", chosen_word)

if __name__ == "__main__":
    play_guessing_game()
