## While loop method
zones = int(input("How many zones must I cross?"))

print("Crossing zones...")
while zones > 0:
    print("...Crossed zone " + str(zones))
    zones = zones -1
print("Crossed all zones. Jumanji!")