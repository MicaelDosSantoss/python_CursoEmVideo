from math import sin, cos, tan, radians
# Estou importando a biblioteca math, é também selecionando as ferramentas que eu irei usar

n = float(input('Digite o ângulo: '))
# número para ser digitado

c = cos(radians(n)) # O comando cos é para pegar um número é transforma-lo em COSSENO
s = sin(radians(n)) # O comando sin é para pegar um número é transforma-lo em SENO
t = tan(radians(n)) # O comando tan é para pegar um número é transforma-lo em TANGENTE  
# randians tranforma o número em radiante

print(f'O ângulo de {n}° tem o Cosseno de {c:.2f}°, o Seno de {s:.2f}°, e a Tangente de {t:.2f}°')

# usei o :.2f para deixar o número float com apenas 2 casas depois da vírgula

# código para descobrir se os valores do SENO, COSSENO é TANGENTE