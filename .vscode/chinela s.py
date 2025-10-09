class Chinela:
    def __init__(self):
        self.__tamanho : int = 0
    def getTamanho(self):
        return self.__tamanho
    def setTamanho(self, valor: int) -> int :
        if valor > 19 and valor < 51:
            self.__tamanho = valor
            return
        else:
            print("não existe esse tamanho de chinela")
            return

def main():
    chinelin = Chinela()
    while chinelin.getTamanho() == 0 :
        tamanho = int(input(":"))
        chinelin.setTamanho(tamanho)
    print("parabens, você comprou um chinelo de tamanho", chinelin.getTamanho())

main()