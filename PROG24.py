n1=float(input('Digite o primeiro número '))
n2=float(input('Digite o segundo número '))

print('1 - Somar')
print('2 - Subtrair')
print('3 - Multiplicar')
print('4 - Dividir')

opcao=int(input('Escolha uma opção '))
match opcao:
    case '1':
        resultado = n1 + n2
    case '2':
        resultado = n1 - n2
    case '3':
        resultado = n1 * n2
    case '4':
        resultado = n1 / n2
    case _:
        resultado=0
        print('Opção Invalida')
print(f'O resultado é {resultado}')
