"""
Author: Luis Dawkins
Date: 10/15/23
This program will prompt a user for two file names, then copy the contexts of one file and output it to another another

1. Input
    prompt user for file names
2. Processing
    Copy text from input file
    Implant text to output file
    retrieve text from output file
    Format final output
3. Output
    print content of output file

"""

# Input
"""
Input_File = input("Enter a text file you want to be copied: ")
Output_File = input("Enter a text file to recieve data: ")
"""
Input_File = "Goofy.txt"
Output_File = "Insert.txt"

#Initialize key variables
Target_Text = ""

# Processing
File = open(Input_File, "r")

#Copy text
Target_Text = File.read()

#Implant text in output file
File = open(Output_File, "w")
File.write(Target_Text)

#Retrieve output text
File = open(Output_File, "r")

#Final Output
Final_Output = File.read()

#Close file
File.close()

# Output
print(f"The content of {Output_File} file is below: ")
print(Final_Output)