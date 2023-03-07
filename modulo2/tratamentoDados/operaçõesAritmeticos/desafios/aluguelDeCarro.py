d = int(input('quantos dias o carro ficou com você ? '))
k = float(input('quantos km rodados ? '))


p = ( d * 60) + (k * 0.15)

print('total a pagar pelo alguel é R${:.2f}'.format(p))

teste