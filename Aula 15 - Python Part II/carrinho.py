class Carrinho():
    # Método construtor
    def __init__(self):
        self._itens = []
    # Demais métodos da classe
    def get_Valor_Total(self):
        total = 0.0
        for item in self._itens:
            total += item.get_Valor()
        return total
    def get_Quantidade_Itens(self):
        return len(self._itens)
    def adicionar(self,item):
        self._itens.append(item)
    def remover(self,item):
        if item in self._itens:
            self._itens.remove(item)