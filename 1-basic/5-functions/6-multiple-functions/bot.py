# Function
def display_ladder(steps):
    for count in range(steps, 0, -1):
     print("|_|")
    
def create_ladder():
    steps = int(input("Hownmany steps are remaining? "))
    display_ladder(steps)

# Call function
create_ladder()