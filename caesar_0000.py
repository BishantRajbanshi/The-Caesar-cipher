#Bishant Rajbanshi

def welcome():
  # Displays a welcome message to the user
  print("Welcome to the Ceasar Ciper\nThis program encrypts and decrypts text with the Ceasar Ciper algorithm")

def message():
  while True:
    select_mode = input("Would you like to encrypt (e) or dycrypt (d): ")
    if select_mode == 'e' or select_mode == 'd':
      messages= input('What message would you like to encrypt: ').upper()
      print(messages)
      swift = input('What is the shift number: ')
      while not swift.isdigit():
        print('Invalid Shift')
        swift = input('What is the shift number: ')
      return select_mode,messages,int(swift)
    else:
      print('Invalid Mode')

def encrypt(user_message,to_swift):
  encrypted_message = ""
  print(user_message)
  for char in user_message:
    if char.isalpha():
      if char.isupper():
        shifted_char = chr((ord(char) + to_swift - 65) % 26 + 65)
      else:
        shifted_char = chr((ord(char) + to_swift - 97) % 26 + 97)
      encrypted_message += shifted_char
    else:
      encrypted_message += char
  print(encrypted_message)
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
  print(decrypted_message)
  return decrypted_message




    





welcome()
select_mode, user_message,to_swift = message()
# encrypt(user_message,to_swift)
decrypt(user_message,to_swift)
