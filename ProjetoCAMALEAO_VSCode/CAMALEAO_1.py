from math import sqrt


class Carteira:
    def __init__(self, raio, posx, posy):
        self.raio = raio
        self.posx = posx
        self.posy = posy

    def d_parede_x(self, altura):
        """Distância entre a PAREDE do eixo X (tanto superior quanto inferior) e a CARTEIRA observada no momento
         - A ALTURA é o valor da ALTURA da SALA"""
        if self.posy >= self.raio and self.posy <= altura - self.raio:
            return True
        return False
    
    def d_parede_y(self, largura):
        """Distância entre a PAREDE do eixo Y (tanto direita quanto esquerda) e a CARTEIRA observada no momento
         - A LARGURA é o valor da LARGURA da SALA"""
        if self.posx >= self.raio and self.posx <= largura - self.raio:
            return True
        return False
    
    def d_carteira(self, lista1, lista2):
        """Distância entre as CARTEIRAS presentes na LISTA (1 e 2) até a CARTEIRA observada no momento
         - A LISTA1 é das coordenadas em X das carteiras, ja a LISTA 2 é das coordenadas em Y
         (CASO AINDA NÃO TENHA SELECIONADO NENHUMA CARTEIRA, A LISTA DEVE SER VAZIA)"""
        if len(lista1) > 0 and len(lista2) > 0:
            for c in range(0, len(lista1) + 1):
                if sqrt(((lista1[c] - self.posx) ** 2) + ((lista2[c] - self.posy)) ** 2) >= self.raio * 2:
                    return True
                else:
                    return False
        else:
            return True
    
    def d_total(self):
        """Calcula a DISTÂNCIA TOTAL, levando em consideração todos os parâmetros ja escolhidos
         - A ALT na primeira função puxa direto a ALTURA da sala
         - A LAR na segunda função puxa direto a LARGURA da sala
         - A L_CARTEIRAS_X, L_CARTEIRAS_Y na terceira função puxa direto a LISTA DE CARTEIRAS (TANTO EM X QUANTO EM Y)"""
        if self.d_parede_x(alt):
            if self.d_parede_y(lar):
                if self.d_carteira(l_carteiras_x, l_carteiras_y):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False


lar = int(input('Digite a LARGURA da sala (EIXO X/EM cm): '))
alt_parcial = int(input('Digite a ALTURA da sala (EIXO Y/EM cm): '))
tablado = int(input('Digite o TAMANHO do tablado (Espaço do Professor/EM cm): '))
alt = alt_parcial - tablado
l_carteiras_x = [] # Coordenadas X das carteiras
l_carteiras_y = [] # Coordenadas Y das carteiras

raio_carteiras = int(input('Digite o RAIO das carteiras (EM cm): '))
passo = 5

for j in range(0, alt + passo, passo):
    for i in range (0, lar + passo, passo):
        """Esses dois FOR são para rodar todos os pontos I x J da sala, sendo o PASSO a dstância entre cada ponto,
        podendo ser alterado, caso seja necessario. (PADRÃO: 5cm)"""
        cart = Carteira(raio_carteiras, i, j)
        if cart.d_total():
            l_carteiras_x.append(i)
            l_carteiras_y.append(j)

if len(l_carteiras_x) == len(l_carteiras_y):
    for c in range(0, len(l_carteiras_x) + 1):
        print(f'A carteira {c} é ({l_carteiras_x[c]}, {l_carteiras_y[c]})')
        # input('Próxima Carteira...') # APENAS PARA TER UM CONTROLE MAIOR DE CADA CARTEIRA
else:
    print('HOUVE ALGUM PROBLEMA...')

# O programa esta fazendo a verificação da distancia das paredes, mas não esta fazendo a verificação entre as carteiras.
