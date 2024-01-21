def cadastrarPeca(armazenamento):
    # Try e para que o programa não encerra caso algo for digitado errado
    try:
        codigo = input('Código da peça: ')
        nome = input('Por favor entre com o NOME da peça: ')
        fabricante = input('Por favor entre com o FABRICANTE da peça: ')
        valor = float(input('Por favor entre com o valor da PEÇA(R$): '))
        armazenamento[codigo] = {'Código': codigo, 'Nome': nome, 'Fabricante': fabricante, 'Valor': valor}
        print("Peça cadastrada com sucesso!")
    except ValueError:
        print('Valor inválido')


def consultarPeca(dicionario):
    print('1 - Consultar todas as peças\n'
          '2 - Consultar por código\n'
          '3 - Consultar por fabricante\n'
          '4 - Retornar')
    consulta = input(">> ")
    if consulta == '1':
        if not dicionario:
            print("Não há peças cadastradas.")
        else:
            print("Todas as peças cadastradas:")
            for codigo, peca in dicionario.items():
                print('-' * 15)
                print("Código da peça:", codigo)
                print("Nome da peça:", peca['Nome'])
                print("Fabricante da peça:", peca['Fabricante'])
                print("Valor da peça: R${:.2f}".format(peca['Valor']))
                print('-' * 15)
    elif consulta == '2':
        codigo_consulta = input('Digite o código da peça: ')
        peca = dicionario.get(codigo_consulta)
        # Mostra o resultado por código
        if peca:
            print('-' * 15)
            print("Código da peça:", codigo_consulta)
            print("Nome da peça:", peca['Nome'])
            print("Fabricante da peça:", peca['Fabricante'])
            print("Valor da peça: R${:.2f}".format(peca['Valor']))
            print('-' * 15)
        else:
            print("Peça não encontrado.")
    elif consulta == '3':
        fabricante_consulta = input('Digite o fabricante da peça: ')
        pecas_fabricante = []
        # Verifica o dicionário de peças, obtendo o código e a peça
        for codigo, peca in dicionario.items():
            # Verifica o fabricante da peça
            if peca['Fabricante'].lower() == fabricante_consulta.lower():
                pecas_fabricante.append((codigo, peca))

        if pecas_fabricante:
            print("Peças do fabricante", fabricante_consulta + ":")
            for codigo, peca in pecas_fabricante:
                print('-' * 15)
                print("Número do código:", codigo)
                print("Nome do produto:", peca['Nome'])
                print("Fabricante do produto:", peca['Fabricante'])
                print("Valor do produto: R${:.2f}".format(peca['Valor']))
                print('-' * 15)

        else:
            print("Nenhuma peça encontrada com este fabricante", fabricante_consulta)

    elif consulta == '4':
        return
    else:
        print("Opção de consulta inválida.")


def removerPeca(remover):
    # Pedido do código
    codigo_remocao = input("Digite o código da peça a ser removido: ")
    # Verifica se o código de remoção está presente na lista "remover"
    if codigo_remocao in remover:
        # Remove a peça da lista
        removido = remover.pop(codigo_remocao, None)
        print("Peça removida com sucesso!")
    else:
        print("Peça não encontrada.")
        print("Tente novamento")
        return removerPeca


# guarda o que for cadastrado
memoria = {}

# Pedido de opção para o usuario escolher
print('Bem vindo ao controle de Estoque da bicicletaria')
while True:
    try:
        print("Escolha a opções desejada:\n"
              "1 - Cadastrar peça\n"
              "2 - Consultar peça\n"
              "3 - Remover peça\n"
              "4 - Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            print('Você selecionou a opção (CADASTRAR PEÇA)')
            cadastrarPeca(memoria)
        elif opcao == "2":
            print('Você selecionou a opção (CONSULTAR PEÇA)')
            consultarPeca(memoria)
        elif opcao == '3':
            print('Você selecionou a opção (REMOVER PEÇA)')
            removerPeca(memoria)
        elif opcao == "4":
            break
        else:
            print("Opção inválida! Digite novamente.")
    except ValueError:
        print('Utilize apenas números')
