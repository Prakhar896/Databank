### Data Types
### 5 data types tested in current syllabus
##
##num = 123 # assigns 123 to the object "num"
##

### First: int (integers) -> positive or negative
##num1 = 1
##num2 = -2
##print("num1 is", type(num1), ", num2 is ", type(num2))
##

### floats -> can also be positive or negative
##num1 = 1.0
##num2 = 2. # still treated as float by python
##
##num3 = 2/1 # makes a float, as it is not floor division
##num4 = 2e6 # exponential, aka 2 * 10^3
##print(num4)
##

# string -> a string of characters
##string1 = "hey you!"
##string2 = 'so strong'
##string3 = ''' this is a super long
##and tough
##
##journey
##0 0
##_____
##rigk34g
##
##4g3
##
##'''
### triple quotes are not in the syllabus
### print(string3)
##string4 = 'hello' # if we press enter while typing a string with single quotes, it will just break the program
##
##string5 = 'Mr Phua\'s wife\'s birthday' # either this or use double quotes
##print(string5)
##string6 = "Mr Phua's \nwife's birthday"
##print(string6)
### \n is a esacaping character which creates a newline after it
### typing \t creates a tab (indentationo)
### typing just \ tells python to ignore end of line
##
##string7 = "mr phua \t is a teacher"
##print(string7)

# boolean -> True or False
##boo1 = True
##boo2 = False
##boo3 = 1 == 3
##print(boo3)
### logic operators create bool types
##
### list -> anythin, and everything in a pair of []
### sometimes known as arrays or matrix
### good habit to keep items of the same type in a list and not put multiple data types into a single list
##lst1 = []
##lst2 = [123, "abd", False, None, ("hey!"), [0,0,0,1]]
##print(lst2)
### lst2 is a bad example of a list but is one nonetheless
##
### a list within a list [[0], [[[0,0]]]] is called a nested list
##list3 = [
##    [0], [0],
##    [0], [0],
##    [1], [1]
##    ]
##print(list3)
### python is smart enough to tell that you are typing a list
### so even pressing enter will continue with typing of the list
##
##
### string placeholders
##string1 = "you are {} years old".format("smth") # {} is a placeholder

# string concatenation
# concatenation means + ing the strings together

first_name = "Eddie"
last_name = "Phua"
full_name = first_name + " " + last_name
print(full_name)

# string repetition

##top = "*"
##mid = "*" * 3
##bot = "*" * 5
##print(top,'\n' + mid, '\n' + bot)

### string formatting
##race = "Elven"
##pwr = 100
####print("Hi,", first_name + last_name, " welcome!"
##
##print("Hi, {} {}, welcome! You are of the {} race. Enjoy! You have {} power!".format(first_name, last_name, race, pwr))
##
### len() counts the number of characters including spaces in a string
##
##a = len("Eddie Phua")
##print(a) # prints 10

# indexing
selfish = "12345678"
#          01234567

##print(selfish[1])
##print(selfish[-1]) # prints 8
##print(selfish[len(selfish) - 1]) # gets the last character in a string

print(selfish[2:6]) # prints 3456
print(selfish[1:]) # slicing
print(selfish[::2]) # prints character after jumps two in between
# ^^^ prints 1357

# NOTE: STRINGS CAN'T BE CHANGED ONCE ASSIGNED
## selfish[7]='z' # type error

















