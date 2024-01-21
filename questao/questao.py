"""Questão1"""
# Imprime a mensagem de boas vindas
print('Bem vindo a loja')
# Pede ao usuário o valor do produto e a quantidade desejada
valor1 = int(input('Entre com o valor do produto: '))
quant = int(input('Entre com o valor da quantidade: '))

# Calcula o preço total sem desconto
mult = (valor1 * quant)

# Calcula o desconto com base na quantidade de produtos comprados
if 10 <= quant <= 99:
    desconto = mult * 0.05
elif 100 <= quant <= 999:
    desconto = mult * 0.1
elif quant >= 1000:
    desconto = mult * 0.15
else:
    desconto = 0

# Calcula o preço total com desconto e exibe ambos os valores
total = (mult - desconto)

# Imprime na tela o valor sem e com desconto
print('O valor sem desconto foi: R${:.2f}'.format(mult))
print('O valor com desconto foi R${:.2f} (Desconto {:.0%})'.format(total, desconto / mult))
