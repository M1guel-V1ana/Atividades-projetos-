class Slipper:
    def __init__(self):
        self.__tamanho : int = 0

    def getTamanho(self) -> int:
        return self.__tamanho

    def setTamanho(self, valor: int ):
        if valor > 19 and valor < 51:
            self.__tamanho = valor
            return
        else:
            print("fail: valor digitado nao corresponde ao tamanho da chinela ")
            return

def main():
    chinela = Slipper()

    while chinela.getTamanho() == 0 :
        tamanho = int(input(": "))
        chinela.setTamanho(tamanho)
    print("Parabens, você comprou uma chinela tamanho", chinela.getTamanho())
main()