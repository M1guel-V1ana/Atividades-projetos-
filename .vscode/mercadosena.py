class Cliente:
    def __init__(self, nome: str):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def __str__(self):
        return f"{self.__nome}"


class Market:
    def __init__(self, caixas: int):
        self.espera: list[Cliente] = []
        self.caixas: list[Cliente | None] = [None for _ in range(caixas)]

    def __str__(self):
        caixas = ", ".join([str(x) if x else "-----" for x in self.caixas])
        espera = ", ".join(str(x) for x in self.espera)
        return f"Caixas: [{caixas}]\nEspera: [{espera}]"

    def arrive(self, cliente: Cliente):
        self.espera.append(cliente)

    def call(self, index: int):
        if self.espera == []:
            print("fail: sem clinetes")
            return
        if self.caixas[index] is not None:
            print("fail: caixa ocupado")
            return
        self.caixas[index] = self.espera.pop(0)

    def finish(self, index: int) -> Cliente | None:
        if self.caixas[index] is None:
            print("fail: caixa inexistente")
            return
        if index < 0 or index >= len(self.caixas):
            print("fail: caixa vazio")
            return

        aux = self.caixas[index]
        self.caixas[index] = None
        return aux


def main():
    mercado = None

    while True:

        line = input(": ")
        print("$" + line)
        args: list[args] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(mercado)
        elif args[0] =="init":
            p = int(args[1])
            mercado = Market(p)
        elif args[0] == "arrive":
            nome = args[1]
            mercado.arrive(Cliente(nome))
        elif args[0] == "call":
            num = int(args[1])
            mercado.call(num)
        elif args[0] == "finish":
            index = int(args[1])
            mercado.finish(index)


main()

