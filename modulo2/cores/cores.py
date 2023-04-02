#Cores para o termial

# É possível colocar 3 códigos, sytle,text,back


# STYLE receberá 0,1,4,7

print('='*20,'\n \033[1;35m SYTLE \033[m \n','='*20,'\n') 

# 0 = sem nenhum estilo:
print('\033[0m Sem estilo\033[m')

# 1 = ficará em negrito(bold):
print('\033[1m Negrito\033[m')

# 4 - ficará subliado(underline):
print('\033[4m Subliado/Underline \033[m')

# 7 - ficará invertido as cores (Negative)
print('\033[7m Negativo \033[m \n')

print('='*20, '\n \033[1;35m CORES \033[m \n', '='*20)


# Cores receberá 30,31,32,33,34,35,36,37

# 30 - Branco
print('\n \033[1;30m BRANCO \033[m')

# 31 - Vermelho
print('\033[1;31m VERMELHO \033[m')

# 32 - Verde
print('\033[1;32m VERDE \033[m')

# 33 - Amarelo
print('\033[1;33m AMARELO \033[m')

# 34 - Azul
print('\033[1;34m AZUL \033[m')

# 35 - Roxo
print('\033[1;35m ROXO \033[m')

# 36 - Turquesa
print('\033[1;36m TURQUESA \033[m') 

# 37 - Cinza
print('\033[1;37m CINZA \033[m \n')

print('=' * 20, '\n \033[1;35m BACK \033[m \n','=' * 20)

# No back são os mesmos padrões de cores pórem você além de colocar o 3 você precisa colocar o 4:

# 40 - Branco
print('\n \033[1;30;40m BRANCO \033[m')

# 41 - Vermelho
print('\033[1;30;41m VERMELHO \033[m')

# 42 - Verde
print('\033[1;30;42m VERDE \033[m ')

# 43 - Amarelo
print('\033[1;30;43m AMARELO \033[m ')

# 44 - Azul
print('\033[1;30;44m AZUL \033[m ')

# 45 - Roxo
print('\033[1;30;45m ROXO \033[m ')

# 46 - Turquesa
print('\033[1;30;46m TURQUESA \033[m ')

# 47 - Cinza
print('\033[1;30;47m CINZA \033[m ')

# print('=-='*20,'\n \033[30;41mTeste\033[m \n','=-='*20)

print(19 // 2)
print(19 % 2)