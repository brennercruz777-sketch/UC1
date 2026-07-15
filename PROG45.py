soma = 0
numero = 1
numero = int(input('Digite um número (0 = parar): '))
while numero != 0:
    soma = soma + numero
    numero = int(input("Digite um número (0 = parar): "))
print(f'A soma dos números digitados é {soma}')