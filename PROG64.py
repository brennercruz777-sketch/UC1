mercado = []
produto=" "
while produto != "sair":
    produto=input("Digite um produto (ou digite 'sair') =>").lower()
    if produto == "sair":
        break
    if produto in mercado:
        print('Produto já cadastrado!')
    else:
        mercado.append(produto)
        print('\nLista do Mercado:')
        for x in mercado:
            print(x)