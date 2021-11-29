class Carteira:
    def __init__(self, raio, largura, comprimento, tablado):
        self.raio = raio
        self.largura = largura
        self.comprimento = comprimento
        self.tablado = tablado

    def dist_py(self):
        """Calcula a distancia ENTRE as paredes em Y e o espaço do PROFESSOR (distancia entre a parede de baixo e parede de cima)"""
        return self.comprimento - (2 * self.raio) - self.tablado

    def dist_px(self):
        """Calcula a distancia ENTRE as paredes em X (distancia entre a parede da direita e parede da esquerda)"""
        return self.largura - 2 * self.raio
    
    def dist(self):
        from math import sqrt, floor
        return floor(sqrt(3) * self.raio)


largura_total = int(input('Digite a LARGURA da sala: '))
comprimento_total = int(input('Digite o COMPRIMENTO da sala: '))
tablado = int(input('Digite o ESPAÇO do professor: '))

raio_carteira = int(input('Digite o RAIO das Carteiras: '))

cart = Carteira(raio_carteira, largura_total, comprimento_total, tablado)
px_calc = cart.dist_px() # DIREITA E ESQUERDA
py_calc = cart.dist_py() # FUNDO E PROFESSOR
y = cart.dist()
lista_carteiras = []
contador = 1

for j in range(0, py_calc + y, y):
    if contador % 2 == 0:
        for i in range(raio_carteira, px_calc + 2 * raio_carteira, 2 * raio_carteira):
            lista_carteiras.append((i, j))
    else:
        for i in range(0, px_calc + 2 * raio_carteira, 2 * raio_carteira):
            lista_carteiras.append((i, j))
    contador += 1        

for ind, qq in enumerate(lista_carteiras):
    print(f'Carteira {ind + 1}: {qq}')
