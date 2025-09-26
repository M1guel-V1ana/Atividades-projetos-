class Carro:
    def __init__(self, modelo, cor, rodas):
        self.modelo = modelo
        self.cor = cor
        self.rodas = rodas
------------------
    def Andar(self):
        print("estou andando pela rua")

    def Descer(self):
        print("Estou Descendo")

    def Pasa(self):
        print("tem um passageiro.")
    def Componentes_car(self):
        print(self.modelo, self.cor, self.rodas)

carro = Carro("nissan" , "Preto", "rosinha")
carro.Andar()
carro.Descer()
carro.Pasa()
carro.Componentes_car()
