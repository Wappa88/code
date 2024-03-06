print(('''\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
 \\\\\\Unreliable Personality diagnosis!!\\\\\\
  \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n''').upper())
print("From now, I ask you 5 questions to analyse your personality!!(???)\n")

name = input('''But, At First, What is your name?:\n>> ''')
print("\nWelcome!! ", name, "!!\nSo, Let's get start it!!\n")

# Collect & Calclate user's answer 

# Redundant version but it works

# one = int(input('''Q1. Which color would you choose for your personal color?
#   Blue: 0
#   Red:  1
#   >> '''))
# two = int(input('''
# Q2. Which animal would you choose to pet?
#   Sheep:  0
#   Lion:   1
#   >> '''))
# three = int(input('''
# Q3. Which person would you choose to talk?
#   Kind, Calm, and Gentle: 0
#   Funny, Dangerous, and Chaos: 1
#   >> '''))
# four = int(input('''
# Q4. Which weapon would you choose for against your enemy?
#   Sword:  0
#   Gun:    1
#   >> '''))
# five = int(input('''
# Q5. Lastly, Which would you choose for your life?
#   Contributing to keep your society's order:  0
#   Fighting to refine this world:              1
#   >> '''))
# point = one + two + three + four + five

# Sophysticated version

questions = [
  "Q1. Which color would you choose for your personal color?\n  Blue: 0\n  Red: 1\n>> ",
  "Q2. Which animal would you choose to pet?\n  Sheep: 0\n  Lion: 1\n>> ",
  "Q3. Which person would you choose to talk?\n  Kind, Calm, and Gentle: 0\n  Funny, Dangerous, and Chaos: 1\n>> ",
  "Q4. Which weapon would you choose against your enemy?\n  Sword: 0\n  Gun: 1\n>> ",
  "Q5. Lastly, Which would you choose for your life?\n  Contributing to keep your society's order: 0\n  Fighting to refine this world: 1\n>> ",
]

# Preventing wrong input by while statement

answers = [] # Setting empty list.
for question in questions: # Doing variable question for each questions' asking from Q1 to Q5.
  while True: # Infinite loop until break statement is encountered.          
    answer = input(question)  # Storing question's value at variable answer.
    if answer in ['0', '1']:  # Validation user's input is 0 or 1.
      answers.append(int(answer)) # Adding answer's value at list called questions.
      break # Exiting loop.
    else: # If answer's value is not 0 or 1...
      print("OH OH, You have to input an appropriate number (0 or 1)!!\n")  # Showing this comment and return while.

# Addition a list called answers' each value
point = sum(answers)

# Showing result

print("\nAlright,", name, "'s personality is... Let me guess...\n")

if point >= 4:
  print(("You are as hot as fire!!").upper())
elif point == 3:
  print("You might be an ordinal person, but I sense a hidden passion within you...")
else:
  print("You are so COOL.")

# -------------------------------------------------------------
# Pseudocode
# Unreliable Personality diagnosis!!

# From now, I ask you 5 questions to analyse your personality!!(???)
# But, At First, What is your name?

# 1. Which color would you choose for your personal color?
#   Blue: 0
#   Red:  1

# 2. Which animal would you choose to pet?
#   Sheep:  0
#   Lion:   1

# 3. Which person would you choose to talk?
#   Kind, Calm, and Gentle: 0
#   Funny, Dangerous, and Chaos: 1

# 4. Which weapon would you choose for against your enemy?
#   Sword:  0
#   Gun:    1

# 5. Lastly, Which would you choose for your life?
#   Contributing to keep your society's order:  0
#   Fighting to refine this world:              1

# Result...
# Your're personality is...

# If point <= 4 then it's HOT!!
# Else if point == 3 then it's Normal.
# Else point <= 2 then it's COOL.
# -------------------------------------------------------------
# name = input("")
# one = int(input("Q1."))
# two = int(input("Q2."))
# three = int(input("Q3."))
# four = int(input("Q4."))
# five = int(input("Q5."))
# point = one + two + three + four + five

# print (name)
# if point <= 4:
#   print ("HOT")
# elif point == 3:
#   print ("Normal")
# else:
#   print ("COOL")

# Reference:
# Code & comment's evaluation: Perplexity.AI