#vetores e arrey

nome: str | None
class Onibus:
    def __init__(self, ncadeiras : int):
        self.espera : list[Pessoa] = []
        self.cadeira : list[Pessoa | None] = []
        for _ in range(ncadeiras):
            self.cadeira.append(None)

    def __str__(self):
        return f"Cadeiras{self.cadeira}/ n_espera {self.espera}"

david = Pessoa("David")
