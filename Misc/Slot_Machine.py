# Write code below 💖
"""
Date: 12/14/2025

This program selects from a list of items and outputs three. If the
right criteria is met the user wins the game.

Significant Constants
  a. Items list
1. Input
  a. Initialize verification flag variable
  b. Prompt user to play again after while loop
2. Processing
  a. While Loop
  b. Randomly select three items
  c. Determine game outcome
  d. Configure final print result
3. Output
  a. Output final result
"""
import random

### Significant Constants
#Items list
symbols = ['🍒',' 🍇', '🍉', '7️⃣']

#Initialize variable
verification_flag = True

### Processing
#While Loops
while verification_flag:
  #Randomly select three items
  results = random.choices(symbols, k=3)

  #Determine game outcome
  if results[0] == "7️⃣" and results[1] == "7️⃣" and results[2] == "7️⃣":
    game_outcome = "Jackpot! 💰"
  else:
    game_outcome = "Thanks for playing!"
  
  #Configure final print result
  final_output = f"""
{results[0]} | {results[1]} | {results[2]}
{game_outcome}
  """

  ### Output
  #Output final result
  print(final_output)

  ### Input
  #Prompt user to play again after while loop
  user_input = input("Would you like to play again? 'Y' or 'N' ")
  if user_input == "Y":
    verification_flag = True
  else:
    verification_flag = False



