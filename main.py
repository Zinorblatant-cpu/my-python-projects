nome = str(input('qual é o seu nome ?')).strip()
if nome == 'lais':
    print('eitaa que nome bonito')
elif nome == 'pedro' or nome == 'maria':
    print('seu nome é bem popular no brasil')
elif nome in 'fiora veigar pop lulu':
    print('vc tem o nome de um personagen de lol')
else:
    print('que nome normal')
print('ola {}'.format(nome))
