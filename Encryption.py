"""
This program encrypts a message inputted by the user using the vigenere cipher. This program uses
simple math equations to output a encypted message. Following the encryption process, export data either
through a basic print statement or using more advanced applications, such as email, twitter, or pastebin.

Significant Constants
    Default message
    Default custom key
1. Input
    User input process
    Recieve option
    Recieve message from user
    Recieve custom key from user
2. Processing
    Initialize Vigenere cipher variables
    Iterate through message
    Determine if char is a letter, or non-letter
    Calculate input variables for equation
    Main computational equation, or vigenere cipher
    Populate final message variable
3. Output
    Determine Data sharing output, default is print statement

Assignments:

Notes:
    Use Try and Except block to handle default variables for user input.

"""

### Significant Constants
text = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding'
Encryption_Tool = "Luna"

### Input
def User_Interface():

    Option_Menu = """
1. Encrypt
2. Decrypt
    
Input answer: """

    # Prompt user for encrypting option
    print("Would you like to encrypt or decrypt a message?")

    # Request message and encryption key for main computational program.
    try:
        Encryption_Tool = int(input(Option_Menu))
    except ValueError:
        Encryption_Tool = 3

    try:
        text = input("Message: ")
    except ValueError:
        text = "Hello, World!"

    try:
        custom_key = input("Custom Key: ")
    except ValueError:
        custom_key = "echo"

    return Encryption_Tool, text, custom_key


### Processing
def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    processed_text = ''
    key = key.lower()

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            processed_text += char
        else:
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            processed_text += alphabet[new_index]

    return processed_text

def encrypt(message, key):
    return vigenere(message, key)

def decrypt(message, key):
    return vigenere(message, key, -1)

### Output
def Main():

    Encryption_Tool, text, custom_key = User_Interface()

    if Encryption_Tool == 1:
        Encrypted_Text = encrypt(text, custom_key)
        print(f'Option: Encryption\nEncrypted text: {Encrypted_Text}\nCustom Key: {custom_key}')
    elif Encryption_Tool == 2:
        decryption = decrypt(text, custom_key)
        print(f'Option: Decryption\nDecrypted text: {decryption}\nCustom Key: {custom_key}')
    elif Encryption_Tool == 3:
        print("User did not input the right selection option.")

#Output
Main()
