carros = []
contador = 0
while contador < 3:
    contador += 1
    item=input('Digite um carro =>')
    carros.append(item)
    print('Carros Adicionados:')
    for i in carros:
        print(i)