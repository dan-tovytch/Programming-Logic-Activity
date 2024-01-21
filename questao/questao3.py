def dimensoesObjeto():
    print('Bem vindo à companhia de logística')
    while True:
        # try para caso for digitado algum valor errado o programa não encerrar
        try:
            # solicita a dimensão do objeto
            largura = float(input('Digite o comprimento do objeto (em cm³): '))
            comprimento = float(input('Digite a largura do objeto (em cm³): '))
            altura = float(input('Digite a altura do objeto (em cm³): '))
            # calcula as dimensões
            volume = largura * comprimento * altura

            # Determina o valor da dimensão com base no volume
            if volume < 1000:
                va_dimensao = 10
            elif volume < 10000:
                va_dimensao = 20
            elif volume < 30000:
                va_dimensao = 30
            elif volume < 100000:
                va_dimensao = 50
            else:
                # se for muito grande
                print('O volume do objeto é (em cm³): {}'.format(volume))
                print('Não aceitamos objetos com dimensões tão grandes')
                continue
            print('O volume do objeto é (em cm³): {}'.format(volume))
            # Retorna o valor da dimensão e o volume do objeto
            return va_dimensao, volume

        except ValueError:
            print('Você digitou alguma dimensão do objeto sem valor numérico')
            print('Por favor, entre com as dimensões desejadas novamente')


def pesoObjeto():
    while True:
        print('Entre com o peso do objeto desejado')
        try:
            # pergunta o peso do objeto para o usuario
            peso = float(input('Digite o peso do objeto (em Kg): '))
        except ValueError:
            print('Você não digitou um valor numérico!')
            print('Por favor, entre com o peso desejado novamente')
            continue
        # Determina o valor do peso com base no peso digitado
        if peso <= 0.1:
            cal_peso = 1
        elif peso < 1:
            cal_peso = 1.5
        elif peso < 10:
            cal_peso = 2
        elif peso <= 30:
            cal_peso = 3
        else:
            # se for muito grande
            print('Não aceitamos objetos tão pesados')
            continue
        return cal_peso


def rotaObjeto():
    while True:
        # pergunta qual rota o usuario deseja
        rota = input('Selecione a rota:\n'
                     'BR - De Brasília até Rio de Janeiro\n'
                     'BS - De Brasília até São Paulo\n'
                     'RB - Rio de Janeiro até Brasília\n'
                     'RS - De Rio de Janeiro até São Paulo\n'
                     'SR - De São Paulo até Rio de Janeiro\n'
                     'SB - De São Paulo até Brasília\n'
                     '>>')
        if rota == 'BR' or rota == 'BS' or rota == 'RB' or rota == 'RS' or rota == 'SR' or rota == 'SB':
            break
        else:
            print('Esta rota não existe, selecione a sua rota novamente!')
    # Determina o valor da rota com base na rota selecionada
    if rota == 'RS' or rota == 'SR':
        va_rota = 1
    elif rota == 'BS' or rota == 'SB':
        va_rota = 1.2
    elif rota == 'BR' or rota == 'RB':
        va_rota = 1.5

    return va_rota


# Chama as funções e armazena os valores retornados em variáveis
va_dimensao, volume = dimensoesObjeto()
peso = pesoObjeto()
va_rota = rotaObjeto()
# Calcula o valor total com base nas dimensões, peso e rota
total = va_dimensao * peso * va_rota

# Imprime o valor total com as dimensões, peso e rota correspondentes
print('Total a pagar (R$): {:.2f} (dimensão: {:.2f} * peso: {:.2f} * rota {:.2f})'.format(total, va_dimensao, peso,
                                                                                          va_rota))
