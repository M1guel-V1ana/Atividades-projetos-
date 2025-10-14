class Pessoa:
    def __init__(self, nome : str):
        self.nome = nome

    def __str__(self):
        return self.nome


class Moto:
    def __init__(self):
        self.pessoa : Pessoa | None = None #deixa explicito que não existe, tipagem de tipo "ou"


    def inserir(self, pessoa : Pessoa) -> bool:
        if self.pessoa != None:
            print("já tem pesosa na moto!")
            return True
        self.pessoa = pessoa
        return False

    def remover(self) -> Pessoa | None:
        aux = self.pessoa
        self.pessoa = None
        return aux

def main():
    moto = Moto()

    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end ":
            break
        if args[0] == "show":
            print(moto)
        if args[0] == "enter"