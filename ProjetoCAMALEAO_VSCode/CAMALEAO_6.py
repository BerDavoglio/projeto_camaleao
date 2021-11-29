from math import sqrt, pow, floor


largura_sala = int(input('Digite a LARGURA da sala (cm): '))
altura_sala = int(input('Digire a ALTURA da sala (cm): '))
raio_carteiras = int(input('Digite o RAIO das carteiras (cm): '))
tablado = int(input('Digite o TAMANHO do tablado do professor (cm): '))


altura_sala -= tablado
'''Altura da sala desconsiderando o tablado,
e guardando a distancia do fundo para o aluno nao encostar na parede'''

largura_sala -= (raio_carteiras* 2)
'''Largura da sala desconsiderando a guarda lateral para o aluno nao tocar a parede'''

distancia_y = floor(sqrt(pow(2 * raio_carteiras, 2) - pow(raio_carteiras, 2)))
'''essa distância funciona quase como o "passo" do programa anterior, vai ser a distância no eixo Y 
entre as fileiras de carteiras'''

l_carteiras = []  # Lista com as coordenadas das cadeiras

count = 1
for j in range(raio_carteiras, altura_sala - raio_carteiras + distancia_y, distancia_y):
    for i in range(raio_carteiras, largura_sala - raio_carteiras, raio_carteiras):
        if count % 2 != 0:
            if i % 2 == 1:
                l_carteiras.append((i, j))
        elif count % 2 == 0:
            if i % 2 == 0:
                l_carteiras.append((i, j))
    count += 1

for carteira in l_carteiras:
    print(f'Carteira {l_carteiras.index(carteira) + 1} {carteira}')
