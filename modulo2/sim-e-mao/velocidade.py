s = float(input('Velocidade atual do carro: '))

if s > float(80.0):
    m = (s - 80) * 7
    print(f'O seu veículo atingiu a velocidade {s}, deverá ser pago uma divida de R$ {m:.2f}')
else:
    print('tudo limpo !!')