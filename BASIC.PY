#Drawing Shapes
print("     /|")
print("    / |")
print("   /  |")
print("  /   |")
print(" /    |")
print("/_____|")



#Variables $ Datatypes
character_name = "Kelvin"
character_age = "38"
character_school = "University Of Portharcourt"

print("there was a man named " + character_name + '')
print("he is " + character_age + " years old")
print("he really liked the named " + character_name + '')
print("but doesn't like being " + character_age + '')
print("he is also a student of " + character_school + '')


#List
Friends = ["marvel", "princess", "Temperance", "goodnews"]
print(Friends)
Friends.append("blessing")
print(Friends)

#Dictionaries

Month_conversions = [
    'mon', "Monday",
    'tue', "Tuesday",
    'wed', "Wednesday",
    'thur', "Thursday",
    'fri', "Friday",
    'sat', "Saturday",
    'sun', "Sunday",
]

print(Month_conversions)

#Guessing Game
Secret_word = "MARVEL"
guess = ''
guess_count = 0
guess_limit = 3
out_of_guesses = False
while guess != Secret_word and not (out_of_guesses):
    if guess_count > guess_limit:
        guess = input("Enter Guess: ")
        guess_count += 1
    else:out_of_guesses = True

if out_of_guesses:
    print("Out Of Guess You Lose!!")
else:
    print("You Win The Game")

#STRING
    
School = "Programmers University"
print(School)
    
num = 1950
print("Rock music is my favourite music from the " + str(num) + 's')


#MAD LIPS GAME
color = input("Enter Color: ")
celebrity = input("Enter favourite celebrity: ")
Proffession = input("Enter current Proffession: ")
Sport = input("Enter Favourite Game: ")




print("Roses are " + color )
print("i love a " + celebrity)
print("my proffession is " + Proffession)
print("my  favourite game is " + Sport)

# BUILDING A CALCULATOR
num1 = input(int("Enter first num: "))
opp = input("Enter Opearator: ")
num2 = input(int("Enter second number: "))

if '+':
    print(num1 + num2)
elif '-':
    print(num2 - num1)
elif '/':
    print(num1 / num2)
elif '*':
    print( num1 * num2)
else: 
    print("Invalid Operation")
























        


























