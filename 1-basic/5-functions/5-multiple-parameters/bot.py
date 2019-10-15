# Function
def climb_ladder(remiNum,topNum):

    if remiNum < topNum:
        print("Still some way to go!")

    if remiNum > topNum:
        print("ERROR....we are at the top already!")

    else:
        print("We made it!")

# Call function
climb_ladder(2,5)
climb_ladder(5,5)
climb_ladder(6,5)

