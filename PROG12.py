nome = input('Digite seu nome ')
n1 = float(input('Digite sua primeira nota '))
n2 = float(input('Digite sua segunda nota '))
n3 = float(input('Digite sua terceira nota '))
n4 = float(input('Digite sua quarta nota '))
m = (n1+n2+n3+n4)/4
print(f'{nome} sua média é {m}')
if m >=6:
    print('Aprovado')
else:
    print('Recuperação')