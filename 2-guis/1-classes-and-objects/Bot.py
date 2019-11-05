class Bot:
    def __init__(self, name, age=0, energy=0, shield=0):
        self.name = name
        self.age = age
        self.energy = energy
        self.shield = shield


### display_name ASCII
    def display_name(self):
        print("##########")
        print("#{}#".format(self.name))
        print("##########")

### display_age ASCII
    def display_age(self):
        print("   {}   ".format(self.age))
        print("   #   ")
        print("########")
        print("~~~~~~~~")
        print("########")

 ### display_energy ASCII
    def display_energy(self):
        bars = int(self.energy)
        print ("Energy:", bars * "█")

### display_sheild ASCII

    def display_sheild(self):
        shild_total = int(self.shield)
        print("Shiled:",shild_total * "*")

### display display_summary ASCII
    def __str__(self):
        return "Name is:{} Ages is:{} Energy is:{} Shiled is:{}".format (self.name, self.age, self.energy, self.shield)


beep = Bot("wibble", 7, 3, 4)
beep.display_name()
beep.display_age()
beep.display_energy()
beep.display_sheild()
print(beep.__str__())


    
    
    



