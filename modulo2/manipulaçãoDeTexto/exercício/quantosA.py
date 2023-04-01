r = input('Digite uma frase: ').upper()


print('A palavra {} tem um total de {} A\nprimeiro A {}\nultima A {}'.format(r, r.count('A'), r.find('A')+1, r.rfind('A')))

# rfind começou a pesquisa do lado ao contrario