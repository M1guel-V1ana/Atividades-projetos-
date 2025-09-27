class Calculadora:
    def __init__(self, batterMax: int, battery: int, display):
        self.batteryMax = 0
        self.battery = 0
        self.display = 0

    def __str__(self) -> str:
        return f"display = {self.display:.2f}, battery = {self.batteryMax}"

    def charge(self, increment: int) -> None:
        self.batteryMax += increment

        if self.batteryMax > 5:
            self.batteryMax = 5


def main():
    calculadora: Calculadora = Calculadora("", "", "")
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
