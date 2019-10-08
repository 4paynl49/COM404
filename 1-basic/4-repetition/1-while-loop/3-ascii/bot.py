count = 0
charging = 0

bars = int(input("How many bars should be charged?"))
while charging < bars:
    count += 1
    print("Charging: " + str(count*" █"))
    charging = charging +1

print("The battery is fully charged")
    
