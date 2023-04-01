# Quando vc armazena uma string ela vai ser lida de forma um por um
# EXEMPLO

t = 'Ola, mundo'
s = '-'

# python : O - l - á - ,-  - m - u - n - d - o, será lido dessa forma em python

# Fatiamento de String 
print(f' Uma uníca letra: {t[0]}, uma parte inteira do texto: {t[5:10]}')

# Fatiamento de string, pulando de 2 em 2

print(f'Pulando de 2 em 2: {t[0:11:2]}')

# 5 até o final

print(f'{t[5:]}')


# do inicio parando do 3

print(f'{t[:3]}')

print('{}\n Analise de string\n'.format('=' * 20))

# len() - descobre o comprimento do texto

print(f'Comprimento do texto é de: {len(t)} \n')

# Count() - conta quantas letras iguais tem no texto, a letra teve ser colocada como parametro

print('quantas vírgulas tem: {}\n'.format(t.count(',') ) )

# caso vc coloque um valor int no paramentro ele ira criar um fatiamento, sim isso é póssivel

# Find() - pegar uma determinada parte da frase

print('Onde há o mundo na frase : {}'.format(t.find('mundo')))

# Caso o find retorne -1 significa que a parte que foi determinada n existe

print('Existe batata na frase : {}\n'.format(t.find('Batata')))

# Você também pode usar o in além do find, pórem ele retornará true se existe, é false caso não existe

print('Existe Ola na frase: {}'.format('Ola' in t))
print('Existe Batata na frase: {}\n'.format('Batata' in t))

print(f'{s * 5} Alteração de caracteres {s * 5}\n')

# Replace() - server para fazer alterações na frase ultilizando codigos

print('{} virou {}\n'.format(t, t.replace('mundo','micael')))

# ele substitiu de uma formar secundaria, ele n altera o código para sempre

# upper() deixa tudo maisculo é lower() deixa tudo minusculo

print('Tudo Maisculo : {}'.format(t.upper()))
print('Tudo Minusculo : {}\n'.format(t.lower()))

# Capitalize - ele ira pegar todos a frase deixará em minusculo todos os caracteres, menos o primeiro caracter, ele ficará maisculo

print('Capitalize: {}'.format(t.capitalize()))

# Title() ele vai fazer um capitalize palavra por palavra, esse quebra a frase é ultiliza os espaço para descobrir as palavras

print('title: {}\n'.format(t.title()))

# strip() - ele removerá espaços inúteis

f = "  OIIII   "

print(f)
print(f.strip())

# no Python existe codigos para tratar determinado lado,


print(f'{s * 20}\nPode parecer que não houve mundança, pórem ouve, ele apenas tirou o espaço da direita(right)\n')


print(f'Tirou o espaço da direita: {f.rstrip()}')
print(f'Tirou o espaço da esquerda: {f.lstrip()}')

# Split() - onde ouver espaço sera criado uma divisão, gerando uma lista é refazendo as fatiações, como seu eu tivesse criado uma varíavel para todas as palavras das frases
# join() - é uma junção do split, ele pode refazer o frase com alguma alteração

list = t.split()

print(f'{list}') # Lista
print(f'{list}') # Junção

