#controle de estado
#mater a consistencia interna

class Carro:
    def __init(self):
        self.npass = 0
        self.max_pass = 2
        self.km  = 0
        self.fuel = 0
        self.max_fuel = 100

    def entrar(self):
        if self.npass < 2 :
            self.npass +=1
            

#early return, retorna as fatias do problema como se estivesse querendo resolver
    def drive(self, distance : int):
        if self.npass ==0 :
            print("sem passageiros")
            return
        if self.fuel == 0 :
            print("sem gasolina")
            return
        if distance > self.fuel:
            print(f"andei só {self.fuel}")
            self.km += self.fuel
            self.fuel = 0
        self.fuel -= distance
        self.km += distance