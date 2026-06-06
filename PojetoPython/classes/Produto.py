from classes.AbstractCrud import AbstractCrud
"""
Classe responsável pelo gerenciamento
dos produtos do estoque.
"""
class Produto(AbstractCrud):

    arquivo = 'db/produtos.json'

    def __init__(self, codigo, nome, quantidade = 5, valor = 150):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor
# Inicializa os atributos do produto
    def inserir(self):
        lista = self.consultar()

        produtoDuplicado = [
            p for p in lista
            if p['codigo'] == self.codigo
        ]
# Impede o cadastro de produtos com código já existente
        if produtoDuplicado:
            print()
            print("Já existe um produto com esse código.")
            return

        super().inserir()