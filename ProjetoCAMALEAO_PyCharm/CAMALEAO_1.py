from math import sqrt, pow

"""TODAS AS MEDIDAS ESTÃO EM cm!!!"""


class Carteira:
    def __init__(self, raio, x, y):
        self.raio = raio
        self.x = x
        self.y = y

    def distancia_carteira(self, pontox, pontoy):
        """Essa função é para fazer a distância entre o (x, y) da carteira e os (x, y) das outras carteiras,
        que serão adicionadas conforme o programa roda."""
        if sqrt(((pontox - self.x) ** 2) + ((pontoy - self.y) ** 2)) >= (self.raio * 2):
            return True
        else:
            return False

    def distancia_paredex(self, altura):
        """Essa função é para calcular a distancia entre a parede do eixo X com relação à carteira"""
        if abs(self.x - altura) >= self.raio:
            return True
        else:
            return False

    def distancia_paredey(self, largura):
        """Essa função é para calcular a distancia entre a parede do eixo Y com relação à carteira"""
        if abs(self.y - largura) >= self.raio:
            return True
        else:
            return False

    def distancia_total(self, alturatot, larguratot, lista):
        """Essa função é para calcular as distancias totais"""
        if self.distancia_paredex(alturatot):
            if self.distancia_paredey(larguratot):
                if len(lista) != 0:
                    for c in lista:
                        if self.distancia_carteira(c[0], c[1]):
                            return True
                else:
                    return True
            else:
                return False
        else:
            return False


carteiras_colocadas = []  # Lista das carteiras

larg = int(input('Digite a LARGURA da sala (em cm): '))  # Largura da sala
altu = int(input('Digite a ALTURA da sala (em cm): '))  # Altura da sala

tablado = int(input('Digite o TAMANHO do tablado (em cm): '))  # Tamanho do tablado
altunova = altu - tablado

raio_carteira = int(input('Digite a DISTÂNCIA entre as carteiras (em cm): '))  # Distancias entre carteira
raio_carteira /= 2
esp = int(input('Digite o ESPAÇAMENTO: '))  # Espaçamento (APENAS PARA CÁLCULOS)

for j in range(0, altunova + esp, esp):  # Loop de cada ponto do plano cartesiano
    for i in range(0, larg + esp, esp):
        cart = Carteira(raio_carteira, i, j)
        if cart.distancia_total(altunova, larg, carteiras_colocadas):
            tupla = (i, j)
            carteiras_colocadas.append(tupla)
        else:
            pass

for indice, ca in enumerate(carteiras_colocadas):
    print(f'Carteira {indice} = {ca}')
