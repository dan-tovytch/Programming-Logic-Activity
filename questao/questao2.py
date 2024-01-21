"""Questão 2 Aluno Daniel Melentovytch Santos RU: 4464640"""

# Exibe o cardápio
print('Bem vindos a lanchonete\n       '
      '**********CARDÁPIO**********\n'
      '| CÓDIGO |       Descrição       | Valor |\n'
      '|   100  |   Cachorro Quente     | 9,00  |\n'
      '|   101  | Cachorro Quente Duplo | 11,00 |\n'
      '|   102  |        X-Egg          | 12,00 |\n'
      '|   103  |       X-Salada        | 12,00 |\n'
      '|   104  |       X-Bacon         | 14,00 |\n'
      '|   105  |        X-Tudo         | 17,00 |\n'
      '|   200  |   Refrigerante lata   | 5,00  |\n'
      '|   201  |      Chá Gelado       | 4,00  |')

total = 0
dinheiro = 0

# Para dar inicio ao loop para que possa ser feito varios pedidos
while True:
    # Solicitação do codigo
    codigo = int(input('Entre com o código desejado: '))

    # Verifica qual produto foi escolhido e adiciona o valor correspondente a (dinheiro)
    if codigo == 100:
        valor = 9.00
        print('Você pediu um cachorro quente no valo de R${:.2f}'.format(valor))
    elif codigo == 101:
        valor = 11.00
        print('Você pediu um Cachorro quente duplo no valor de R${:.2f}'.format(valor))
    elif codigo == 102:
        valor = 12.00
        print('Você pediu um X-egg no valor de R${:.2f}'.format(valor))
    elif codigo == 103:
        valor = 12.00
        print('Você escolheu um X-Salada no valor de R${:.2f}'.format(valor))
    elif codigo == 104:
        valor = 14.00
        print('Você escolheu um X-Bacon no valor de R${:.2f}'.format(valor))
    elif codigo == 105:
        valor = 17.00
        print('Você escolheu um X-Tudo no valor de R${:.2f}'.format(valor))
    elif codigo == 200:
        valor = 5.0
        print('Você escolheu um Refrigerante lata no valor de R${:.2f}'.format(valor))
    elif codigo == 201:
        valor = 4.0
        print('Você escolheu um chá gelado no valor de R${:.2f}'.format(valor))

    # se o codigo não estiver na tabela dará como opção invalida
    else:
        print('Opção invalida')
        continue

    # Incrementa a quantidade de pedidos e adiciona o valor do produto ao total
    total += 1
    dinheiro += valor

    # Pergunta se o usuario deseja algo ou não
    cont = int(input('Deseja pedir algo mais?\n1 - Sim\n0 - Não\n>>'))

    # Se o usuário digitar 1, o loop continua
    if cont == 1:
        continue

    # Se o usuário digitar o, o loop para e finaliza
    elif cont == 0:
        break

# Exibe o total
print('o total a ser pago é: {:.2f}'.format(dinheiro))
