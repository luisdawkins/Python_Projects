"""
Date: 10/29/2025
This program asks the user for foreign currency amounts then calculates the total in USD

1. Inputs
  a. Initialze variables
  b. Foreign currency exchange rate
  c. Ask for foreign currency amounts
  d. Convert to integar variable
2. Processing
  a. Convert Foreign Currency into USD
  b. Add converted amount to USD total
3. Output
  a. Display final USD amount
"""

### Input
#Initialize Variables
Final_USD_Amount = 0.0

#Foreign Currency Exchange rates
Colombian_Pesos_Exchange_Rate = 0.00026
Peruvian_Soles_Exchange_Rate = 0.29
Brazilian_Reais_Exchange_Rate = 0.19 

#Ask for foreign currency amounts
#Convert to integar variable
Pesos_Total = int(input("What do you have left in pesos? "))
Soles_Total = int(input("What do you have left in soles? "))
Reais_Total = int(input("What do you have left in reais? "))

### Processing
#Convert Foreign Currency into USD
#Add converted amount to USD total
Final_USD_Amount = Pesos_Total * Colombian_Pesos_Exchange_Rate
Final_USD_Amount += Soles_Total * Peruvian_Soles_Exchange_Rate
Final_USD_Amount += Reais_Total * Brazilian_Reais_Exchange_Rate

### Output
print(Final_USD_Amount)
