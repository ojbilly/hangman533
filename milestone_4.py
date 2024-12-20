import random

class Hangman:

    def __init__(self, word, num_lives=5):
        """
        Initializes the attributes for the Hangman game.

        Parameters:
        - word (str): The word to guess.
        - num_lives (int): The number of lives the player has. Default is 5.
        """
        self.word = word
        self.num_lives = num_lives
        self.word_guessed = ['_' for _ in self.word]  # Initialize with underscores
        self.num_letters = len(set(self.word))  # Count of unique letters to guess
        self.list_of_guesses = []  # Keep track of guessed letters

    def guess_letter(self, letter):
        """
        Handles the user's guess.

        Parameters:
        - letter (str): The letter guessed by the user.
        """
        if letter in self.list_of_guesses:
            print(f"You already guessed '{letter}'. Try a different letter.")
            return

        self.list_of_guesses.append(letter)

        if letter in self.word:
            print(f"Good guess! '{letter}' is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    self.word_guessed[i] = letter
            print(f"Current word: {''.join(self.word_guessed)}")

            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Wrong guess. You have {self.num_lives} lives left.")
            print(f"Current word: {''.join(self.word_guessed)}")

# Main game loop
if __name__ == "__main__":
    # Initialize the game with the word "pearl"
    word = "pearl"
    hangman_game = Hangman(word)

    print("Welcome to Hangman!")
    print(f"Word to guess: {''.join(hangman_game.word_guessed)}")

    while hangman_game.num_lives > 0 and hangman_game.num_letters > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single alphabetical character.")
            continue

        hangman_game.guess_letter(guess)

    if hangman_game.num_letters == 0:
        print(f"Congratulations! You guessed the word: {hangman_game.word}")
    else:
        print("Game over! You've run out of lives.")
        print(f"The word was: {hangman_game.word}")
