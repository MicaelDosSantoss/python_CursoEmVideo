print("==== Desafio 1 ====")

nome = input('Qual o seu nome ?')

print('Olá, {}! Prazer é ter conheçer!'.format(nome) )

print("==== Desafio 2 ====")

dia = input('dia ?')
mes = input('mês ?')
ano = input('ano ?')

print('Você nasceu no dia {} de {} de {}, Correto ?'.format(dia,mes,ano))

print("==== Desafio 3 ====")

Num1 = int(input('Primeiro número ?'))
Num2 = int(input('Segundo número ?'))
soma =(Num1 + Num2)

# Os números não era somados poís input trazia o valor final é string, porém o Int() a string acaba virando um número inteiro


print('A soma é', soma)