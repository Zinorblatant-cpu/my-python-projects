print('='*20)
print('10 termos de uma PA')
print('='*20)
p1 = int(input('Primero termo'))
r = int(input('razão'))
d = p1 + (10-1) * r
for c in range(p1, d, r):
    print('{}'.format(c), end= '->')
print('final da PA')
