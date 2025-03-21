#Bishant Rajbanshi

def welcome():
  # Displays a welcome message to the user
  print("Welcome to the Ceasar Ciper\nThis program encrypts and decrypts text with the Ceasar Ciper")

def enter_message():
  while True:
    '''
    Ask user to choose weather to encrypt or dycrypt mode, message and shift number
    '''
    select_mode = input("Would you like to encrypt (e) or dycrypt (d): ")
    if select_mode == 'e' or select_mode == 'd':
      #Asks user weather to encrypt or decrypt the messages
      user_message= input('What message would you like to {}: '.format('encrypt' if select_mode == 'e' else 'decrypt')).upper()
      to_shift = input('What is the shift number: ')
      while not to_shift.isdigit():
        print('Invalid Shift')
        to_shift = input('What is the shift number: ')
      return select_mode, user_message, int(to_shift)
    else:
      print('Invalid Mode') 

#this function encrypts the message using Caeser Cipher and returns encrypted message
def encrypt(user_message,to_shift):
  encrypted_message = ""
  for char in user_message:
    if char.isalpha():
      if char.isupper():
        shifted_char = chr((ord(char) + to_shift - 65) % 26 + 65)
      else:
        shifted_char = chr((ord(char) + to_shift - 97) % 26 + 97)
      encrypted_message += shifted_char
    else:
      encrypted_message += char
  return encrypted_message

#this function decrypts the message using Caeser Cipher
def decrypt(user_message,to_shift):
  decrypted_message = ""
  for char in user_message:
    if char.isalpha():
      if char.isupper():
        shifted_char = chr((ord(char) - to_shift - 65) % 26 + 65)
      else:
        shifted_char = chr((ord(char) - to_shift - 97) % 26 + 97)
      decrypted_message += shifted_char
    else:
      decrypted_message += char
  return decrypted_message

#This function encrypts or decrypts the messages from file
def process_file(file_name,select_mode,to_shift):
  try:
    with open(file_name,'r') as file:
      user_message = [line.strip() for line in file]
      if select_mode == 'e':
        return[encrypt(message,to_shift) for message in user_message]
      elif select_mode == 'd':
        return [decrypt(message,to_shift) for message in user_message]

  except FileNotFoundError:
    print('File not found.')
    return[]

#Checks if the given named file exists or not
def is_file(file_name):
    try:
        with open(file_name, 'r'):
            return True
    except FileNotFoundError:
        return False

#Writes  results on result file if not founds it makes new one 
def write_messages(messages):
    with open('results.txt', 'w') as file:
        for message in messages:
            file.write(message + '\n')

#This function determines weather the input is from files or console and carries out functions accordingly
def message_or_file():
   onlyconsole = 'n'
   if onlyconsole == 'y':
     enter_message()
   else:
    while True:
        select_mode = input("Would you like to encrypt (e) or dycrypt (d): ")
        if select_mode == 'e' or select_mode == 'd':  
          input_type = input('Would you like to read from a file (f) or the console (c)? ').lower()
          if input_type == 'c':
              user_message= input('What message would you like to {}: '.format('encrypt' if select_mode == 'e' else 'decrypt')).upper()
              to_shift = input('What is the shift number: ')
              while not to_shift.isdigit():
                print('Invalid Shift')
                to_shift = input('What is the shift number: ')
              return select_mode, user_message, None, int(to_shift)
          elif input_type == 'f':
            filename = input('Enter a filename: ')
            if is_file(filename):
              to_shift = input('What is the shift number: ')
              while not to_shift.isdigit():
                  print('Invalid Shift')
                  to_shift = input('What is the shift number: ')
              return select_mode, None, filename, int(to_shift)
            else:
              print('Invalid Filename')
              return select_mode, None, None, None
          else:
              print('Invalid Input Type')
        else:
          print('Invalid Mode')


#This function is the main function of the given progarm
def main():
   #starts the program with a welcome meassage
   welcome()
   while True:
      select_mode, user_message, file_name, to_shift = message_or_file()
      if file_name:
        user_message = process_file(file_name, select_mode, to_shift)
        if user_message:
          write_messages(user_message)
          print('Output is written to results.txt')
      else:
        if select_mode == 'e':
          result = encrypt(user_message, to_shift)
        else:
          result = decrypt(user_message, to_shift)
        print(result)
        
      another_message = input('Would you like to encrypt or decrypt another message? (y/n): ').lower()
      while not (another_message == 'y' or another_message == 'n'):
        print('Invalid Input')
        another_message = input('Would you like to encrypt or decrypt another message? (y/n): ').lower()
      if another_message == 'n':
        print('Thanks for using the program, goodbye!')
        break

#Runs the main function when the script is executed
if __name__ == "__main__":
    main()
