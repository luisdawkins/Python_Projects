"""
Date: 12/1/25

This program asks the user set of questions to determine which of the following houses the user
will be sorted into.

1. Input
  a. Initialize Max House variables, House Score and Questions
  b. Ask the user a set of predefined questions
  c. Modify House Score
  d. Determine if output is invalid
2. Processing
  a. Determine which house should the user be sorted into
  b. Assign judgement status
  c. Determine which house has the highest
3. Output
  a. Print all house scores
"""

### Input
#Max house variables
Max_Score = 0
Max_Score_House = ""

#Initialize House Score
Hufflepuff_Score = 0
Slytherin_Score = 0
Ravenclaw_Score = 0
Gryffindor_Score = 0

#Initialize Questions
Question_One_String = """
Q1) Do you like Dawn or Dusk?
    1) Dawn
    2) Dusk

    """
Question_Two_String = """
Q2) When I’m dead, I want people to remember me as:
    1) The Good
    2) The Great
    3) The Wise
    4) The Bold

    """
Question_Three_String = """
Q3) Which kind of instrument most pleases your ear?
    1) The violin
    2) The trumpet
    3) The piano
    4) The drum

    """

#Ask the user a set of predefined questions
Question_One_Input = int(input(Question_One_String))

#Modify House Score
if Question_One_Input == 1:
    Gryffindor_Score += 1
    Ravenclaw_Score += 1
elif Question_One_Input ==2:
    Hufflepuff_Score += 1
    Slytherin_Score += 1
else:
    #Determine if output is invalid
    print("Wrong input")

Question_Two_Input = int(input(Question_Two_String))

if Question_Two_Input == 1:
    Hufflepuff_Score += 2
elif Question_Two_Input == 2:
    Slytherin_Score += 2
elif Question_Two_Input == 3:
    Ravenclaw_Score += 2
elif Question_Two_Input == 4:
    Gryffindor_Score += 2
else:
    print("Wrong input")

Question_Three_Input = int(input(Question_Three_String))

if Question_Three_Input == 1:
    Slytherin_Score += 4
elif Question_Three_Input == 2:
    Hufflepuff_Score += 4
elif Question_Three_Input == 3:
    Ravenclaw_Score += 4
elif Question_Three_Input == 4:
    Gryffindor_Score += 4
else:
    print("Wrong input")

#Determine which house has the highest

if Max_Score < Hufflepuff_Score:
    Max_Score = Hufflepuff_Score
    Max_Score_House = "Hufflepuff"

if Max_Score < Slytherin_Score:
    Max_Score = Slytherin_Score
    Max_Score_House = "Slytherin"

if Max_Score < Ravenclaw_Score:
    Max_Score = Ravenclaw_Score
    Max_Score_House = "Ravenclaw"

if Max_Score < Gryffindor_Score:
    Max_Score = Gryffindor_Score
    Max_Score_House = "Gryffindor"

### Output
#Print all House scores
print("Hufflepuff Score: ", Hufflepuff_Score)
print("Slytherin Score: ", Slytherin_Score)
print("Ravenclaw Score: ", Ravenclaw_Score)
print("Gryffindor Score: ", Gryffindor_Score)
print("\nThe house with the most points is: " + Max_Score_House)
