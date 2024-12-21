import random

class Hangman:

    def __init__(self, secret_word, max_lives=5):
        self.secret_word = secret_word
        self.remaining_lives = max_lives
        self.current_guess_state = ['_' for _ in self.secret_word]  
        self.remaining_unique_letters = len(set(self.secret_word))  
        self.guessed_letters = []  

    def process_guess(self, guessed_letter):
        if guessed_letter in self.guessed_letters:
            print(f"You already guessed '{guessed_letter}'. Try a different letter.")
            return

        self.guessed_letters.append(guessed_letter)

        if guessed_letter in self.secret_word:
            print(f"Good guess! '{guessed_letter}' is in the word.")
            for index, character in enumerate(self.secret_word):
                if character == guessed_letter:
                    self.current_guess_state[index] = guessed_letter
            print(f"Current word: {' '.join(self.current_guess_state)}")

            self.remaining_unique_letters -= 1
        else:
            self.remaining_lives -= 1
            print(f"Wrong guess. You have {self.remaining_lives} lives left.")
            print(f"Current word: {' '.join(self.current_guess_state)}")

def start_game(word_list):
    max_lives = 5
    game_instance = Hangman("pearl", max_lives)

    while True:
        if game_instance.remaining_lives == 0:
            print("You lost! The word was:", game_instance.secret_word)
            break
        elif game_instance.remaining_unique_letters > 0:
            player_guess = input("Guess a letter: ").lower()
            if len(player_guess) == 1 and player_guess.isalpha():
                game_instance.process_guess(player_guess)
            else:
                print("Invalid input. Please enter a single alphabetical character.")
        else:
            print("Congratulations. You won the game!")
            print("The word was:", game_instance.secret_word)
            print(f"You finished the game with {game_instance.remaining_lives} lives remaining.")
            break

if __name__ == "__main__":
    word_list = ["pearl"]
    start_game(word_list)
