txt = str(input('digite a frase:')).strip().lower()
txt2 = txt.split()
txt3 = ''.join(txt2)
inverso = ''
for txt4 in range(len(txt3) - 1, -1, -1):
    inverso += txt3[txt4]
if inverso == txt3:
    print('ele é um palindromo')
else:
    print('ele não é um palindromo')

print('o inverso de {} é {}'.format(txt3, inverso))
