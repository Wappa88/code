# def hello():
#   print('Hey you!!\n')

# hello()

# def convert(meters):
#   feet = meters * 3.281
#   return feet

# for i in range(1, 101):
#   print(i, 'm = ', convert(i), 'feet')

words = []

def prompt(kind):
  ask = "please enter " + kind + ": "
  word = input(ask)
  words.append(word)
  
prompt('adjective')
prompt('nationality')
prompt('name')
prompt('plural noun')
prompt('adjective')
prompt('plural noun')

print('Computers were invented by a', words[0], words[1], 'engineer named', words[2], '. To make a computer, you need to take a lot of', words[3], ', melt them down, and make', words[4], words[5], '.')