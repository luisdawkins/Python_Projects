"""
Date: 11/12/25

This program will randomly select a phrase from a predefined list.

1. Input
  a. Initialize predefined list
  b. Prompt user for question
2. Processing
  a. Generate random number
  b. Select phrase from list with random number
3. Output
  a. Print phrase
"""
import random

### Input
#Initialize predefined list
Valid_Answers_List = ["Yes - definitely.", "It is decidedly so.", "Without a doubt.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "My sources say no.", "Outlook not so good.", "Very doubtful."]

#Prompt user for question
input("Question:      ")

### Processing
#Generate random number
#Select phrase from list with random number
num = random.randint(0, len(Valid_Answers_List) - 1)

### Output
#Print phrase
print("Magic 8 Ball:  " + Valid_Answers_List[num])
