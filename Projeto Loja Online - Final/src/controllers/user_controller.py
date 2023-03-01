# Jonathan Martins Gomes - RA: 20.00862-7
from models.user_model import User
import streamlit as st
from dao.user_dao import User_DAO
        
def update_user_secrets(user_db):
    status_user_update = True
    login_info = open(".streamlit/secrets.toml",'w')
    login_info.write("[passwords]")
    login_info.close()
    for user in user_db:
        username = user.get_Username()
        email = user.get_Email().split("@")
        user_password = user.get_Senha()
        user_str = f'{username} = "{user_password}"'
        email_str = f'{email[0]} = "{user_password}"'
        login_info = open(".streamlit/secrets.toml",'r')
        login_info_read = login_info.read()
        login_info.close()
        if (f'{username} =' in login_info_read) or (f'{email[0]} =' in login_info_read):
                st.write(f'Username/E-mail já está em uso!')
                status_user_update = False
        else:
            login_info = open(".streamlit/secrets.toml",'a')
            if user_str == email_str:
                login_info.write(f'\n{user_str}')
            else:
                login_info.write(f'\n{user_str}')
                login_info.write(f'\n{email_str}')
            login_info.close()
    return status_user_update

class UserController():
    def __init__(self) -> None:
        self.user_db = User_DAO()
        self._users = self.user_db.get_all()
        update_user_secrets(self._users)
    
    def add_user(self, username, email, password, cpf, birthdate, name):
        try:
            Aux = User(username, email, password, cpf, birthdate, name)
            self.user_db.inserir_usuario(Aux)
        except:
            return False
        return True
    
    def update_user(self, username, kind, item):
        try:
            for user in self._users:
                if (username == user.get_Username()) or (username == user.get_Email()):
                    if kind == "password":
                        user.set_Senha(item)
                    else:
                        user.set_Email(item)   
                    self.user_db.atualizar_usuario(user)
        except:
            return False
        return True
    
    def get_Users(self,user):
        return self._users[user]
    
    def get_Quantidade_User(self):
        return len(self._users)
    
    def checkUser(self, user):
        return user in self._users