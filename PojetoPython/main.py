from classes.Produto import Produto

# Exibe o menu principal do sistema
def menu():
    print()
    print("1 - Listar Produtos")
    print("2 - Inserir Produto")
    print("3 - Alterar Produto")
    print("4 - Excluir Produto")
    print("0 - Sair")
    print()
# Mantém o sistema em execução até o usuário escolher sair
opcao = 1

while opcao != 0:

    menu()
     # Valida a opção digitada pelo usuário
    try:
        opcao = int(input('Escolha uma opção: '))
    except ValueError:
        print("\n❌ Digite apenas números.\n")
        continue
    # Lista todos os produtos cadastrados
    if opcao == 1:

        print()
        print("=" * 50)
        Produto.ListarTodos()
        print("=" * 50)

    elif opcao == 2:
        # Coleta os dados do novo produto
        codigo = input("Código: ")

        if codigo.strip() == "":
            print("Código é obrigatório.")
            continue

        nome = input("Nome: ")
        
        if nome.strip() == "":
            print("Nome é obrigatório.")
            continue
        # Validação da quantidade
        while True:
            try:
                quantidade = int(input("Quantidade: "))

                if quantidade < 0:
                    print("Quantidade não pode ser negativa.")
                    continue

                break

            except ValueError:
                print("Digite apenas números inteiros.")
        # Validação dovalor do produto
        while True:
            try:
                valor = float(input("Valor:"))

                if valor < 0:
                    print("Valor não pode ser negativo.")
                    continue

                break

            except ValueError:
                    print("Digite um valor válido.")

        # Cria o objeto Produto e salva no JSON
        produto = Produto(codigo, nome, quantidade, valor)
        produto.inserir()

    elif opcao == 3:
        # Exibe os produtos disponíveis para alteração
        Produto.ListarTodos()

        lista = Produto.consultar()

        if not lista:
            print("\n❌ Nenhum produto cadastrado.\n")
            continue

        # Valida o item selecionado
        try:
            selecionado = int(input('Qual item deseja alterar? '))

            if selecionado < 0 or selecionado >= len(lista):
                print("\n❌ Item inexistente!")
                print("Digite um número válido da lista.\n")
                continue

        except ValueError:
            print("\n❌ Digite apenas números.\n")
            continue

        item = Produto.consultar(selecionado)

        # Mostra os dados atuais do produto
        print("\n===== DADOS ATUAIS =====")
        print(f"Código: {item['codigo']}")
        print(f"Nome: {item['nome']}")
        print(f"Quantidade: {item['quantidade']}")
        print(f"Valor: R$ {float(item['valor']):.2f}")
        print()

        #Permite manter o nome atual pressionando Enter
        nome = input(f"Novo nome [{item['nome']}]: ")

        if nome == "":
            nome = item['nome']

        while True:

            # Permite manter a quantidade atual pressionando Enter
            quantidade = input(
                f"Nova quantidade [{item['quantidade']}]: "
            )

            if quantidade == "":
                quantidade = item['quantidade']
                break

            try:
                quantidade = int(quantidade)

                if quantidade < 0:
                    print("Quantidade não pode ser negativa.")
                    continue

                break

            except ValueError:
                print("Digite apenas números.")

        while True:

            # Permite manter o valor atual pressionando Enter
            valor = input(
                f"Novo valor [{item['valor']}]: "
            )

            if valor == "":
                valor = item['valor']
                break

            try:
                valor = float(valor)

                if valor < 0:
                    print("Valor não pode ser negativo.")
                    continue

                break

            except ValueError:
                print("Digite um valor válido.")

        # Atualiza o produto selecionado
        produto = Produto(
            item['codigo'],
            nome,
            quantidade,
            valor
        )

        produto.alterar(selecionado)

    elif opcao == 4:

        # Exibe os produtos disponíveis para exclusão
        Produto.ListarTodos()

        lista = Produto.consultar()

        if not lista:
            print("\n❌ Nenhum produto cadastrado.\n")
            continue

        try:
            selecionado = int(input('Qual item deseja excluir? '))
        except ValueError:
            print("\n❌ Digite apenas números.\n")
            continue

        if selecionado < 0 or selecionado >= len(lista):
            print("\n❌ Item inexistente!")
            print("Digite um número válido da lista.\n")
            continue

        # Solicita confirmação antes da exclusão
        confirmacao = input("Tem certeza? (S/N): ").upper()

        if confirmacao == "S":
            Produto.excluir(selecionado)
        else:
            print("Exclusão cancelada.")
# Encerramento do sistema
print()
print("Ate a próxima!")

'''
Essa parte do codigo usamos match case, mas como meu programa não roda por causa das atualizaçoes o codigo sera feira tambem com if e elif 
para ver funcionando


    match opcao
        case 1:
            print()
            print('*****************************************************************************************************************')
            Produto.ListarTodos()
            print('*****************************************************************************************************************')

        case 2:
            codigo = input('Digite o código: ')
            nome = input('Digite o nome: ')
            quantidade = input('Digite a quantidade: ')
            valor = input('Digite o valor: ')

            produto = Produto(codigo, nome, quantidade, valor)
            produto.inserir()

        case 3:
            
            Produto.ListarTodos()
            selecionado = int(input('Qual item deseja alterar? '))
            item = Produto.consultar(selecionado)

            quantidade = int(input('Qual a nova Quantidade? '))
            valor = int(input('Qual o novo Valor? '))

            produto = Produto(item["codigo"], item ["nome"], quantidade, valor)
            produto.alterar(selecionado)


        case 4:

            Produto.ListarTodos()
            selecionado = int(input('Qual item deseja excluir? '))
            Produto.excluir(selecionado)

'''