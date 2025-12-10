"""
Date: 12/9/25
This program allows a user to play Rock, Paper,Scissors with a computer.

1. Input
    a. Prompt User input
    b. Generate random computer value
2. Process
    a. Evaluate user input
    b. Determine Game Outcome
    c. Assign Player and Computer Icon
3. Output
    a. Print Final result
"""
import random

### Input
#Prompt User input
Player = int(input("""
===================
Rock Paper Scissors
===================

1) ✊
2) ✋
3) ✌️
Pick a number: """))

#Generate random computer value
Computer = random.randint(1, 3)

### Processing
print(Player, Computer)
#Evaluate user input
if Player == 1 and Computer == 1:
    #Determine Game Outcome
    Game_Outcome = "It's a tie!"
    Player_Icon, Computer_Icon = "✊", "✊"
elif Player == 2 and Computer == 2:
    Game_Outcome = "It's a tie!"
    Player_Icon, Computer_Icon = "✋", "✋"
elif Player == 3 and Computer == 3:
    Game_Outcome = "It's a tie!"
    Player_Icon, Computer_Icon = "✌️", "✌️"
elif Player == 1 and Computer == 3:
    Game_Outcome = "The player won!"
    Player_Icon, Computer_Icon = "✊", "✌️"
elif Player == 3 and Computer == 2:
    Game_Outcome = "The player won!"
    Player_Icon, Computer_Icon = "✌️", "✋"
elif Player == 2 and Computer == 1:
    Game_Outcome = "The player won!"
    Player_Icon, Computer_Icon = "✋", "✊"
elif Computer == 1 and Player == 3:
    Game_Outcome = "The Computer won!"
    Player_Icon, Computer_Icon = "✊", "✌️"
elif Computer == 3 and Player == 2:
    Game_Outcome = "The Computer won!"
    Player_Icon, Computer_Icon = "✌️", "✋"
elif Computer == 2 and Player == 1:
    Game_Outcome = "The Computer won!"
    Player_Icon, Computer_Icon = "✋", "✊"
else:
    Game_Outcome = "User input is not valid"

### Output
#Print final result
print(f"""

You chose: {Player_Icon}
CPU chose: {Computer_Icon}
{Game_Outcome}
""")
