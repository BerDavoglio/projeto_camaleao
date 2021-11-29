class Carteira:
    """Carteira é a classe do objeto Carteira"""
    def __init__(self, posx, posy, raio, lista):
        self.posx = posx
        self.posy = posy
        self.raio = raio
        self.lista = lista

    def distancia_x(self, sala_y):
        """Essa função é para calcular a distancia entre a parede do eixo X com relação à carteira"""
        if sala_y - self.posy >= self.raio and sala_y >= self.raio:
            return True
        else:
            return False

    def distancia_y(self, sala_x):
        """Essa função é para calcular a distancia entre a parede do eixo Y com relação à carteira"""
        if sala_x - self.posx >= self.raio and sala_x >= self.raio:
            return True
        else:
            return False

    def distancia_carteira(self):
        """Essa função é para fazer a distância entre o (x, y) da carteira e os (x, y) das outras carteiras,
            que serão adicionadas conforme o programa roda."""
        if len(self.lista) > 0:
            for c in self.lista:
                from math import sqrt
                if sqrt((c[0] - self.posx) ** 2 + (c[1] - self.posy) ** 2) >= self.raio * 2:
                    return True
                else:
                    return False
        else:
            return True

    def distancia_total(self):
        """Essa função é para calcular as distancias totais"""
        if self.distancia_x(altura):
            if self.distancia_y(largura):
                if self.distancia_carteira():
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False


largura = int(input('Digite a LARGURA da sala: '))  # Largura da sala
altura_sala = int(input('Digite a ALTURA da sala: '))  # Altura da sala
tablado = int(input('Digite o TAMANHO do tablado: '))  # Tamanho do Tablado
carteira = int(input('Digite o RAIO da carteira: '))  # Raio da carteira
esp = int(input('Digite o ESPAÇAMENTO das carteiras: '))  # Espaçamento (APENAS PARA CÁLCULOS)

altura = altura_sala - tablado
n_carteiras = []

for j in range(0, altura + esp, esp):  # Loop de cada ponto do plano cartesiano
    for i in range(0, largura + esp, esp):
        cart = Carteira(i, j, carteira, n_carteiras)
        if cart.distancia_total():
            n_carteiras.append((i, j))

for i, c in enumerate(n_carteiras):
    print(f'Carteira {i} -> {c}')
