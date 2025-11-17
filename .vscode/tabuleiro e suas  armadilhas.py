class Player:
    def __int__(self, label: int, pos: int, free: bool):
        self.label = label
        self.pos = pos
        self.free = free

    def getLabel(self):
        return self.label
    def getPos(self):
        return self.pos

    def setPos(self, pos: int):
        self.pos = pos
    def setFree(self, free: bool):
        self.free = bool








def main():
    tabu = None

    while True:

        line = input()
        print("$"  + line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(tabu)
main()