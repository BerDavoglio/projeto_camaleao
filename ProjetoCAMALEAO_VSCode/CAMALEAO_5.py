class Carteira:
    def __init__(self, raio, altura, comprimento, tablado):
        self.raio = raio
        self.altura = altura
        self.comprimento = comprimento
        self.tablado = tablado

    def dist_px(self):
        """Calcula a distancia ENTRE as paredes em X e o espaço do PROFESSOR (distancia entre a parede de baixo e parede de cima)"""
        return self.altura - (2 * self.raio) - self.tablado

    def dist_py(self):
        """Calcula a distancia ENTRE as paredes em Y (distancia entre a parede da direita e parede da esquerda)"""
        return self.comprimento - 2 * self.raio
    
    def dist(self):
        from math import sqrt, floor
        return floor(sqrt(3) * self.raio)


altura_total = int(input('Digite a ALTURA da sala: '))
comprimento_total = int(input('Digite o COMPRIMENTO da sala: '))
tablado = int(input('Digite o ESPAÇO do professor: '))

raio_carteira = int(input('Digite o RAIO das Carteiras: '))

cart = Carteira(raio_carteira, altura_total, comprimento_total, tablado)
px_calc = cart.dist_px() # DIREITA E ESQUERDA
py_calc = cart.dist_py() # FUNDO E PROFESSOR
y = cart.dist() # DISTÂNCIA ENTRE AS LINHAS
lista_carteiras = []
contador = 1

for j in range(0, px_calc + y, y):
    for i in range(0, py_calc + raio_carteira, 2 * raio_carteira):
        if contador % 2 == 0:
            if (i % raio_carteira) % 2 == 1:
                lista_carteiras.append((i, j))
        else:
            if (i % raio_carteira) % 2 == 0:
                lista_carteiras.append((i, j))
    contador += 1

for ind, qq in enumerate(lista_carteiras):
    print(f'Carteira {ind}: {qq}')
