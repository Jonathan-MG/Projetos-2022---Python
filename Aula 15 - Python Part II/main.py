from item import Item
from carrinho import Carrinho

item_1 = Item('Carregador','Carrega iPhone e Android',200.0)
item_2 = Item(valor = 350.0, nome = 'God of War', descricao = 'Kleiton - O Bom de Guerra')
item_3 = Item(valor = 350.0, nome = 'God of War', descricao = 'Kleiton - O Bom de Guerra')

carrinho = Carrinho()

# print(item_1==item_2)
# print(item_1==item_1)
# print(item_2==item_3)
# print(item_1==carrinho)

print(f'\nTamanho: {carrinho.get_Quantidade_Itens()}')
print(f'Valor: {carrinho.get_Valor_Total()}')

carrinho.adicionar(item_1)
carrinho.adicionar(item_2)

print(f'\nTamanho: {carrinho.get_Quantidade_Itens()}')
print(f'Valor: {carrinho.get_Valor_Total()}')

carrinho.remover(item_1)

print(f'\nTamanho: {carrinho.get_Quantidade_Itens()}')
print(f'Valor: {carrinho.get_Valor_Total()}')