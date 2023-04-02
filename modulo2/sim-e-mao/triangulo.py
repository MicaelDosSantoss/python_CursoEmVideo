print('É possível fazer esse triangulo')

print('=-='*20)

n1 = float(input('Primeira reta:'))
n2 = float(input('Segunda reta:'))
n3 = float(input('Terceira reta:'))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
 print('É possível formar o triangulo')
else: 
 print('Não é possível formar o triangulo')