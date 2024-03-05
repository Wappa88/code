password = None
attempts = []
while password != 'riu1988':
  password = input("Enter correct password: ")
  attempts.append(password)
  if password != 'riu1988':
    print('Incorrect. Try again.')
    for i in attempts:
      print(i)
print('Welcome.')