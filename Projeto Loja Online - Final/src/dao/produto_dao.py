# Jonathan Martins Gomes - RA: 20.00862-7

from pickle import FALSE, TRUE
import sqlite3
from models.product_model import Produto

class Produto_DAO:    
    _instance = None
    def __init__(self) -> None:
        self._connect()

    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = Produto_DAO
        ()
        return cls._instance

    def _connect(self):
        self.conn = sqlite3.connect('./database/sqlite.db')

    def get_all(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            SELECT * FROM Jogos;
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(Produto(keyword = resultado[0],
                                      nome = resultado[1],
                                      descricao = resultado[2],
                                      valor = resultado[3],
                                      imagem = resultado[4]))
        self.cursor.close()
        return resultados
    
    def inserir_item(self, item):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            INSERT INTO Jogos (id, nome, descricao, preco, imagem)
            VALUES(?,?,?,?,?);
        """, (item.get_Keyword(), 
              item.get_Nome(), 
              item.get_Descricao(), 
              item.get_Valor(), 
              item.get_Imagem()))
        self.conn.commit()
        self.cursor.close()
    
    def pegar_item(self, produto):
        id = produto.get_Keyword()
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Jogos WHERE id == '{id}';
        """)
        item = None
        resultado = self.cursor.fetchone()
        if resultado != None:
            item = Produto(keyword = resultado[0],
                           nome = resultado[1],
                           descricao = resultado[2],
                           valor = resultado[3],
                           imagem = resultado[4])
        self.cursor.close()
        return item

    def atualizar_item(self,item):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                UPDATE Jogos 
                SET nome = '{item.get_Nome()}', preco = '{item.get_Valor()}'
                WHERE id == '{item.get_Keyword()}';
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True
    
    def deletar_item(self, produto):
        id = produto.get_Keyword()
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                DELETE from Jogos WHERE id == '{id}';
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True
    
    def search_all_for_name(self, nome):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Jogos WHERE nome LIKE '{nome}%';
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(Produto(keyword = resultado[0],
                                      nome = resultado[1],
                                      descricao = resultado[2],
                                      valor = resultado[3],
                                      imagem = resultado[4]))
        self.cursor.close()
        return resultados