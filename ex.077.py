palavras = ('APRENDER', 
            'PROGRAMAR',
            'LINGUAGEM',
            'PYTHON',
            'CURSO',
            'ESTUDAR',
            'PRATICAR',
            'TRABALHAR',
            'MERCADO',
            'PROGRAMADOR',
            'FUTURO')
for c in palavras:
    print(f'\nna palavra {c} temos ', end='' )
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')