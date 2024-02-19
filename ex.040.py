nota1 = int(input('nota do trabalho:'))
nota2 = int(input('nota da prova'))
media = (nota1 + nota2) / 2
if media >= 5 and media < 7:
    print('sua nota foi {} vc esta de recuperação'.format(media))
elif media > 7:
    print('sua nota foi {} vc esta aprovado'.format(media))
elif media < 5:
    print('sua nota foi {} vc esta reprovado'.format(media))
