"""
Date: 10/31/25
This program determines the ph level of a variable provided by the user.

1. Input
  a. Prompt user for numeric variable
  b. Normalize input
2. Processing
  a. Determine ph level
  b. Assign value to Acidic Level output variable
3. Output
  a. Print Acidic Level Output
"""

### Input
# Prompt user for numeric variable
Working_User_Input = int(input("Please input a number between 0 and 14 "))

### Processing
# Determine ph level
if Working_User_Input > 7:
  #Assign value to Acidic Level output variable
  Final_PH_Level_Output = "Basic"
elif Working_User_Input < 7:
  Final_PH_Level_Output = "Acidic"
else :
  Final_PH_Level_Output = "Neutral"

### Output
# Print Acidic Level Output
print(Final_PH_Level_Output)
