# Jonathan Martins Gomes - RA: 20.00862-7

class Carrinho_Ctrl():
    def __init__(self) -> None:
        self._carrinho = []
    
    # Demais métodos da classe
    def adicionar(self,produto):
        for item in self._carrinho:
            if produto.get_Nome() == item.get_Nome():
                return False
        self._carrinho.append(produto)  
        return True  
    
    def exibir_Produtos(self,produto):
        return self._carrinho[produto]
    
    def get_Valor_Total(self):
        total = 0.0
        for produto in self._carrinho:
            total += produto.get_Valor()
        return total
    
    def exibir_tudo(self):
        resultado = []
        for item in self._carrinho:
            resultado.append(item.get_Nome())
        return resultado
    
    def get_Quantidade_Produtos(self):
        return len(self._carrinho)
    
    def remover(self,produto):
        if produto in self._carrinho:
            self._carrinho.remove(produto)