# Jonathan Martins Gomes - RA: 20.00862-7

import sqlite3
from models.pedido_model import Pedido
class PedidoDAO:
    _instance = None
    def __init__(self) -> None:
        self._connect()

    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = PedidoDAO()
        return cls._instance

    def _connect(self):
        self.conn = sqlite3.connect('./database/sqlite.db')

    def get_all(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            SELECT * FROM Pedidos;
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(Pedido(numero_pedido = resultado[0],
                                     id_cliente = resultado[1], 
                                     produtos = resultado[2],
                                     valor_total= resultado[3], 
                                     data_hora = resultado[4]))
        self.cursor.close()
        return resultados
    
    def inserir_pedido(self, pedido):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            INSERT INTO Pedidos (
                id, 
                id_cliente, 
                produtos,
                valor_total, 
                data_hora
            )
            VALUES(
                "{pedido.numero_pedido}",
                "{pedido.id_cliente}",
                "{pedido.produtos}",
                "{pedido.valor_total}",
                "{pedido.data_hora}"
            );
        """)
        self.conn.commit()
        self.cursor.close()
    
    def pegar_pedido(self, numero_pedido):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Pedidos WHERE id == "{numero_pedido}";
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(Pedido(numero_pedido = resultado[0],
                                     id_cliente = resultado[1], 
                                     produtos = resultado[2],
                                     valor_total= resultado[3], 
                                     data_hora = resultado[4]))
        self.cursor.close()
        return resultados
    
    def atualizar_pedido(self, pedido):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                UPDATE Pedidos 
                SET produtos = "{pedido.produtos}", valor_total = "{pedido.valor_total}", data_hora = "{pedido.data_hora}"
                WHERE id == "{pedido.numero_pedido}";
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True
    
    def deletar_pedido(self, pedido):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                DELETE FROM Pedidos WHERE id == "{pedido.numero_pedido}";
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True