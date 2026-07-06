idade=int(input('Digite sua idade '))
genero=input('Digite seu gênero (M/F) ').upper()
if idade >=18 and genero =='M':
    print('Você esta apto a servir!')
else:
    print('Você não esta apto a servir!')