def idade_nasc(ano):
    idade = 2026 - ano

    if idade > 65:
        print(f'Sua idade é {idade} Idoso')
    elif idade >=18:
        print(f'Sua idade é {idade} Maior de idade')
    else:
        print(f'Sua idade é {idade} Menor de idade')

nasc=int(input('Digite o ano de nascimento '))
idade_nasc(nasc)