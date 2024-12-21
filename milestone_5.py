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
            print(f"Current word: {' '.join(self.word_guessed)}")

            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Wrong guess. You have {self.num_lives} lives left.")
            print(f"Current word: {' '.join(self.word_guessed)}")

def play_game(word_list):
    """
    Starts the Hangman game with the given word list.

    Parameters:
    - word_list (list): List of words for the game.
    """
    num_lives = 5
    game = Hangman("pearl", num_lives)

    while True:
        if game.num_lives == 0:
            print("You lost! The word was:", game.word)
            break
        elif game.num_letters > 0:
            guess = input("Guess a letter: ").lower()
            if len(guess) == 1 and guess.isalpha():
                game.guess_letter(guess)
            else:
                print("Invalid input. Please enter a single alphabetical character.")
        else:
            print("Congratulations. You won the game!")
            print("The word was:", game.word)
            break

if __name__ == "__main__":
    word_list = ["pearl"]
    play_game(word_list)
