"""
Author: Luis Dawkins
Date: 9/23/23
This program runs the famous hangman game for a user.

"""

import random
from Words import Word_List

#Retrieve secret word for Hangman game
def Get_Word():
    try:
        Word = random.choice(Word_List)
    except:
        print("There was an error with selecting a word.")
    else:
        return Word.upper()

#Main computations
def Play(Word):

    #Initialize key variables and set up the game
    Word_Completion = "_" * len(Word)
    Guessed = False
    Guessed_Letters = []
    Guessed_Words = []
    Tries = 6
    print("Let's play Hangman!")
    print(Display_Hangman(Tries))
    print(Word_Completion)
    print("\n")

    #Guessing section of Hangman
    while not Guessed and Tries > 0:
        Guess = input("Please guess a letter or word: ").upper()
        if len(Guess) == 1 and Guess.isalpha():
            if Guess in Guessed_Letters:
                print("You already guessed the letter", Guess)
            elif Guess not in Word:
                print(Guess, "is not in the word.")
                Tries -= 1
                Guessed_Letters.append(Guess)
            else:
                print("Good job,", Guess, "is in the word!")
                Guessed_Letters.append(Guess)
                Word_as_List = list(Word_Completion)
                indices = [i for i, Letter in enumerate(Word) if Letter == Guess]
                for index in indices:
                    Word_as_List[index] = Guess
                Word_Completion = "".join(Word_as_List)
                if "_" not in Word_Completion:
                    Guessed = True
        elif len(Guess) == len(Word) and Guess.isalpha():
            if Guess in Guessed_Words:
                print("You already guessed the word", Guess)
            elif Guess != word:
                print(Guess, "is not the word.")
                Tries -= 1
                Guessed_Words.append(Guess)
            else:
                Guessed = True
                Word_Completion = Word
        else:
            print("Not a valid guess.")
        print(Display_Hangman(Tries))
        print(Word_Completion)
        print("\n")
    if Guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + Word + ". Maybe next time!")

#Display
def Display_Hangman(Tries):
    Stages = [  # final state: head, torso, both arms, and both legs
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / \
           -
        """,
        # head, torso, both arms, and one leg
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / 
           -
        """,
        # head, torso, and both arms
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |      
           -
        """,
        # head, torso, and one arm
        """
           --------
           |      |
           |      O
           |     \|
           |      |
           |     
           -
        """,
        # head and torso
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        # head
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        # initial empty state
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return Stages[Tries]

def Main():
    Word = Get_Word()
    Play(Word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        Word = Get_Word()
        Play(Word)


if __name__ == "__main__":
    Main()
