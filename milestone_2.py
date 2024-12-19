import random

word_list = ["Mango", "Apple", "Banana", "Grapes", "Strawberry"]


word = random.choice(word_list)

guess = input("Enter a single letter: ")


if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")

print("You guessed....", word)