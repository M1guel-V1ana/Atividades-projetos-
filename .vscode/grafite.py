class Grafite:
    def __init__(self, calibre: float, dureza: str, tamanho: int): # Construtor com os metodos calibre, dureza e tamanho...
        self.calibre = calibre
        self.dureza = dureza
        self.tamanho = tamanho

    def desgasteFolha(self) -> int : # aqui vai retorna a dureza do grafite que vou utilizar de acordo com a string...
        if self.dureza == "HB":
            return 1
        elif self.dureza == "2B":
            return 2
        elif self.dureza == "4B":
            return 4
        elif self.dureza == "6B":
            return 6
        else:
            return 0

    def __str__(self): # retorna os valores de
        return f"{self.calibre} : {self.dureza} : {self.tamanho} "

class Lapiseira: # classe lapseira onde vou o chmar em sequencia a classe Grafite...
    def __init__(self, calibre : float):
        self.calibre = calibre
        self.bico: Grafite | None = None # chama a classe grafite e atribui variaveis vázias a ela
        self.tambor : list[Grafite] = [] #cria uma lista vazia com os grafites de dureza variavel


    def __str__(self) -> str: # utilizamos formatação de strings para dar o retorno dos parametros adicionados
        bico = str(self.bico) if self.bico else "[]"
        tambor = "".join(str(g) for g in self.tambor)
        tambor = f"<{tambor}>"
        return (f"Calibre: {self.calibre}, bico: {bico}, tambor: {tambor}")

    def inserir(self, grafite: Grafite): #metodo para inserir o grafite
        if self.calibre != grafite.calibre: # verifica se grafite é de mesma espessura
            print("fail: calibre incompativel")
            return
        self.tambor.append(grafite) #adiciona o grafite ao tambor

    def puxar(self): #puxa um grafite para o bico
        if self.bico is not None: #verifica se o bico não está vazio
            print("fail: ja existe grafite no bico")
            return
        if not self.tambor: # faço a negação do tambor é a mesma coisa que está fazendo o len(self.tambor) == 0
            print("fail: tambor vazio")
            return
        self.bico = self.tambor.pop(0)

    def remover(self): #remove o grafite
        if self.bico is None:
            print("fail: nao existe grafite no bico")
            return
        self.bico = None

    def escrever(self): #definimos o metodo de escrever no papel
        if self.bico is None: #verificamos se o bico esta vazio
            print("fail: nao existe grafite no bico")
            return
        gasto = self.bico.desgasteFolha() #atribuimos uma variavel de gasto para escrever no papel de acordo com a espessura do grafite

        # se o grafite estiver com o tamanho <= 10 ele não pode ser usado

        if self.bico.tamanho() <= 10:
            self.bico = None
            print("fail: grafite pequeno demais")
            return
        if self.bico.tamanho - gasto < 10:
            self.bico = None
            print("fail: texto incompleto")
            return

        self.bico.tamanho -= gasto
        print(f"escreveu uma folha, grafite com {self.bico.tamanho}mm")


def main():
    lapinho = None

    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break

        elif args[0] == "show":
            print(lapinho)

        elif args[0] == "init":
            q = float(args[1])
            lapinho = Lapiseira(q)

        elif args[0] == "insert":
            calibre = float(args[1])
            dureza = args[2]
            tamanho = int(args[3])
            grafite = Grafite(calibre, dureza, tamanho)

            if lapinho is None:
                print("fail: lapiseira nao iniciada")
            elif not lapinho.inserir(grafite):
                print("fail: calibre incompatível")

        elif args[0] == "pull":
            lapinho.puxar()



main()
