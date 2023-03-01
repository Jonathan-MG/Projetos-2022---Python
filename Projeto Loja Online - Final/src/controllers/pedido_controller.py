# Jonathan Martins Gomes
# from controllers.carrinho_controller import Carrinho_Ctrl
from models.pedido_model import Pedido
from dao.pedido_dao import PedidoDAO

class Pedido_Ctrl:
    def __init__(self) -> None:
        self.pedido_db = PedidoDAO()

    def inserir_pedido(self,id_cliente, carrinho, data_hora):
        try:
            numero_pedido = len(self.pedido_db.get_all())+1
            produtos = str(carrinho.exibir_tudo())
            valor_total = carrinho.get_Valor_Total()
            Aux = Pedido(numero_pedido, id_cliente, produtos, valor_total, data_hora)
            self.pedido_db.inserir_pedido(Aux)
        except:
            return False
        return True