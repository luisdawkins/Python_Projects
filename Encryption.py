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
Add option menu similar to traditional terminal menu, such as SEToolkit in linux
Complete a Final output message template for output message

Notes:
    Use Try and Except block to handle default variables for user input.

"""
"""
text = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding'
Encryption_Tool = "Luna"
"""

def User_Interface():

    Option_Menu = """
    1. Encrypt
    2. Decrypt
    """

    # Prompt user for encrypting option
    print("Would you like to encrypt or decrypt a message?")
    Encryption_Tool = input("Type either 'encrypt' or 'decrypt' :")

    # Request message and encryption key for main computational program.
    try:
        text = input("Message: ")
    except ValueError:
        text = "Hello, World!"

    try:
        custom_key = input("Custom Key: ")
    except ValueError:
        custom_key = "echo"

    return Encryption_Tool, text, custom_key

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    processed_text = ''

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

def Main():

    Encryption_Tool, text, custom_key = User_Interface()

    # Final Output Message should include option selected, text, and custom key
    Final_Output_Message = """
    
    """

    if Encryption_Tool == "encrypt":
        Encrypted_Text = encrypt(text, custom_key)
        print(f'\nEncrypted text: {Encrypted_Text}')
        print(f'Custom Key: {custom_key}')
    elif Encryption_Tool == "decrypt":
        decryption = decrypt(text, custom_key)
        print(f'\nDecrypted text: {decryption}\n')
        print(f'Custom Key: {custom_key}')

#Output
Main()
