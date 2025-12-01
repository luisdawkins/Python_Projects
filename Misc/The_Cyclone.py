"""
Date: 12/1/25

This program prompts the user for height and credit values then determines
if they can enjoy the ride.

Significant Constants
  a. Height and Credit requirements
1. Input
  a. Prompt user for Height and Credit Value
  b. Convert values from string to integars
2. Processing
  a. Determine if criteria is met to pass the entry system
  b. Assign ride status variable
3. Output.
  a. Print ride status variable
"""

### Significant Constants
#Height and Credit requirements
Height_Requirement = 137
Credit_Requirement = 10

### Input
#Prompt user for Height and Credit Value
Height_Input = int(input("What is your height in cm?: "))
Credit_Input = int(input("How many credits do you have: "))
Ride_Status = "You have not met the requirements"

### Processing
#Determine if criteria is met to pass the entry system
if Height_Input >= Height_Requirement and Credit_Input >= Credit_Requirement:
  #Assign ride status variable
  Ride_Status = "Enjoy the ride!"
elif Height_Input < Height_Requirement and Credit_Input >= Credit_Requirement:
  Ride_Status = "You are not tall enough to ride."
elif Height_Input >= Height_Requirement and Credit_Input < Credit_Requirement:
  Ride_Status = "You don't have enough credits."
else:
  Ride_Status = "You have not met either requirement."

### Output
#Print ride status variable
print(Ride_Status)
