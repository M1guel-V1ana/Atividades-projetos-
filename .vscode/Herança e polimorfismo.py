from symtable import Class
from typing import Any
#liguagen não orientadas a objetos  ou pouco orientafas é nescessario ter um tipo de contrato, traits e interfaces... # forma que um objeto precisa ter pra ser tratado como algo

from abc import ABC, abstractmethod
# classe Pai
# classe Base
# super classe
class Brinquedo(ABC):

    def __init__(self, nome: str = "") -> None:  # cada briquedo de ter um nome.
        self.nome = nome

    def apertar(self):
        print("squish!!")
    @abstractmethod
    def jogar_nochao(self):
        pass


def brincar(brinquedo: Brinquedo):
   brinquedo.apertar()
   brinquedo.jogar_nochao()
   print(brinquedo.nome)



#sub classe
class Ursinho(Brinquedo):  # antes de ser um ursinho é um brinquedo, começa de dentra para fora, da camada interna 

    def __init__(self, nome: str ):
        super().__init__(nome)

    #def apertar(self) -> None:
     #   print("fuf!")

    def jogar_nochao(self) -> None:
         print("Ursinho quica e cai!")

    def getNome(self) -> str:
        return self.nome

    def __str__(self):
        return "Ursinho de pelucia"

class Bola(Brinquedo):
    def __init__(self, nome: str):
        super().__init__(nome)

    def apertar(self) -> None:
        print("pof!")

    def jogar_nochao(self) -> None:
        print("a bola quica repetidas vezes")

    def getNome(self) -> str:
        return self.nome

    def __str__(self):
        return "Bola de futebol, como é bom jogar!"
class Chocalho(Brinquedo):
    def __init__(self, nome: str):
        super().__init__(nome)
    def apertar(self) -> None:
        print("chocalho só faz barulho ao jogar no chão ")

    def jogar_nochao(self) -> None:
        print("briiinlinnn!")

    def getNome(self) -> str:
        return self.nome

    def __str__(self):
        return "Chocalho de bb"


brinquedos : list[Brinquedo] = [Ursinho("furão"), Bola("Rosa"), Chocalho("fluf")]
for brinquedo in brinquedos:
    brinquedo.apertar()