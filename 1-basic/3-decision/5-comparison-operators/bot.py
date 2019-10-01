# User enters in whole numbers with a screen print of the whole number.
num1 =int(input("Please enter the first number."))
print(num1)
num2 =int(input("Please enter the second number."))
print(num2)

if (num1>num2):
    print("The second number is the smallest")
elif (num1<num2):
    print("The first number is the smallest")
else:
    print("both number are equal")
