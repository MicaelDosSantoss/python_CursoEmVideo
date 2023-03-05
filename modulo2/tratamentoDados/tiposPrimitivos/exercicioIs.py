digite = input('Digite algo :')

print('O {} tem número :  '.format(digite), digite.isnumeric())
print('O {} tem letra :  '.format(digite), digite.isalpha())
print('O {} tudo maisculo :  '.format(digite), digite.isupper())
print('O {} tudo minusculo :  '.format(digite), digite.islower())