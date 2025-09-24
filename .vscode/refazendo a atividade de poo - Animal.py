class Animal:
    def __init__(self, species:str, sound: str): #construtor
        self.species : str = species
        self.sound : str = sound
        self.age : int = 0

    def __str__(self) -> str: #to string
        return f"{self.species}:{self.age}:{self.sound}"

    def ageBy (self, increment : int ) -> None: #estagios de vida do animal
        if self.age == 4:
            print(f"warning: {self.species} morreu.")
        self.age += increment
        if self.age >= 4:
            self.age = 4
            print(f"waring: {self.species} morreu.")

    def makeSound(self) -> str: #som que o animal faz
        if self.age == 0:
            return "---"
        if self.age in (1,2,3):
            return self.sound
        if self.age == 4:
            return "RIP"

def main(species=None):
    animal : Animal = Animal ("","")
    while True:
        line: str = input()
        print ("$" + line)
        args:  list[str] = line.split(" ")
        if args[0] == "end":
             break
        if args[0] == "init":
             species: str = args[1]
             sound: str = args[2]
             animal = Animal(species, sound )
        if args[0] == "show":
             print(animal)
        if args[0] == "noise":
             print(animal.makeSound())



main()

