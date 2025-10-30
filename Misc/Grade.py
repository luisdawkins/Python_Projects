"""
Date: 10/29/2025
This program determines generates a random number and determines if the grade is passing or failing

1. Inputs
  a. Initialize variables
  b. Generate random number
2. Processing
  a. Run grade determination equation
  b. Assign determination result
3. Output
  a. Display determination result
"""
import random

### Input
#Initialize Variables
Grading_Standard = 55

#Generate random number
Grade = random.randint(0, 100)

### Processing
#Run grade determination equation
#Assign determination result
if Grade >= Grading_Standard:
  Grade_Determination = 'You passed.'
else:
  Grade_Determination = 'You failed.'

### Output
print(Grade_Determination)
