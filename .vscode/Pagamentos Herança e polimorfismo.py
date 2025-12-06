from abc import ABC, abstractmethod
from logging import exception


class Pagamento(ABC):
    def __init__(self, valor: float, descricao: str):
        self.valor = valor
        self.descricao = descricao

    #def resumo(self): # pode ser feito assim
     #   print(f"Pagamento de R$ <{self.valor}>:<{self.descricao}>")


    def resumo(self) -> str:
        return f"Pagamento de R$ <{self.valor}>:<{self.descricao}>"

    def validar_valor(self):
        if self.valor <= 0 :
            raise Exception(" O valor do pagamento deve ser maior que 0")


    @abstractmethod
    def processar(self):
        pass

def processar_pagamento(pagamento: Pagamento):
    pagamento.resumo()
    pagamento.validar_valor()
    pagamento.processar()

class CartaoCredito(Pagamento):
    def __init__(self, valor, descricao, numero_cartao, nome_titular, limite_disponivel):
        super().__init__(valor, descricao)
        self.numero = numero_cartao
        self.nome_titular = nome_titular
        self.limite = limite_disponivel

    def processar(self):
        if self.valor > self.limite:
            print("Erro! você estourou o seu limite")

        else:
            self.limite -= self.valor
            print("Pagamento aprovado!")

class Pix(Pagamento):
    def __init__(self, valor, descricao, chave, banco):
        super().__init__(valor, descricao)
        self.chave = chave
        self.banco = banco

    def processar(self):
        print(f"Pagamento confirmado {self.chave}: {self.banco}")


class Boleto(Pagamento):
    def __init__(self, valor, descricao, codigo_barras, vencimento: str):
        super().__init__(valor, descricao)
        self.codigo = codigo_barras
        self.vencimento = vencimento

    def processar(self):
        print("Boleto Gerado. Aguardando pagamento...")


pagamentos = [Pix(7, "Coxinha", 3044512370, "PICPLAY"),
              CartaoCredito(400, "camisa polo vinho","123456789000", "Mikael", 3000),
              Boleto(200, "diamantes no free five",123456789000, "2026-04-17")]

for pagamento in pagamentos:
    try:
        processar_pagamento(pagamento)
    except Exception as e:
        print("Erro no pagamento", e)