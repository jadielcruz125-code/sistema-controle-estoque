import json
from abc import ABC

"""
Classe responsável pelas operações básicas
de CRUD e persistência em arquivos JSON.
"""
class AbstractCrud:
# Carrega os dados armazenados no arquivo JSON
    def detalhar(self):
        return self.__dict__

# Adiciona um novo registro à base de dados
    def inserir(self):
        lista = self.consultar()
        lista.append(self.detalhar())
        self.__gravarArquivo(lista)

# Atualiza os dados de um registro existente
    def alterar(self, item):
        lista = self.consultar()
        lista[item] = self.detalhar()
        self.__gravarArquivo(lista)

# Salva os dados atualizados no arquivo JSON
    def __gravarArquivo(self, lista):
        with open(self.arquivo, 'w') as file:
            json.dump(lista, file, indent=4, ensure_ascii=False)

        print('Operação realizada com sucesso')

# Remove um registro da base de dados
    @classmethod
    def excluir(cls, item):
        lista = cls.consultar()
        del lista[item]

        with open(cls.arquivo, 'w') as file:
            json.dump(lista, file, indent=4, ensure_ascii=False)
        print('Operação realizada com sucesso')

# Exibe todos os registros cadastrados
    @classmethod
    def ListarTodos(cls):

        lista = cls.consultar()

        if not lista:
            print("Nenhum produto cadastrado.")
            return

        print("\n===== PRODUTOS CADASTRADOS =====\n")

        for i, p in enumerate(lista):
            print(f"Item: {i}")
            print(f"Código: {p['codigo']}")
            print(f"Nome: {p['nome']}")
            print(f"Quantidade: {p['quantidade']}")
            print(f"Valor: R$ {float(p['valor']):.2f}")
            print("-" * 40)
# Retorna um item específico ou toda a lista
    @classmethod
    def consultar(cls, item=None):
        try:
            with open(cls.arquivo) as file:
                lista = json.load(file)

            return lista[item] if isinstance(item, int) else lista

        except Exception:
            return []