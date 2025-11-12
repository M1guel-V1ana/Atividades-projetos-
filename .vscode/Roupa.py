class Roupa:
    def __init__(self):
        self.__tamnahoroupa : str = ""

    def getTamanho(self):
        return self.__tamnahoroupa
    def setTamanho(self, valor: str):
        if valor in ["PP", "P", "M","G", "GG","XG"]:
            self.__tamnahoroupa  = valor
        else:
            print("fail: tamanho da roupa invalido, PP,P,M,G,GG ou XG")