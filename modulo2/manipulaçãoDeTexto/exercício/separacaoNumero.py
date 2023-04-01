r = int(input('Digite um número de 0 a 9999: '))
 
u = r // 1 % 10 # pega a unidade
d = r // 10 % 10 # pega a dezena
c = r // 100 % 10 # pega a centena
m = r // 1000 % 10 # pega a milhar

print(f'Unidade: {u}\nDezena: {d}\nCentena: {c}\nMilhar {m}') # apresentação