def is_league_united(hero1,hero2):
    if hero1 == "Superman" and hero2 == "Wonder Woman":
        print("true")
        return True
    else:
        print("false")
        return False

def decide_plan(hero1,hero2):
    Responce = is_league_united(hero1,hero2)
    if Responce == True:
         print("Time to save the world")
    else:
        print("We must united the league")
        
def run():
    hero1=input("Choose your first hero")
    hero2=input("Choose your second hero")
    plan=input("Please choose from League or Plan")
    if plan == "League":
        is_league_united(hero1,hero2)
    elif plan == "Plan":
        decide_plan(hero1,hero2)
    else:
        print("error")


run()
        

