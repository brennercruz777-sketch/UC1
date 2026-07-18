cursos = ['Barbeiro','Gastronomia']
item=input('Digite um curso =>')
cursos.append(item)
print('Listagem de cursos:')
for x in cursos:
    print(x)
print('Escolha um curso para excluir:')
exclu=input('Exclua um curso =>')
cursos.remove(exclu)
for x in cursos:
    print(x)