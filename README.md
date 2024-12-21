# Fruit (milestone_2.py) & Word Guessing Games (milestone_3.py)

## Table of Contents

1. [Description]
2. [Installation Instructions]
3. [Usage Instructions]
4. [File Structure]
5. [License]

---

## Description

### Fruit Guessing Game (milestone_2.py)

The **Fruit Guessing Game** (implemented in `milestone_2.py`) is a beginner-friendly Python project designed to demonstrate:

- How to work with Python lists to store a collection of data (e.g., fruit names).
- Using the `random` module to select a random item from a list.
- Validating user input with Python's built-in functions.

**What It Does**:

- Prompts the user to enter a single letter.
- Validates the input to ensure it is exactly one alphabetical character.
- Provides feedback on the validity of the input.

**Aim of the Project**:

- Practice Python basics like lists, loops, and input validation.
- Build a foundational understanding of user interaction in Python.

---

### Word Guessing Game (milestone_3.py)

The **Word Guessing Game** (implemented in `milestone_3.py`) is an interactive game where the user must guess a letter in a predefined word.

**What It Does**:

- Continuously prompts the user to guess a letter until they enter valid input.
- Validates the input to ensure it is a single alphabetical character.
- Checks if the guessed letter is in the word and provides appropriate feedback.

**Aim of the Project**:

- Understand modular programming by splitting logic into reusable functions (`check_guess` and `ask_for_input`).
- Practice validation and conditionals for user input.
- Learn how to check for the presence of characters in strings.

**What I Learned from Both Projects**:

- How to use Python’s `random.choice` to select items from a list.
- Effective input validation using `len()` and `.isalpha()`.
- How to create and call functions for modular programming.
- Structuring Python scripts for readability and reusability.

---

## Installation Instructions

1. Ensure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/).
2. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/ojbilly/guessing-games.git
   ```

# Hangman Game (milestone_4.py)

## Table of Contents

1. [Description]
2. [Installation Instructions]
3. [Usage Instructions]
4. [File Structure]
5. [License]

---

## Description

The **Hangman Game** is a beginner-friendly Python project that demonstrates how to:

- Use classes to encapsulate game logic.
- Handle user input validation.
- Implement a simple game loop with winning and losing conditions.

### What It Does

- Initializes the game with a word ("pearl") to be guessed.
- Prompts the user to guess one letter at a time.
- Validates the input to ensure it is a single alphabetical character.
- Updates the game state based on correct or incorrect guesses.
- Ends the game when the word is fully guessed or the player runs out of lives.

### Aim of the Project

The aim of this project is to:

- Practice Python programming concepts such as classes, loops, and input validation.
- Understand modular programming by splitting functionality into reusable methods.
- Build a simple yet engaging console-based game.

### What I Learned

- How to use classes and methods effectively to structure a project.
- Input validation techniques for interactive programs.
- How to build a game loop with user-defined end conditions.

---

## Installation Instructions

1. Ensure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/).
2. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/hangman-game.git
   ```
3. Navigate to the project directory:
   ```bash
   cd hangman-game
   ```

---

## Usage Instructions

1. Run the `milestone_4.py` script:
   ```bash
   python milestone_4.py
   ```
2. Follow the prompts to guess letters in the word "pearl".
3. Keep guessing until:
   - You guess all the letters correctly and win, or
   - You run out of lives and lose the game.

---

## File Structure

```plaintext
hangman-game/
├── milestone_4.py      # Hangman Game script
├── README.md           # Documentation for the game
```

---

## License

This project was created by Osaze Omoruyi and is free to use. You are welcome to modify and distribute this software as you see fit.

---

# Hangman Game (milestone_5.py)

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [License](#license)

## Description

The **Hangman Game** is a simple command-line implementation of the classic word-guessing game. The aim of the project is to provide a fun way to practice programming concepts such as object-oriented programming (OOP), user input validation, and control flow.

### Features:

- Players attempt to guess the hidden word by suggesting letters.
- Players have a limited number of lives (attempts).
- Feedback is provided for each guess, indicating whether the letter is in the word and showing progress.
- The game concludes with a win or loss message depending on whether the player guesses the word within the allotted lives.

### Key Learnings:

- How to structure a Python program using classes and methods.
- Handling user input and validating data.
- Implementing game logic and maintaining state across multiple rounds.
- Using lists and sets for efficient data handling.

## Installation

1. Ensure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. Clone this repository or copy the `Hangman` code into a file named `hangman.py`.
3. Open a terminal or command prompt and navigate to the directory containing the file.

## Usage

1. Run the program using the following command:
   ```bash
   python hangman.py
   ```
2. The game will prompt you to guess a letter.
3. Enter one alphabetical character at a time. The program will inform you if the letter is correct, already guessed, or not in the word.
4. Continue guessing until you either guess the word correctly or run out of lives.
5. The program will display a win or loss message at the end.

### Example Gameplay:

```
Guess a letter: p
Good guess! 'p' is in the word.
Current word: p _ _ _ _

Guess a letter: a
Good guess! 'a' is in the word.
Current word: p _ a _ _

Guess a letter: z
Wrong guess. You have 4 lives left.
Current word: p _ a _ _

... (continue guessing) ...
```

## File Structure

```
.
├── hangman.py   # The main script containing the Hangman game code
```

## License

This project was created by Osaze Omoruyi and is free to use. You are welcome to modify and distribute this software as you see fit.

---

Happy coding and have fun playing Hangman!
