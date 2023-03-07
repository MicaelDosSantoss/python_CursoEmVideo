d = float(input('qual o valor do produto ? R$'))


print('O desconto será de 10%,  valor final a pagar é: R${:.2f}'. format( d - (d*10/100) ))