class Biscoito:
    def __init__(self, sabor, gosto):
        self.sabor = sabor
        self.gosto = gosto

    def croc(self):
        return f'O sabor {self.sabor} faz croc croc'

bisc1 = Biscoito('limão', 'laranja')
bisc2 = Biscoito('chocolate', 'morango')

print(f'O biscoito tem sabor de {bisc2.sabor} e gosto de {bisc2.gosto}')
print(bisc2.croc())
print(f'O biscoito tem sabor de {bisc1.sabor} e gosto de {bisc1.gosto}')
print(bisc1.croc())