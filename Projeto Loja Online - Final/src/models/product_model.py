# Jonathan Martins Gomes - RA: 20.00862-7

class Produto():    
    # Método construtor
    def __init__(self,nome,descricao,keyword,valor,imagem):
        self._nome = nome
        self._descricao = descricao
        self._keyword = keyword
        self._valor = valor
        self._imagem = imagem
    
    # Getters da classe
    def get_Nome(self):
        return self._nome
    
    def get_Descricao(self):
        return self._descricao
    
    def get_Keyword(self):
        return self._keyword
    
    def get_Valor(self):
        return self._valor
    
    def get_Imagem(self):
        return self._imagem
        
    # Faz com que o item print de forma especifica
    def __str__(self) -> str:
        return f'Nome: {self._nome} - R$ {str(self._valor)}'