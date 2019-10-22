# Function
print("Your health is 100%. Escape is in progress...")
health = 100
count = 0

while count <= 5:
    UserInput=input("…Oh dear, who is that?")
    if UserInput == "Smiler's Bot":
        print("Time to jam out of here!")
        health=health -20


    elif UserInput == "Hacker":
        health + 20
        print("Yay! Better follow this one!")

    else:
        print("Phew, just another emoji!")
    count = count +1
    
print("Escaped! Health is ", str(health) + "%")

