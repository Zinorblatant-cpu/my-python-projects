from random import randint
from time import sleep
itens = ('pedra', 'tesoura', 'papel')
pc = randint(0,2)
print('=' * 30)
print('escolha uma das opeções')
print('''[ 0 ] Pedra
[ 1 ] tesoura
[ 2 ] papel''')
print('=' * 30)
player = int(input('qual é sua escolha? '))
print('=' * 30)
print('jo')
sleep(0.5)
print('ken')
sleep(0.5)
print('po')
sleep(0.5)
print('=' * 30)
print('vc jogou {} e eu jogeui {}'.format(itens[player],itens[pc]))
print('=' * 30)
if pc == 0:
    if player == 0:
        print('EMPATE')
    if player == 1:
        print('PERDEU')
    if player == 2:
        print('VENCEU')
if pc == 1:
    if player == 0:
        print('VENCEU')
    if player == 1:
        print('EMPATE')
    if player == 2:
        print('PERDEU')
if pc == 2:
    if player == 0:
        print('PERDEU')
    if player == 1:
        print('VENCEU')
    if player == 2:
        print('EMPATE')



