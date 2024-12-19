import random

create_list_of_fruits = ["Mango", "Apple", "Banana", "Grapes", "Strawberry"]


word = random.choice(create_list_of_fruits)

guess = input("Enter a single letter: ")


if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")

print("You guessed....", word)