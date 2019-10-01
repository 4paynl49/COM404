# Working out if a whole number is odd or even.
num =int(input("Please enter a whole number."))

# Useing the modulo command
mod = num % 2
if mod > 0:
    print("The number " + str(num) + " is an odd number.")
else:
    print("The number " + str(num) + " is an even number.")

print("Hail Hydra")