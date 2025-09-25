class Carro:
    def __init__(self, passa: int = 0, gas: int = 0, km: int = 0):
        self.passa: int = 0
        self.gas: int = 0
        self.km: int = 0

    def __str__(self) -> str:
        return f"pass: {self.passa}, gas: {self.gas}, km: {self.km}"

    def maxPassa(self):
        self.passa += 1
        if self.passa >= 2:
            self.passa = 2
            print("fail: limite de pessoas atingido.")


def main():
    carro: Carro = Carro("", "", 0)

    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(carro)
        elif args[0] == "enter":
            carro.maxPassa()


main()