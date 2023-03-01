# Jonathan Martins Gomes - RA: 20.00862-7

class User():
    def __init__(self, username, 
                 email, 
                 password, 
                 cpf, 
                 birthdate, 
                 name):
        self._username = username
        self._email = email
        self._password = password
        self._cpf = cpf
        self._birthdate = birthdate
        self._name = name
        self._contador = 0
    
    def get_Username(self):
        return self._username
    
    def get_Email(self):
        return self._email
    
    def get_Senha(self):
        return self._password
    
    def get_Cpf(self):
        return self._cpf
    
    def get_Birthdate(self):
        return self._birthdate
    
    def get_Name(self):
        return self._name
    
    def set_Email(self, email):
        self._email = email
    
    def set_Senha(self, password):
        self._password = password
    
    def __str__(self) -> str:
        return f'Username:"{self._username}", E-mail:"{self._email}", Senha:"{self._password}", Nome:"{self._name}", Nascimento:"{self._birthdate}", CPF:"{self._cpf}".'
    