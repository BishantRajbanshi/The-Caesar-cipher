#Subash Bikram Tamang(2407749)
from unittest import result
from urllib import response

import os
def welcome():
    #Printing a welcome message for the Caesar Cipher program
    print("\nWelcome to the Caesar Cipher")
    print("This program encrypts and decrypts text with the Caesar Cipher. \n")

def enter_message():
    while True:
        '''
        Asking user to choose whether he/she want to use encryption or decryption mode and source.
        After doing those returns mode{encry and dcry}, source{messgae(if console), filename (if file)}, and shift. 
        '''
        mode= input("Would you like to encrypt (e) or decrypt (d): ").lower()
        if not (mode == 'e' or mode == 'd'):
            print('Invalid Mode')
            continue
        source = input("Would you like to read from a file (f) or the console (c)? ").lower()
        if not (source == 'f' or source == 'c'):
            print(f'Invalid Source')
            continue
        if source == 'f':
            fileName = input("Enter a filename: ")
            if not is_file(fileName):
                print("Invalid Filename")
                continue
            return mode, None, fileName, int(input("What is the shift number: "))
        else:
            #Asking the user to enter the message to be encrypted or decrypted 
            message = input("What message would you like to {}: ".format('encrypt' if mode == 'e' else 'decrypt'))
            while True:
                try:
                #Getting the shift value for caesar Cipher 
                    shift = int(input("What is the shift number: "))
                    break
                except ValueError:
                    print("Invalid Shift")

            return mode, message.upper(), shift
    
def encry_decry_key_generator(encry_or_decry, shift):
    #Generate the key-value pair for encryption or decryption based on the shift value 
    letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    keyValuePair = {}
    j = 0
    if shift > 26:
        shift %= 26
    
    if encry_or_decry == 'e':
        for i, lett in enumerate(letters):
            if shift + i < 26:
                keyValuePair[lett] = letters[i + shift]
            else:
                keyValuePair[lett] = letters[j]
                j += 1
    
    else:
        for i, lett in enumerate(letters):
            if shift + i < 26:
                keyValuePair[letters[i + shift]] = lett
            else:
                keyValuePair[letters[j]] = lett
                j += 1
    return keyValuePair

def encrypt(message, shift):
    #Encrypt the message using the Caesar Cipher 
    encry_key = encry_decry_key_generator('e', shift)
    result = ''
    for character in message:
        if character in encry_key:
            result += encry_key[character]
        else:
            result += character
    return result.upper()

def decrypt(message, shift):
    #decrypt the message using the Cesar Cipher 
    decry_key = encry_decry_key_generator('d', shift)
    result = ''
    for character in message:
        if character in decry_key:
            result += decry_key[character]
        else:
            result += character
    return result.upper()

#Checks if the given filename exists or not. 
def is_file(filename):
    return os.path.isfile(filename)

#Write a messages after going throught the shift process and stores the message in the file named "results.txt".
def write_messages(messages):
    with open('results.txt', 'w') as f:
        for message in messages:
            f.write(message + "\n")

def process_file(filename, mode, shift):
    '''
    Process a file for encryption or decryption(depends upon users choise).   
    '''
    if not is_file(filename):
        print("Invalid Filename")
        return []
    messages = []
    with open(filename, 'r') as f:
        for line in f:
            message = line.strip().upper()
            if mode == 'e':
                messages.append(encrypt(message, shift-1))
            else:
                messages.append(decrypt(message, shift-1))
    return messages

def message_or_file():
    enterMessage = enter_message()
    return enterMessage

#Main function
def main():
    #Entry point of the program 
    welcome()
    while True:
        #get user input ofr mode, message, and shift 
        mode, message,fileName, shift = message_or_file()
        if fileName is not None:
            messages = process_file(fileName, mode, shift)
            write_messages(
                [encrypt(message, shift) if mode == 'e' else decrypt(message, shift) for message in messages])
            print("Output written to results.txt")
        #performs encryption or decryption based on the user's choice 
        else: 
            if mode == 'e':
                print(encrypt(message, shift))
            else:
                print(decrypt(message, shift))

        #Asking the user if they want to encrypt/decrypt again 
        response = input("Would you like to encrypt/decrypt again? (y/n): ").lower()
        if response != 'y':
            print("Thanks for using the program, GoodBye!")
            break

if __name__ == '__main__':
    #Run the main function when the script is executed 
    main() 