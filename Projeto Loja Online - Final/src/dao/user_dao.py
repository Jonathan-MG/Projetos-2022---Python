# Jonathan Martins Gomes - RA: 20.00862-7

from pickle import FALSE, TRUE
import sqlite3
from models.user_model import User

class User_DAO:    
    _instance = None
    def __init__(self) -> None:
        self._connect()

    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = User_DAO
        ()
        return cls._instance

    def _connect(self):
        self.conn = sqlite3.connect('./database/sqlite.db')
    
    def get_all(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            SELECT * FROM Usuarios;
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(User(username = resultado[0],
                                    name = resultado[1],
                                    email = resultado[2],
                                    password = resultado[3],
                                    cpf = resultado[4],
                                    birthdate = resultado[5]))
        self.cursor.close()
        return resultados

    def inserir_usuario(self,usuario):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            INSERT INTO Usuarios (username, name, email, password, cpf, birthdate)
            VALUES(?,?,?,?,?,?);
        """, (usuario.get_Username(), 
              usuario.get_Name(), 
              usuario.get_Email(), 
              usuario.get_Senha(), 
              usuario.get_Cpf(), 
              usuario.get_Birthdate()))
        self.conn.commit()
        self.cursor.close()
        
    def pegar_usuario(self,username):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Usuarios WHERE username == '{username}';
        """)
        item = None
        resultado = self.cursor.fetchone()
        if resultado != None:
            item = User(username = resultado[0],
                        name = resultado[1],
                        email = resultado[2],
                        password = resultado[3],
                        cpf = resultado[4],
                        birthdate = resultado[5])
        self.cursor.close()
        return item
    
    def atualizar_usuario(self,usuario):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                UPDATE Usuarios 
                SET email = '{usuario.get_Email()}', password = '{usuario.get_Senha()}'
                WHERE username == '{usuario.get_Username()}';
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True
    
    def deletar_usuario(self, username):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                DELETE from Usuarios WHERE id == '{username}';
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True



