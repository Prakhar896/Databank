# Selection constructs

# my code
##if input('Enter you name: ') == 'Prakhar':
##    print('Hey there prakhar!!!')
##else:
##    print('i dont know u...')

# lesson code
##is_raining = True
##
##if is_raining:
##    print('Use an umbrella')
##
##else:
##    print('Wear something light')

# Else: meant to cover any other conditions not mentioned in previous statements

# Nested if statements #
# Elif #

# Example: Authenticate a password #
# APPROACH 1 USING NESTED IF-ELSE
##password = "P@assword"

##givenPassword = input("Enter your password: ")
##
##if givenPassword == "":
##    print("Please do not give an empty input.")
##else:
##    if givenPassword == "P@ssword":
##        print("Correct password!")
##    else:
##        print("Incorrect password")


# APPROACH 2 USING ELIF

##if givenPassword == "":
##    print("Please do not give an empty input")
##elif givenPassword == "P@ssword":
##    print("Correct password!")
##else:
##    print("Incorrect password!")
##

# Challenge 1

##def day_of_week(day):
##    if day == "Mon" or day == "Tue" or day == "Wed" or day == "Thu" or day == "Fri":
##        return "weekday"
##    else:
##        return "weekend"
##
##print(day_of_week("Wed"))

# Challenge 2
##def sum_multiple(first, second, third, fourth, fifth):
##    result = 0
##    if first % 5 == 0:
##        result += 1
##    if second % 5 == 0:
##        result += 1
##    if third % 5 == 0:
##        result += 1
##    if fourth % 5 == 0:
##        result += 1
##    if fifth % 5 == 0:
##        result += 1
##    return result

# Challenge 3
##def odd_integer(first, second, third, fourth, fifth):
##    result = 0
##    if first % 2 == 0:
##        result += 1
##    if second % 2 == 0:
##        result += 1
##    if third % 2 == 0:
##        result += 1
##    if fourth % 2 == 0:
##        result += 1
##    if fifth % 2 == 0:
##        result += 1
##    return result
##

# Challenge 4
# for loop method
##def odd_integer(first, second, third, fourth, fifth):
##    ints = [first, second, third, fourth, fifth]
##    result = 0
##    for num in ints:
##        if num % 2 == 0:
##            result += 1
##    return result

# math method
def odd_integer(first, second, third, fourth, fifth):
    return first % 2 + second % 2 + third % 2 + fifth % 2


        
