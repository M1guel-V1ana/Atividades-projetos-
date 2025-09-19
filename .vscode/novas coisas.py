# Sem orientação a objeto :
def comer(comida):
    comida -=1
    return comida
def dormir():
    sono = False
    return sono
'''
cahorro_1 = "Nelson"
comida_cachorro_1 = 3
sono_cachorro_1 = True

cachorro_2 ="Pedrin"
comida_cachorro_2 = 6
sono_cachorro_2 = False

sono_cachorro_1 = dormir()

comida_cachorro_2 = comida(comida_cachorro_2)
'''

#com orientação a objetos:
class Cachorro:
    def __init__(self, nome, comida, sono):
        self.nome = nome
        self.comida = comida
        self.sono = sono
    def comer(self):
        self.comer -= 1
    def dormir(self):
        self.sono = False
#podemos criar varios cachorros dentro da mesma classe reutilizando os metodos

cachorro_1 = ("Nelson", 3, True)
cachorro_2 = ("Pedrin", 6,  False)

cachorro_2.comer()
cachorro_1.dormir()

