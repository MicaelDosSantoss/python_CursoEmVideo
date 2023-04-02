from random import randint

c = '-=-'

print(f'{c * 20}\n ADIVINHE !!!\n{c * 20}') 

s = int(input('Que numero eu estou pensando, número de 0 a 5: ')) # pergunta

e = randint(0, 5) # número aleatorio de 0 a 5

if s == e: # se a variavel s for igual a váriavel e:
    print(f'Parabéns, você acertou, o número era {s}')
else: # se não
    print('Tente novamente !!!')