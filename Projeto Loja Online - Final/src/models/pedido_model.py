# Jonathan Martins Gomes - RA: 20.00862-7

class Pedido:
    def __init__(self, numero_pedido, id_cliente, produtos, valor_total, data_hora) -> None:
        self.numero_pedido = numero_pedido
        self.id_cliente = id_cliente
        self.produtos = produtos
        self.valor_total = valor_total
        self.data_hora = data_hora

    def __str__(self) -> str:
        return f'Número do Pedido: {self.numero_pedido} - Cliente: {self.id_cliente} - Data: {self.data_hora}\nProdutos: {self.produtos}\nValor total: {str(self.valor_total)}'