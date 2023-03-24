from math import hypot
# estou importando o math, é usando a ferramenta para calculo de hipotenusa

c_o = float(input('Valor do cateto oposto: ')) # Digitar o valor do cateto oposto
c_a = float(input('Valor do cateto adjacente: ')) # Digitar o valor do cateto adjacente

h = hypot(c_o,c_a) # Calculo da hipotenusa

print(f'Valor da hipotenusa é {h}') # É mostrado o valor da hipotenusa