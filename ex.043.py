peso = float(input('Qual é seu pesso?  (Kg) '))
altura = float(input('qual é sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é {:.1f}'.format(imc))
if imc < 18.5:
    print('vc esta magro')
elif imc >= 18.5 and imc <= 24.9:
    print('vc esta normal')
elif imc >= 25.0 and imc <= 29.9:
    print('vc esta sobrepeso  grau 1')
elif imc >= 30.0 and imc <= 39.9:
    print('vc esta em obesidade grau 2')
elif imc > 40:
    print('vc es com obesidade grave grau 3')
else:
    print('algo deui de erado tente denovo')
