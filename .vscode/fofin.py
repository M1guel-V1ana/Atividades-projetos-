class Calculadora:
    def __init__(self, batteryMax: int) :
        self.display: float = 0.0 # inicia sem valor
        self.battery : int = 0 # inicia 0
        self.batteryMax = int = batteryMax #carga máxima
    def __str__(self) -> str:
        return f"display = {self.display:.2f}, battery = {self.battery}"

    def charge(self, increment: int) -> None:
        self.batteryMax += increment

        if self.battery > self.batteryMax:
            self.battery = self.batteryMax


def main():
    calculadora: Calculadora = Calculadora( )
    while True:

        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "init":
            batteryMax: int = args[1]
        elif args[0] == "show":
            print(calculadora)
        elif args[0] == "charge":
            calculadora.charge(int(args[1]))


main()
