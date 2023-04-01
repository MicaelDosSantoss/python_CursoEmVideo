r = input('Digite o nome da sua cidade: ').upper()

s = 'SANTO' in r

if s == True:
     print(f'Existe SANTO no nome da cidade, {r}')
else: 
    print('Não existe SANTO no nome da cidade')
