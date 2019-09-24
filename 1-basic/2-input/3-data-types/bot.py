# Input your human veriables 
name =input("What is your name human?") 
age =int(input("How old are you (in years)?"))
hight =float(input("How tall are you (in meters)?"))
weight =float(input("How much do you weigh (in kilograms)?"))
BMI=weight/(hight*hight)
print(name + " You are " + str(age) +"years old and you BMI is " + str(BMI))
