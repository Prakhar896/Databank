# Functions

# Authorise function (not taught/done by teacher, by me)
##print('DEV CONSOLE INITIALISE')
##def authorise(username, password):
##    if username == 'Prakhar0706':
##        if password == 'yaya':
##            print('Authorised!')
##            return
##        else:
##            print('Incorect password!')
##
##    else:
##        print('Incorrect username!')
##
##
##authorise(input('please enter the username: '), input('please enter the password: '))
##
##def contentPrint(content, repetitions):
##    for currentRepetition in range(repetitions):
##        print(content)
##
##contentPrint('baba', 3)

# Teacher's Content

# Objective of Function: Requests user for name and prints "Hello <name>"

def greet(name):
    print('Hello ' + name)
    return

##greet(input('What is your name? '))

# Challenges
# Challenge 1
##def how_old(birth_year):
##    # Complex Method
##    try:
##        asInt = int(birth_year)
##    except:
##        print('cannot convert to int')
##        return
##    years_old = 2021 - asInt
##    oldAsString = str(years_old)
##    print('You are ' + oldAsString + ' years old')
##    if years_old > 30:
##        print('damn bitch u old')
##        return
##    return
##
##how_old(input('What year were you born in? '))

# Challenge 2
def sameOrNot(first, second):
    # Complex Method
    if first == second:
        print('True')
        return True
    else:
        print('False')
        return False
    return
    # Simple Method
##    print(first == second)
##    return

sameOrNot(input('Enter first arg: '), input('Enter second arg: '))
