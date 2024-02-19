lista = ('laips', 1.75, 
        'borracha', 2, 
        'caderno', 15.90, 
        'estojo', 25, 
        'transferidor', 4.20,
        'compasso', 9.99, 
        'mochila', 120.32, 
        'canetas', 22.30, 
        'livro', 34.90)
print("-" * 27)
print("Litsa De Preços")
print("-" * 27)
for itens in range(0, len(lista)):
    if itens % 2 == 0:
        print(f'{lista[itens]:.<20}' , end="")
    else:
        print(f'R${lista[itens]:>1}')