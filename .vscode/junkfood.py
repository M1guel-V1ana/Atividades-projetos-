class Slot:
    def __init__(self, name: str = "empty", quantity: int = 0, price: float = 0.00 ): #slots de comida com nome, preço e quantidade
        self.name = name
        self.quantity = quantity
        self.price = price

    def getName(self):
        return self.name
    def getQuantity(self):
        return self.price
    def getPrice(self):
        return self.price



    def setNam(self, name: str):
        self.name = name
    def setQuantity(self, quanitity: int):
        self.quantity = quanitity
    def setPrice(self, price: float):
        self.price = price
    def __str__(self):
        return f"[  {self.name}: {self.quantity} U : {self.price:.2f} R$]"


class VendingMachine:
    def __init__(self, capacity: int):
        self.slots: list[Slot] = [Slot() for _ in range(capacity)] # lista com os slots de comida
        self.saldo = 0.0

    def getSlot(self, index: int):
        if index < 0 or index >= len(self.slots):
            print("fail: indice não existe")
            return None
        return self.slots[index]

    def setSlot(self, index: int, name: str, quantity: int, price: float): #atribuimos valores
        if index < 0 or index >= len(self.slots):
            print("fail: indice não existe")
            return

        self.slots[index].setNam(name)
        self.slots[index].setQuantity(quantity)
        self.slots[index].setPrice(price)

    def clean(self, index: int):
        if index < 0 or index >= len(self.slots):
            print("fail: indice não encontrado")
            return
        self.slots[index] = Slot()

    def inserirDinheiro(self, value: float): #inserir o dinheirinho na máquina
        if value<= 0:
            print("fail: valor invalido")
            return
        self.saldo += value

    def pedirTroco(self) -> str: # pede o troco a máquina
        troco = self.saldo
        self.saldo = 0.0
        print(f"voce recebeu {troco:.2f} R$")
        return troco
    def comprar(self, index: int): # condições para comprar as comidas na maquina
        if index < 0 or index >= len(self.slots):
            print("fail: indice invalido")
            return
        slot = self.slots[index]

        if slot.getName() == "empty":
            print("fail: espiral sem produtos ")
            return
        if slot.getQuantity() == 0:
            print("fail: espiral sem produtos ")
            return
        if slot.getPrice() > self.saldo:
            print("fail: saldo insulficiente")
            return

        slot.setQuantity(slot.getQuantity() - 1)
        self.saldo -= slot.getPrice()


    def getSaldo(self):
        return self.saldo


    def __str__(self):
        out = " "
        for i, slot in enumerate(self.slots):
            out += f"{i} {slot}\n"
        out += f"saldo: {self.saldo:.2f} R$"
        return out



def main():
    jkf = VendingMachine(0)

    while True:
        line = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(jkf)
        elif args[0] == "init":
            qtd = int(args[1])
            jkf = VendingMachine(qtd)
        elif args[0] == "set":
            id = int(args[1])
            n = args[2]
            qtd = int(args[3])
            pr = float(args[4])

            jkf.setSlot(id, n, qtd, pr)
        elif args[0] == "limpar":
            l = int(args[1])
            jkf.clean(l)
        elif args[0] == "dinheiro":
            d = float(args[1])
            jkf.inserirDinheiro(d)
        elif args[0] == "troco":
            jkf.pedirTroco()
        elif args[0] == "comprar":
            id = int(args[1])
            jkf.comprar(id)
        else:
            print("fail: comando invalído !!!")

main()
