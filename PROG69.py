try:
    idade= int(input('Digite a sua idade:'))
    print(f'Sua idade é {idade}')
except ValueError:
    print('Digite apenas números validos!!!')