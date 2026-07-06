cargo=input('Digite seu cargo (caixa, vendedor ou gerente) ').upper()
if cargo=='CAIXA':
    salario = 1500
elif cargo=='VENDEDOR':
    salario = 2400
elif cargo=='GERENTE':
    salario = 4000
else:
    salario=0
    print('cargo não existe, digite o cargo válido')
inss = salario * 0.12
if salario > 2000:
    irrf = salario * 0.14
else:
    irrf = salario * 0.08
salario_final = salario - inss - irrf
print(f'Seu cargo é {cargo} teu salario é {salario} e os impostos são:')
print(f'INSS:{inss}')
print(f'IRRF:{irrf}')
print(f'salario final:{salario_final}')