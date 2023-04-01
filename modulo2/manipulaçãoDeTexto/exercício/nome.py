r = input('Digite seu nome completo: ').strip() # Digitar o nome é remover espações em brancos apenas do começo é do fim
s = '-' # Separação, usado na innha 13

max = r.upper() # Tudo maisculo
min = r.lower() # tudo minusculo

Quantletras = len(r) - r.count(' ') # Lê a quantidade de letra menos os espações

N = r.split() # transforma a frase em uma lista

QuantPrimeiroNome = len(N[0]) # Pegando apenas o primeiro nome

print(f'{s * 20}\n Nome em maisculo: {max}\n Nome em minusculo: {min}\n Quantidades de letras: {Quantletras}\n quantidades de letras do primeiro nome igual a : {QuantPrimeiroNome}')
# Apresentação do código