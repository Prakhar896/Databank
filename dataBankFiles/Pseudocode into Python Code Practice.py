# Challenge 1
while True:
    birth_year = int(input('Enter your birth year: '))
    if birth_year > 2021:
        print('Invalid input. Try again.')
        continue
    else:
        break

age = 2021 - birth_year
print(age)

# Challenge 2
while True:
    pwd = input('Enter password: ')
    if not (len(pwd) >= 8 and pwd.find(' ') == -1 and pwd.isalnum() == False):
        print('Invalid password. Try again.')
        continue
    hasUppercase = False
    hasNumber = False
    for char in pwd:
        if char.isupper():
            hasUppercase = True
        if char.isnumeric():
            hasNumber = True
    if hasUppercase and hasNumber:
        print('success')
        break
    else:
        print('Invalid password. Try again.')
        continue

