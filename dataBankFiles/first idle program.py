#basic hello world program :D
def hello():
    print("Salutations, my fellow coder!")


hello()
name = input("What is your name? ")
if name == "Prakhar":
    password = input("Please enter your devpass: ")
    if password == "open.js":
        print('Good Afternoon ' + name + ', welcome to your devconsole')
        command = input("What would you like to do? ")
        if command == "printvalue":
            value = input("What is the value that is to be printed? ")
            print(value)



