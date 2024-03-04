# greeting = "Hey!!\n"
# asking = "What are you doing right here right now?\n"
# raging = "Are you joking me!?"
# gentle = greeting * 3 + asking + raging

# print(gentle)

name = input("What's your name: ").upper()
birthYear = input("When is your birth year?: ")
birthMonth = input("When is your birth month?: ").capitalize()
birthDay = input("When is your birth day?:")

print("\n[" + name + "]'s birthdate is ...\n" + birthMonth + " " + birthDay + ". " + birthYear + "\n")