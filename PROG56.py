def notas(n1,n2,n3,n4):
    media = (n1 + n2 + n3 + n4)/4
    if media >=7:
        print(f'Sua média é {media} Aprovado')
    elif media >=5:
        print(f'Sua média é {media} Recuperação')
    else:
        print(f'Sua média é {media} Reprovado')

n1=float(input('Digite sua primeira nota '))
n2=float(input('Digite sua segunda nota '))
n3=float(input('Digite sua terceira nota '))
n4=float(input('Digite sua quarta nota '))
notas(n1,n2,n3,n4)