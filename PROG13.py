anon = int(input('Digite o ano de nascimento '))
anoa = int(input('Digite o ano atual '))
idade = anoa - anon
if idade >=18:
    print(f'Sua idade é {idade} Maior de idade')
else:
    print(f'Sua idade é {idade} Menor de idade')
