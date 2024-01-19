#Bishant Rajbanshi

def welcome():
  # Displays a welcome message to the user
  print("Welcome to the Ceasar Ciper\nThis program encrypts and decrypts text with the Ceasar Ciper algorithm")

def enter_message():
  while True:
    select_mode = input("Would you like to encrypt (e) or dycrypt (d): ")
    if select_mode == 'e' or select_mode == 'd':
      messages= input('What message would you like to {}: '.format('encrypt' if select_mode == 'e' else 'decrypt')).upper()
      return select_mode,messages
    else:
      print('Invalid Mode')

def encrypt(user_message,to_swift):
  encrypted_message = ""
  for char in user_message:
    if char.isalpha():
      if char.isupper():
        shifted_char = chr((ord(char) + to_swift - 65) % 26 + 65)
      else:
        shifted_char = chr((ord(char) + to_swift - 97) % 26 + 97)
      encrypted_message += shifted_char
    else:
      encrypted_message += char
  return encrypted_message

def decrypt(user_message,to_swift):
  decrypted_message = ""
  for char in user_message:
    if char.isalpha():
      if char.isupper():
        shifted_char = chr((ord(char) - to_swift - 65) % 26 + 65)
      else:
        shifted_char = chr((ord(char) - to_swift - 97) % 26 + 97)
      decrypted_message += shifted_char
    else:
      decrypted_message += char
  return decrypted_message

def process_file(file_name,select_mode):
  shift = int(input('What is the shift number: '))
  while not shift.isdigit():
        print('Invalid Shift')
        shift = int(input('What is the shift number: '))

  try:
    with open(file_name,'r') as file:
      user_message = [line.strip() for line in file]
      if select_mode == 'e':
        return[encrypt(message) for message in user_message]
      elif select_mode == 'd':
        return [decrypt(message) for message in user_message]

  except FileNotFoundError:
    print('File not found.')
    return[]

def is_file(file_name):
    try:
        with open(file_name, 'r'):
            return True
    except FileNotFoundError:
        return False

def write_messages(messages):
    with open('results.txt', 'w') as file:
        for message in messages:
            file.write(message + '\n')

def message_or_file():
   while True:
      select_mode = input("Would you like to encrypt (e) or dycrypt (d): ")
      if select_mode == 'e' or select_mode == 'd':  
         input_type = input('Would you like to read from a file (f) or the console (c)? ').lower()
         if input_type == 'c':
            messages= input('What message would you like to {}: '.format('encrypt' if select_mode == 'e' else 'decrypt')).upper()
            



    





welcome()
select_mode, user_message = message()
# encrypt(user_message,to_swift)
decrypt(user_message,to_swift)
