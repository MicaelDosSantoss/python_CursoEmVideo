print('{:=^20}'.format(' Exercicio '))

n1 = int(input('primeiro valor :'))
n2 = int(input('segundo valor :'))


# + : Adição

adicao = n1 + n2 

# - : Substração

substracao = n1 - n2

# * : Multiplicação 

multiplicacao = n1 * n2

# / : Divisão

divisao = n1 / n2


print('as contas são:\n Adição {}\n Substração {}\n Multiplicação {}\n Divisão {:.3f},'.format(adicao, substracao, multiplicacao, divisao))

# No codigo {:.3f} : .3 siginifica 3 casas decimais, é o f significa flutuante.
# caso você coloque o codigo end="" não ira acontecer a quebra de linha.
# Outro comando é \n que quebra a linha

print('=' * 20)

# ** : Potência

potencia = n1 ** n2

# // : Divisão inteira

divisaoInteira = n1 // n2

# % : Resto da Divisão

restoDivisao = n1 % n2

print('as contas são:\n Potência {}\n Divisão inteira {}\n Resto divisão {}'.format(potencia, divisaoInteira, restoDivisao))

print('=' * 20)

# == : E usado para saber sobre um valor de uma conta

