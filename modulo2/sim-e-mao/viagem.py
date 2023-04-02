s = float(input('Quantos KMs precisa para chegar a seu destino ?: '))

if s <= 200:
   r = (s * 0.50)
else:
    r = (s * 0.45)

print(f'O km {s} corresponde a um total de R$ {r:.2f}')