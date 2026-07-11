carros={}
for i in range (2):
    carro = input('Digite um carro: ')
    marca = input('Digite a marca: ')
    valor = float(input('Digite o valor: '))
    carros[carro] = {
        'marca': marca,
        'valor': valor
    }
print(f'Lista de carros {carros}') 