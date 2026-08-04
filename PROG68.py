class Passarinho:
    def __init__(self, raca, cor):
        self.raca = raca
        self.cor = cor

    def cantar(self):
        return f'{self.raca} canta pi pi pi'

passaro1 = Passarinho('canário', 'amarelo')
passaro2 = Passarinho('calopsita', 'verde')

print(f'{passaro1.raca} com a cor {passaro1.cor}')
print(passaro1.cantar())