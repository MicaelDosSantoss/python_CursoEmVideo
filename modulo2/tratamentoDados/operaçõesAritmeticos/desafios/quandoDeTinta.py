l = float(input('Largura da parede ? '))
a = float(input('Altura da parede ? '))

total = l * a

print('Largura {:.2f} x Altura {:.2f} total de {}m3, você precisará de {}L'.format(l,a,total, (total / 2)))