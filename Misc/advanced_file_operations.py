"""
Date: 1/10/25

This program attempts to read and output the contents of a csv file. If unable to do so,
it will create the csv file for future use.

1. Input
    a. Define file path
    b. Define data
2. Processing
    a. Create try/except block
    b. Configure file handling method within try block
    c. Iterate through every row within csv file
    d. Configure write method within except block
    e. Write key information to csv file
3. Output
    a. Print each row of information
    b. Print confirmation message upon successful or failed execution

"""
import csv

### Input
#Define file path
file_path = "packing_list.csv"
#Define Data
data = [
    ['Item', 'Quantity'],
    ['Blender', 2],
    ['Posters', 30],
    ['Shoes', 2]
]

### Processing
#Create try/except block
try:
    #Configure file handling method within try block
    #the encoding arguement is to prevent configuration issues
    with open(file_path, 'r', encoding='utf-8') as file:
        #Configure file object
        csv_reader = csv.reader(file)
        #Iterate through every row within csv file
        for row in csv_reader:
            #Print each row of information
            print(row)

    print("\nData has been successfully written.")
except FileNotFoundError:
    #Print confirmation message upon successful or failed execution
    print("Packing list file not found. Creating a new one.")
    #Configure write method within except block
    with open(file_path, 'w', newline="") as file:
        csv_writer = csv.writer(file)
        for row in data:
            #Write key information to csv file
            csv_writer.writerow(row)
