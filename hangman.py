import random
def choose_word():
    words=["python","code","alpha","game","programming"]
    return  random.choice(words) 
word=choose_word()
print("Welcome to Hangman!")
print("The word has", len(word), "letters.")
guessed_letters=[]
display_word = ["_"]*len(word)
def display_current_word(display_word):
    print("word:", " ".join(display_word))
display_current_word(display_word)    
incorrect_guesses=0
max_incorrect_guesses=6
def get_guess():
    guess = input("Guess a letter: ").lower()
    if len(guess) !=1 or not guess.isalpha():
        print("Please only enter single letter.")
        return None
    return guess
def already_guessed(guess,guessed_letters):
    return guess in guessed_letters
def reveal_letter(guess,word,display_word):
    for i in range(len(word)):
        if word[i]== guess:
            display_word[i]=guess
def record_guess(guess,guessed_letters):
    guessed_letters.append(guess)
def count_wrong_guess(incorrect_guesses):
    return incorrect_guesses+1

def display_hangman(incorrect_guesses):
    stages = [
        """
         +---+
         |   |
             |
             |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
             |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
         |   |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
        /|   |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
        /|\\  |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
        /|\\  |
        /    |
        =========
        """,
        """
         +---+
         |   |
         O   |
        /|\\  |
        / \\  |
        =========
        """
    ]

    print(stages[incorrect_guesses])
display_hangman(0)
while incorrect_guesses < max_incorrect_guesses and "_" in display_word:
    
    guess= get_guess()
    if guess is None:
        continue
    if already_guessed(guess,guessed_letters):
        print("You have guessed that letter.")
        continue
    
    record_guess(guess,guessed_letters)
        
    if guess in word:
        print("Good guess!")
        reveal_letter(guess,word,display_word)
    else:
        incorrect_guesses= count_wrong_guess(incorrect_guesses)
        print("Wrong guess!")
    display_current_word(display_word)
    display_hangman(incorrect_guesses)
    print("Guessed letters:",", ".join(guessed_letters))
    print("Incorrect guesses:", incorrect_guesses, "/", max_incorrect_guesses)
    print()
if "_" not in display_word:
    print("Congratulations! You guessed the word:", word)
else:
    print("Game over!")
    print("The word was:", word)
