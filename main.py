import random
import replit
from words import word_list


def get_valid_word():
    word = random.choice(word_list)
    return word.upper()


def start(word):
    current_word = "_" * len(word)
    attempts = 6
    letters_guessed = []
    words_guessed = []
    guessed = False
    print("Welcome to Hangman!\nLet's Begin :)")
    print(Hangman(attempts))
    print(current_word)
    print()
    while not guessed and attempts > 0:
        guess = input("Guess a letter or a word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in letters_guessed:
                print("You already guessed that letter. Please try again.", guess)
            elif guess not in word:
                print(guess, "is not in this word.")
                attempts -= 1
                letters_guessed.append(guess)
            else:
                print("Nice,", guess, "is in this word.")
                letters_guessed.append(guess)
                word_as_list = list(current_word)
                x = [i for i, letter in enumerate(word) if letter == guess]
                for index in x:
                    word_as_list[index] = guess
                current_word = "".join(word_as_list)
                if "_" not in current_word:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in words_guessed:
                print("You already guessed that word.", guess)
            elif guess != word:
                print(guess, "is not the correct word.")
                attempts -= 6
                words_guessed.append(guess)
            else:
                guessed = True
                current_word = word
        else:
            print("Not a valid guess.")
        print(Hangman(attempts))
        print(current_word)
        print()
    if guessed:
        print("Well done, you guessed the word. You win!")
        print()
    else:
        print("Sadly, you ran out of attempts. The word was " + word + ".")
        print()


def Hangman(attempts):
    stages = [
                """
                   __________
                   |/       |
                   |        O
                   |       \\|/
                   |        |
                   |       / \\
                   |
                 -----
                """,
                
                """
                   __________
                   |/       |
                   |        O
                   |       \\|/
                   |        |
                   |       /
                   |
                 -----
                """,
                
                """
                   __________
                   |/       |
                   |        O
                   |       \\|/
                   |        |
                   |
                   |
                 -----
                """,
              
                """
                   __________
                   |/       |
                   |        O
                   |       \\|
                   |        |
                   |
                   |
                 -----
                """,
                
                """
                   __________
                   |/       |
                   |        O
                   |        |
                   |        |
                   |
                   |
                 -----
                """,
                
                """
                   __________
                   |/       |
                   |        O
                   |    
                   |
                   |
                   |
                 -----
                """,
                
                """
                   __________
                   |/       |
                   |      
                   |    
                   |
                   |
                   |
                 -----
                """
    ]
    return stages[attempts]


data = {"yes":1}

def GameEnded():
    word = get_valid_word()
    start(word)
    while input("Want to play again?" + "  yes " + " or " + " no  ") == "yes":
      if data["yes"] == 1:
        replit.clear()
        word = get_valid_word()
        start(word)
    else: 
      print()
      print("Thanks for playing see you next time.")

GameEnded()

