# Python Hangman Game

## About the project

This is a simple text-based game developed using Python as part of my CodeAlpha Python Programming Internship.

In this game, the computer randomly selects a word, and the player tries to guess it one letter at a time. The player can make up to six incorrect guesses before the game ends.

## How to Play

1. Run the `hangman.py` file.
2. The program randomly selects one word from five predefined words.
3. Guess one letter at a time.
4. Correct guesses reveal the letter in the word.
5. Incorrect guesses increase the counter and update the Hangman drawing.
6. You can make up to six incorrect guesses.
7. Win by revealing all the letters before reaching the limit.

## Features

- Random word selection using Python's random module.
- Input validation.
- Detection of repeated guesses.
- Tracking of guessed letters.
- ASCII Hangman drawings.
- Win and lose messages.

## Python Concepts Used

- Variables and data types
- Lists and strings
- Functions
- Loops and conditional statements
- User input and output
- The random module

## How to Run

Make sure Python 3 is installed.

Run the following command in your terminal:

```bash
python hangman.py
```

If that command doesn't work, try:

```bash
python3 hangman.py
```

## Sample Output

The following is an example of how the game might look. The actual word and output may differ because the word is selected randomly.

```text
Welcome to Hangman!
The word has 6 letters.

word: _ _ _ _ _ _

         +---+
         |   |
             |
             |
             |
        =========

Guess a letter: p

Good guess!
word: p _ _ _ _ _

         +---+
         |   |
             |
             |
             |
        =========

Guessed letters: p
Incorrect guesses: 0 / 6
```

## Hangman Drawing

The Hangman drawing changes as the player makes incorrect guesses.

```text
Stage 1: No incorrect guesses

         +---+
         |   |
             |
             |
             |
        =========

Stage 2: One incorrect guess

         +---+
         |   |
         O   |
             |
             |
        =========

Stage 3: Two incorrect guesses

         +---+
         |   |
         O   |
         |   |
             |
        =========

Stage 4: Three incorrect guesses

         +---+
         |   |
         O   |
        /|   |
             |
        =========

Stage 5: Four incorrect guesses

         +---+
         |   |
         O   |
        /|\  |
             |
        =========

Stage 6: Five incorrect guesses

         +---+
         |   |
         O   |
        /|\  |
        /    |
        =========

Stage 7: Six incorrect guesses

         +---+
         |   |
         O   |
        /|\  |
        / \  |
        =========
```

## Game Results

If the player guesses the word correctly:

```text
Congratulations! You guessed the word: python
```

If the player reaches six incorrect guesses:

```text
Game over!
The word was: python
```