class Camisa:
    def __init__(self):
        self.__tamnaho: str = ""

    def getTamanho(self):
        return self.__tamnaho
    def setTamanho(self, valor : str ):
        if valor in ["PP", "P", "M", "G", "GG", "XG"]:
            self.__tamnaho = valor
        else:
            print("tamanho de roupa não encontrado")


def main():
    blusa = Camisa()

    while blusa.getTamanho() == "":
        tamanho = input(": ")
        blusa.setTamanho(tamanho)
    print("parabens você comprou uma camisa de tamanho", blusa.getTamanho())
main()