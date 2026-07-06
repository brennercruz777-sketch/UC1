i=int(input('Digite sua idade '))
ing=input('Você possui o ingresso (S-Sim / N-Não)? ').upper()
if i >=12 and ing=='S':
    print('Acesso liberado!')
elif i <12 and ing=='S':
    print('Você tem ingresso mas não possui a idade mínima!')
else:
    print('Você precisa de ingresso!')