digite = input('Digite algo :')

print('O {} tem número:'.format(digite), digite.isnumeric())
print('O {} tem letra:'.format(digite), digite.isalpha())
print('O {} tudo maisculo:'.format(digite), digite.isupper())
print('O {} tudo minusculo:'.format(digite), digite.islower())
print('O {} tem somente espaço:'.format(digite), digite.isspace())
print('O {} tem letras com números:'.format(digite), digite.isalnum())
print('O {} é capatalizada, contém letra maiscula é minuscula:'.format(digite), digite.istitle())