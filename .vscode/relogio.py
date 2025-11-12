class Relogio:
    def __init__(self, hora : int = 0 , minuto : int = 0, segundo : int = 0  ):
        self.__hora = 0
        self.__minuto : int = 0
        self.__segundo : int = 0

        self.setHora(hora)
        self.setMinuto(minuto)
        self.setSegundo(segundo)

    def getHoras(self):
        return self.__hora
    def getMinuto(self):
        return self.__minuto
    def getSegundo(self):
        return self.__segundo

    def setHora(self, h : int):
        if h >= 0 and h <= 23:
            self.__hora = h
        else:
            print("hora invalida ")

    def setMinuto(self, m : int):
        if m >= 0 and m <= 59:
            self.__minuto = m
        else:
            print("minuto invalido")
    def setSegundo(self, s : int):
        if s >= 0 and s <= 59:
            self.__segundo = s
        else:
            print("segundo invalido")

    def nextSecond(self):
        self.__segundo +=1

        if self.__segundo > 59:
            self.__segundo = 0
            self.__minuto +=1
        if self.__minuto > 59:
            self.__minuto = 0
            self.__hora += 1
        if self.__hora > 23 :
            self.__hora = 0

    def __str__(self):
        return f"{self.__hora:02d}:{self.__minuto:02d}:{self.__segundo:02d}"

