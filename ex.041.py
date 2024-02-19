from datetime import date
atual = date.today().year
naci = int(input('ano de nacimento:'))
ida = atual - naci
print('o atleta tem {} anos '.format(ida))
if ida <= 9:
    print('sua categorria é mirim')
elif ida <= 14:
    print('sua categoria é infantil')
elif ida <= 19:
    print('sua categoria é junior')
elif ida == 20:
    print('sua categoria é senior')
elif ida > 20:
    print('sua categoria é master')



