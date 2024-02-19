valor = int(input('valor das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] AVISTA DINHEIRO/CHEQUE
[ 2 ] A VISTA CARTÃO
[ 3 ] 2X NO CARTÃO
[ 4 ] 3X OU MAIS NO CARTÃO POREM COMJUROS DE 20%''')
paga = int(input('escolha uma das opeções:'))
if paga == 1:
    total = valor - (valor * 10 / 100)
    print('o produto recebe um desconto de 10% ficando de R${} para R${}'.format(valor, total))
elif paga == 2:
    total = valor - (valor * 5 / 100)
    print('o produto recebe um desconto de 5% ficando de {} paraa {}'.format(valor, total))
elif paga == 3:
    total = valor // 2
    print('parcelando o produto fica {} de {}'.format(total, valor))
elif paga == 4:
    total = (valor * 2 / 100)
    totalp = int(input('quantas parcelas vc quer faszer?'))
    final = (total + valor) // totalp
    valorp = total + valor
    print('parcelodo em {}x fica {} em {} meses no final vc tera pagado {}'.format(totalp, final, totalp, valorp))
else:
    print('algo deu errado, pfv tente denovo')
print('obrigado por comprar com a gente ;)')


