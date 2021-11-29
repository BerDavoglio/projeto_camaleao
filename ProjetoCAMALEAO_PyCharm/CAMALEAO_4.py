from math import sqrt, pow


class Carteira:
    def __init__(self, posx, posy):
        self.raio = raio_carteiras
        self.posx = posx
        self.posy = posy

    def d_parede_x(self):
        """Distância entre a PAREDE do eixo X (tanto superior quanto inferior) e a CARTEIRA observada no momento
         - A ALTURA é o valor da ALTURA da SALA"""
        if self.posy >= self.raio and self.posy <= altura - self.raio:
            return True
        return False

    def d_parede_y(self):
        """Distância entre a PAREDE do eixo Y (tanto direita quanto esquerda) e a CARTEIRA observada no momento
         - A LARGURA é o valor da LARGURA da SALA"""
        if self.posx >= self.raio and self.posx <= largura - self.raio:
            return True
        return False

    def d_tot(self):
        if self.d_parede_x():
            if self.d_parede_y():
                return True
            else:
                return False
        else:
            return False


def d_carteira(px1, py1, px2, py2):
    return sqrt(pow((px2 - px1), 2) + pow((py2 - py1), 2))


largura = int(input('Digite a LARGURA da sala (EIXO X/EM cm): '))
alt_parcial = int(input('Digite a ALTURA da sala (EIXO Y/EM cm): '))
tablado = int(input('Digite o TAMANHO do tablado (Espaço do Professor/EM cm): '))
altura = alt_parcial - tablado

raio_carteiras = int(input('Digite o RAIO das carteiras (EM cm): '))
passo = 10

l_carteiras = []  # Coordenadas das carteiras

for j in range(0, altura + passo, passo):
    for i in range(0, largura + passo, passo):
        """Esses dois FOR são para rodar todos os pontos I x J da sala, sendo o PASSO a dstância entre cada ponto,
        podendo ser alterado, caso seja necessario. (PADRÃO: 5cm)"""
        cart = Carteira(i, j)
        if cart.d_tot():
            l_carteiras.append((i, j))

"""for a in l_carteiras:
    # Terá que pegar a posição do 'a' na lista e verificar os pontos anteriores apenas, os posteriores não!
    posa = int(l_carteiras.index(a))
    if posa > 0:
        for b in l_carteiras:
            if b != a and l_carteiras.index(b) < l_carteiras.index(a):
                if d_carteira(a[0], a[1], b[0], b[1]) < (raio_carteiras * 2):
                    l_carteiras.remove(b)"""

"""lista2 = []
lista3 = []
for a in l_carteiras:
    posa = int(l_carteiras.index(a))
    if posa > 0:
        # [pon1, pon2, pon3, ..., pon n]
        for b in l_carteiras:
            while l_carteiras.index(b) < l_carteiras.index(a):
                lista2.append(b)
            for c in lista2:
                if d_carteira(a[0], a[1], c[0], c[1]) > (2 * raio_carteiras):
                    lista3.append(c)"""

lista2 = []
for a in l_carteiras:
    # Terá que pegar a posição do 'a' na lista e verificar os pontos anteriores apenas, os posteriores não!
    posa = int(l_carteiras.index(a))
    if posa > 0:
        tamanho = len(l_carteiras)
        for alfa in range(0, tamanho, -1):
            if l_carteiras[alfa] != a and l_carteiras.index(l_carteiras[alfa]) > l_carteiras.index(a):
                if d_carteira(a[0], a[1], l_carteiras[alfa][0], l_carteiras[alfa][1]) >= (raio_carteiras * 2):
                    lista2.append(a)

for ind, qq in enumerate(lista2):
    print(f'Carteira {ind}: {qq}')

# 'Deu' certo, tem que fazer alguns ajustes, mas podemos dizer q, a principio, deu boa!
