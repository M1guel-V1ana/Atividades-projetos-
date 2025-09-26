class Carro:
    def __init__(self, passa, gs, km ):
        self.passa : int = passa
        self.gs : int = gs
        self.km : int = km

    def __str__(self):
        return f"pass : {self.passa}, gas: {self.gs}, km: {self.km}"


    def Maxpass(self):
        if self.passa < 2:
            self.passa += 1
        else:
            print("perigo! Limite de pessoas atingido ")

    def leave(self):
        if self.passa == 0:
            print("ops! Não tem niguém no carro")
        else:
            self.passa -= 1

    def Maxga(self, increment : int):
        self.gs += increment
        if self.gs >100:
            self.gs = 100


    def drive(self, distance : int):
        if self.pas == 0:
            print("ops! cadê a galera do carro")
        elif self.gs == 0:
            print("cadê a gasosa ?")

        else:
            self.km += distance
            self.gas -= distance



def main():
    carro = Carro("", "", "")

    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "enter":
            carro.Maxpass()
        elif args[0] == "show":
            print(carro)
        elif args[0] == "leave":
            carro.leave()
        elif args[0] == "fuel":
            increment = int(args[1])
            carro.Maxga(increment)
        elif args[0] == "drive":
            increment = int(args[1])
            carro.drive(increment)
main()
