"""
Author: Luis Dawkins
Date: 9/23/23
This program runs the famous hangman game for a user.

1. Input
    Retrieve secret word from list
    test for errors
    Format secret word
2. Processing
    Set up graphical interface for user
    Initialize key variables for main computations
    Test guessed character
    Respond according to Hangman rules and logic
    Decide if game was won or lost
    Offer to play again
3. Output
    Display results of game in command prompt
    Display results in a text file including secret word
4. Execute
    Actiavte all necessary code and functions

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

def Outputing_Results(Answer):
    File = open("Winner.txt", "w")
    File.write(f"Congrats you won. Your word was {Answer}")
    File.close()

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
        #Handle already guessed letters and successful valid inputs
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

        #Handle guessing the whole word
        elif len(Guess) == len(Word) and Guess.isalpha():
            if Guess in Guessed_Words:
                print("You already guessed the word", Guess)
            elif Guess != Word:
                print(Guess, "is not the word.")
                Tries -= 1
                Guessed_Words.append(Guess)
            else:
                Guessed = True
                Word_Completion = Word
        else:
            print("Not a valid guess.")

        #Update graphical user interface according to the game results
        print(Display_Hangman(Tries))
        print(Word_Completion)
        print("\n")

    if Guessed:
        print("Congrats, you guessed the word! You win!")
        Outputing_Results(Word)
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

#Main script to execute all code
def Main():
    Word = Get_Word()
    Play(Word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        Word = Get_Word()
        Play(Word)

if __name__ == "__main__":
    Main()
