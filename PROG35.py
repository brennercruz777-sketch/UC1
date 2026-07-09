for i in range(5):
    v=int(input('Digite um valor: '))
    r = v % 2
    if r == 1:
        print(f'O valor {v} é impar')
    else:
        print(f'O valor {v} é par')