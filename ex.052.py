n = int(input('digite um numerio:'))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end='')
        tot +=1
    else:
        print('\033[35m', end='')
    print('{} '.format(c), end='')
print('\n\033[mo numero {} foi divisivel {} vezes'.format(n, tot))
if tot == 2:
    print('ele é um numero primo')
else:
    print('ele não é um numero primo')

