print('--- COMANDA ---')
print('Digite o valor de cada item')
print('Digite 0 para encerrar')
total = 0
valor_item = 1
while valor_item != 0:
    valor_item=int(input('Digite o valor do item: '))
    total += valor_item
p = total * 1.1
print(f'O valor total da comanda com os 10% é {p}')
