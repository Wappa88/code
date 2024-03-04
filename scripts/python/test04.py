fruits = ['apple', 'orange', 'banana', 'grape', 'pear']

print(fruits[0:10])

fruits[3] = 'aaa'

print(fruits[3])
print(fruits[0:10])

fruits.append('ultimate_mango')
print(fruits[0:10])

fruits.insert(2, 'ultimate_pinapple')
print(fruits[0:10])

fruits.remove('orange')
fruits.sort()
print(fruits[0:10])

fruits.reverse()
print(fruits[0:10])

fruits_length = len(fruits)
print(fruits_length)

foods = ['rice', 'bread', ['okome', 'pan'], 'noodle']
print(len(foods))
print(foods[0:10])
print(foods[2])
print(foods[2][1])

height = input('input your height: ')
limit = int(height) > 10
print(limit)