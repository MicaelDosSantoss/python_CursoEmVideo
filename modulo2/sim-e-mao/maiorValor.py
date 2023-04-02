n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))

maior = None
menor = None

# Maior número

if n1 > n2 and n1 > n3:
   maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
     maior = n3

# Menor número
if n1 < n2 and n1 < n3:
   menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
     menor = n3 


print('=-=' * 20)

print(f'Maior número, {maior}\nMenor número, {menor}')