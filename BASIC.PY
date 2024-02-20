
#Drawing Shapes
print("     /|")
print("    / |")
print("   /  |")
print("  /   |")
print(" /    |")
print("/_____|")

#BUILDING A SIMPLE LOGIN AND SIGNUP SYSTEM

print("CREATE ACCOUNT")
user_name1 = input("USER_NAME: ")
Email = input("EMAIL: ")
Password1 = input("PASSWORD: ")

print("Hello " + user_name1 + " Your Account Has Been Created Sucessfully.")


print("LOGIN NOW")
user_name2 = input("USER_NAME: ")
Password2 = input("PASSWORD: ")
if user_name2 == user_name1 and Password2 == Password1:
    print("WELCOME BACK " + user_name2)
elif user_name2 == user_name1 and Password2 != Password1:
    print("CORRECT USER_NAME AND INCORRECT PASSWORD")
elif user_name2 != user_name1 and Password2 == Password1:
    print("INCORRECT USER_NAME AND CORRECT PASSWORD")
else:
    print("INCORRECT USER_NAME AND PASSWORD")


#CLASSES
class employee:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

name = input("Enter your name: ")
age = input("Enter your age: ")
position = input("Enter your position: ")

person = employee(name, age, position)
print(person.name)
print(person.age)
print(person.position)


#READING AND WRITING FILES
Employee_file = open('Employee.txt', 'r')
print(Employee_file.readable)
print(Employee_file.readlines)

Employee_file.close()


#TRY AND EXCEPT IN PYTHON
try:
    x = int(input("Input an interger: "))
    print(x)
except ValueError:
    print("Invalid Value......" )
finally:
    print("Try and Except Finished")

    
#2D LIST AND NESTED LOOPS IN PYTHON
Even_num = [
    [2, 4, 6],
    [8, 10, 12],
    [14, 16, 18],
]

print(Even_num[2][1])
for num in Even_num:
    for rows in num:
        print(rows)
#FOR LOOPs
numbers = [10, 20, 30, 40, 50]
for num in numbers:
    print(num)


#WHILE LOOPs
i = 1
while i <=  6:
    print(i)
    i += 1

#IF STATEMENT  1
value = int(input("Input A Number: "))
if value % 2 == 0:
    print(value, " can be divided 2 ")
else:
    print(value, "cannot be divided by 2")

#IF STATEMENT  2
A =9
B =9
if A > B:
    print(str(A) + " is greater than " + (str (B)))
elif A == B:
    print(str(A) + " is equal to " + (str(B)))
else:
   print(str(A) + " is less than " + (str (B)))

#RETURN KEYWORD 
def subtract_num(num1, num2):
    return num1-num2

num1 =int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(subtract_num(num1, num2))

#FUNCTONS IN PYTHON
def greeting_fun(name, age):
    print("Welcome " + name + " you are " ,age, 'years old')

name = input("Enter your name: ")
age = input("Enter your age: ")
greeting_fun(name, age)

#TUPLES
Even_num = (2, 4, 6, 8, 10)
print(Even_num)
print(Even_num[3])
print(len(Even_num))
print(type(Even_num))


#SIMPLE WORD REPLACEMENT PROGRAM
Sentence = input("Enter Your Sentence: ")
print("Your Sentence is: " + Sentence)
Word1 = input("Enter Word to replace: ")
Word2 = input("Enter Word to replace it with: ")
print(Sentence.replace(Word1, Word2))



#Strings
name = 'Marvel'
Age = 20
print(name.upper())
print(name + ' is' , Age)


#Variables $ Datatypes
character_name = "Kelvin"
character_age = "38"
character_school = "University Of Portharcourt"

print("there was a man named " + character_name + '')
print("he is " + character_age + " years old")
print("he really liked the named " + character_name + '')
print("but doesn't like being " + character_age + '')
print("he is also a student of " + character_school + '')


#GETTING USERS INPUT
name = input("Enter Your Name: " )
Age = int(input("Enter your Age: "))

print("Hello " + name + " You Are " ,Age)


#List
Friends = ["marvel", "princess", "Temperance", "goodnews"]
print(Friends[2][3])
print(type(Friends))
Friends[0] = "Prince"
print(Friends)
cgpa = [2.5, 2.7, 3.8, 4.0]
print(Friends)
Friends.append("blessing")
print(Friends)
Friends.extend(cgpa)
print(Friends)

#Dictionaries
Month_conversions = {
    'mon': "Monday",
    'tue': "Tuesday",
    'wed': "Wednesday",
    'thur': "Thursday",
    'fri': "Friday",
    'sat': "Saturday",
    'sun': "Sunday",
}

print(Month_conversions)
print(Month_conversions['wed'])

# Building Guessing Game
Secret_word = "MARVEL"
guess = ''
guess_count = 0
guess_limit = 3
out_of_guesses = False
while guess != Secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter Guess: ")
        guess_count += 1
    else: out_of_guesses = True

if out_of_guesses:
    print("Out Of Guess You Lose!!")
else:
    print("You Win The Game")

#STRING
School = "Programmers\nUniversity"
print(School)
    
num = 1950
print("Rock music is my favourite music from the " + str(num) + 's')


#MAD LIPS GAME
color = input("Enter Color: ")
celebrity = input("Enter favourite celebrity: ")
Proffession = input("Enter current Proffession: ")
Sport = input("Enter Favourite Game: ")


print("Roses are " + color )
print("i love " + celebrity)
print("my proffession is " + Proffession)
print("my  favourite game is " + Sport)

#BUILDING A BASIC CALCULATOR
num1 = int(input("Enter first num: "))
opp = input("Enter Opearator: ")
num2 = int(input("Enter second number: "))

if opp =='+':
    print(num1 + num2)
elif opp =='-':
    print(num1 - num2)
elif  opp == '/':
    print(num1 / num2)
elif opp =='*':
    print( num1 * num2)
else:
    print("Invalid Operator")
































        


























