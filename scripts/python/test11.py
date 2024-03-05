# play = int(input('''Did you play a game today?
# 0 : No
# 1 : Yes
# >>'''))

# if play == 1:
#   keyword = input('Tell me our secret code: ')
#   if len(keyword) >= 3:
#     print('It\'s too much!!')
#   else:
#     print('It\'s too short!!')
# else:
#   print('Get away from me now.')

words = []
game = int(input('''Did you play a game?:
0 : No
1 : Yes
>>\n'''))

while game == 1:
  new = input("Enter a 3-letter word: ")
  if len(new) > 3 or len(new) < 3:
    print('Go away!! That\'s not a 3-letter word.')
  else:
    if new in words:
      game = 'over'
      print('You already said that word. It\'s time to die, Trator!!')
      print('You know', len(words), "3-letter words.")
    else:
      print('Welcome back.')
      words.append(new)