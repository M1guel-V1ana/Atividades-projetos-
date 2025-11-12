class Pessoa:
    def __init__(self, nome: str ): # criam o metodo construtor para adionar pessoas
        self.nome = nome

    def __str__(self): #retorna o valor do nome da pessoa
        return  self.nome

class Mercantil: #representa o mercantil com caixas e filas de espera
    def __init__(self, n_caixas : int):
        self.espera : list[Pessoa] = []
        self.caixas : list[Pessoa | None] = []

        for _ in range(n_caixas):
            self.caixas.append(None)

    def chegar(self, pessoa : Pessoa): #simulação do cliente chegando
        self.espera.append(Pessoa) #adiciona pessoas a fila de espera

    def chamar(self, index : int):
        if index < 0 or index >= len(self.caixas):
            print("index invalido")
            return
        if self.caixas[index] is not None:
            print("caixa ocupado")
            return
        if len(self.espera) == 0:
            print("ninguem esperando")
            return

        self.caixas[index] = self.espera[0]

    def finalizar(self, index: int) -> Pessoa | None:
        if index < 0 or index >= len(self.caixas):
            print("index invalido")
            return None
        if self.caixas[index] is None:
            print("caixa vazio")
            return None
        aux = self.caixas[index]
        self.caixas[index] = None
        return aux
    def sair(self, nome : str) -> Pessoa | None:
        for i, pessoa in enumerate(self.espera):
            if pessoa.nome == nome:
                del self.espera[i]
                return
        for i, pessoa in enumerate(self.caixas):
            if pessoa and pessoa.nome == nome:
                self.caixas[i] = None
    def __str__(self):
        cadeiras = ", ".join([str(x) if x else "----" for x in self.caixas])
        espera = ", ".join([str(x) for x in self.espera])
        return f"Cadeira: [{cadeiras}]\nEspera: [{espera}]"

david = Pessoa("David")
print(david)
onibus = Mercantil(5)
onibus.espera.append(david)
onibus.espera.append(david)
onibus.espera.append(david)
onibus.espera.append(david)
onibus.espera.append(david)
onibus.caixas[2] = david
print(onibus)