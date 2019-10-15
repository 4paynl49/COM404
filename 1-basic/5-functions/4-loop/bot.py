# Function
def cross_bridge(steps):
    count = 1
    while count <= (steps):
        print("Crossed steps")
        count += 1

    if steps < 5:
         print("The bridge is collapsing!")

    else:
        print("We must keep going!")


# Call function
cross_bridge(3)
cross_bridge(6)