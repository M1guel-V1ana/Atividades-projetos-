class Contato: # apenas os contatos
    def __init__(self, id,nome, email, telefone):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def toString(self):
        return f"{self.id}, {self.nome}, {self.email}, {self.telefone}"


# objetivo Criar uma classe agenda que vai alimentar essa classe Contatos

class Agenda:
    contato = []

    def adicionarContato(self, object):
        self.contato.append(object)
        print("contado adicionado com sucesso")


c1 = Contato(1,"Miguel","miguel@gmail.com", 222454484)
c2 = Contato(2,"Mateus", "mateus@gmail.com", 444856445)
c3 = Contato(3,"Viana", "viana@gmail.com", 4582565999)

a = Agenda()
a.adicionarContato(c1.toString())
a.adicionarContato(c2.toString())
a.adicionarContato(c3.toString())

print(a.contato)