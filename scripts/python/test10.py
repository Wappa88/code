score = int(input('Tell me your today\'s score>> '))
difficulty = int(input('''Tell me your select difficulty from 0 to 3: 
0 : easy
1 : normal
2 : hard
3 : extra-hard
>> '''))

if score >= 100 and difficulty == 3:
  print('YOU ARE THE MASTER.')
else:
  print('Keep it going!!')