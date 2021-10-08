temperature = int(input("What is the temperature today?"))
if temperature > 32:
    print("What a hot day!")
elif temperature >= 28 and temperature <= 32:
    print("It is moderately hot today.")
else:
    print("It is cooling today.")
