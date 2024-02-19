vlc = float(input("qual é o valor da casa?"))
salario = float(input("qula é o seu salario?"))
t = int(input("quantos anos vc quer pagar"))
par = vlc // t
por100 = salario * 30 // 100
if por100 == par or por100 > par:
    print('vc consiguira pagar a casa e vc gastara {} por mes'.format(por100))
else:
    print("vc nao consegui pagar a casa")
