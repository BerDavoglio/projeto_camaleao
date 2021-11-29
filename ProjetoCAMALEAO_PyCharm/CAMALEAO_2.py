def dis_paredex(y, raio, alt):
    """Essa função é para calcular a distancia entre a parede do eixo X com relação à carteira"""
    if y - alt >= raio * 2:
        return True
    else:
        return False


def dis_paredey(x, raio, larg):
    """Essa função é para calcular a distancia entre a parede do eixo Y com relação à carteira"""
    if x - larg >= raio * 2:
        return True
    else:
        return False


def dis_carteira(x, y, lista, raio):
    """Essa função é para fazer a distância entre o (x, y) da carteira e os (x, y) das outras carteiras,
    que serão adicionadas conforme o programa roda."""
    from math import sqrt
    for c in lista:
        if sqrt((lista[c][0] - x) ** 2 + (lista[c][1] - y) ** 2) >= raio * 2:
            return True
        else:
            return False


def distancia_total(x, y, lista, raio, alt, lar):
    """Essa função é para calcular as distancias totais"""
    if dis_paredex(y, raio, alt):
        if dis_paredey(x, raio, lar):
            if len(lista) > 0:
                if dis_carteira(x, y, lista, raio):
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
    else:
        return False


alturasala = int(input('Digite a ALTURA da sala: '))  # Altura da sala
largura = int(input('Digite a LARGURA da sala: '))  # Largura da sala
tablado = int(input('Digite o TAMANHO do tablado: '))  # Tamanho do Tablado
carteira = int(input('Digite o RAIO da carteira: '))  # Raio da carteira
esp = int(input('Digite o ESPAÇAMENTO das carteiras: '))  # Espaçamento (APENAS PARA CÁLCULOS)

altura = alturasala - tablado
n_carteiras = []

for j in range(0, altura + esp, esp):  # Loop de cada ponto do plano cartesiano
    for i in range(0, largura + esp, esp):
        if distancia_total(i, j, n_carteiras, carteira, altura, largura):
            n_carteiras.append(i)

print(n_carteiras)
