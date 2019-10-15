# Function
def escape_by(plan):
    if plan == "jumping over":
        print("We cannot escape that way! The boulder is too big")
        return plan
    if plan == "Running around":
        print("We cannot escape that way! The boulder is moving too fast!")
        return plan
    if plan == "going deeper":
        print("That might just work! Lets go deeper")
        return plan
    else:
        print("We cannot espace that way! The boulder is in the way!")
    

# Call Function
escape_by("jumping over")
escape_by("Running around")
escape_by("going deeper")
print()
escape_by("back flips")
