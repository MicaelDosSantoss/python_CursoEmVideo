r = input('Digite o seu nome completo: ').title()

s = r.split()

print('seu primeiro nome é {}, ultimo nome é {}'.format(s[0], s[len(s)-1]  ))