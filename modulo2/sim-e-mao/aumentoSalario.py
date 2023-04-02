s = float(input('Qual o seu salário atual: '))

if s > 1250: # se a váriavel s for maior que 1250:
    c = s + (s * 10/100)
else: # Se não
    c = s + (s * 15/100)

print(f'Reajuste salarial é de R$ {s:.2f} para R$ {c:.2f}')    