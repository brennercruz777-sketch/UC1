for i in range(1,5):
    a=input('Digite o nome do aluno ')
    n1=float(input('Digite a primeira nota '))
    n2=float(input('Digite a segunda nota '))
    n3=float(input('Digite a terceira nota '))
    m = (n1 + n2 + n3)/3
    if m >=7:
        print(f'{a} suas notas são {n1}, {n2} e {n3}  sua media é {m:.2f} | Aprovado!')
    elif m >=5:
        print(f'{a} sua media é {m:.2f} | Recuperação!')
    else:
        print(f'{a} sua media foi menor que 5 | Reprovado!')