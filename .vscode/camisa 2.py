class Camisa:
    def __init__(self):
        self.__tamanho : str = ""

    def getTamanho(self):
        return self.__tamanho
    def setTamanho(self, valor : str ):
        if valor in ["PP", "P", "M", "G", "GG", "XG"]:
            self.__tamanho = valor
        else:
            print("tamanho de roupa inválido.")

def main():
    brusa = Camisa()

    while brusa.getTamanho() == "":
        tamanho = input()
        brusa.setTamanho(tamanho)
    print("parabens você comprou uma chinela de tamanho", brusa.getTamanho())
main()
