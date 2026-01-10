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
    d. Print each row of csv file
    e. Configure write method within except block
    f. Write key information to csv file
3. output
    a. Print each row of information
    b. Print confirmation message upon successful or failed execution

"""
import csv

file_path = "packing_list.csv"
data = [
    ['Item', 'Quantity'],
    ['Blender', 2],
    ['Posters', 30],
    ['Shoes', 2]
]

try:
    #the encoding parameter is to prevent configuration issues
    with open(file_path, 'r', encoding='utf-8') as file:
        #Configure file object
        csv_reader = csv.reader(file)
        #iterate through every row of csv file
        for row in csv_reader:
            print(row)

    print("\nData has been successfully written.")
except FileNotFoundError:
    print("Packing list file not found. Creating a new one.")
    with open(file_path, 'w', newline="") as file:
        csv_writer = csv.writer(file)
        for row in data:
            csv_writer.writerow(row)
