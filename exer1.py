listas = ["arros", "feijão","lasanha"]
print("esqueci o que tava na lista vc pode ver o que tem nela pfv?")
respota = str(input("[s/n]:")).lower()
if respota == "s":
    for lista in listas:
        print(lista)
else: 
    print("opeção invalida")
