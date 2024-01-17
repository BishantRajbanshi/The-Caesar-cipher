#Bishant Rajbanshi

def welcome():
  print("Welcome to the Ceasar Ciper\nThis program encrypts and decrypts text with the Ceasar Ciper")

def message():
  while True:
    select = input("Would you like to encrypt (e) or dycrypt (d): ")
    if select == 'e' or select == 'd':
      messages= input('What message would you like to encrypt: ')
      return select,messages
    else:
      print('Invalid Mode')

welcome()
mode, user_message = message()

