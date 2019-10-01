# User enters in whole numbers with a screen print of the whole number.
num1 =int(input("Please enter the first number."))
print(num1)
num2 =int(input("Please enter the second number."))
print(num2)
num3 =int(input("Please enter Third number"))
print(num3)

evenCount = 0
oddCount = 0 

# checking condition 
if num1 % 2 == 0: 
    evenCount += 1
else:
    oddCount += 1

if num2 % 2 == 0: 
    evenCount += 1
else:
    oddCount += 1

if num3 % 2 == 0: 
    evenCount += 1
else:
    oddCount += 1


print ("There were " + str(evenCount) + " even and " + str(oddCount) + " odd numbers.")