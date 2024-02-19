from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for ano in range(1, 8):
    n = int(input('Em que ano a {}° pessoa nasceu?'.format(ano))) 
    idade = atual - n
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('ao todo tivemos {} de pessoas menores de idade'.format(totmenor))
