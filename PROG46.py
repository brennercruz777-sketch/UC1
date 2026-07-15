print('--- CAIXA SUPERMERCADO ---')
print('Produtos: 001(Arroz: R$ 4) | 002(Feijão: R$ 7) | 003(Macarrão: R$ 5)')
print('Digite 0 para encerrar a compra.')

soma = 0
codigo = 1

while codigo != '0':
    codigo = input('Digite um código: ')
    if codigo == '001':
        print('Arroz Adicionado')
        soma += 4
    elif codigo == '002':
        print('Feijão Adicionado')
        soma += 7
    elif codigo == '003':
        print('Macarrão Adicionado')
        soma += 5
    elif codigo != '0':
        print('Código inválido')
        
print(f'Total da compra: R$ {soma}')