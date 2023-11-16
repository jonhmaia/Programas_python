import networkx as nx
from collections import deque
import matplotlib.pyplot as plt

# Carregar o grafo a partir do arquivo GraphML
caminho_arquivo = 'grafos/Grafo-Trabalho4.graphml'
grafo = nx.read_graphml(caminho_arquivo)

# Visualizar o grafo (opcional)
pos = nx.spring_layout(grafo)
nx.draw(grafo, pos, with_labels=True, font_weight='bold')
plt.show()

# Definir a função DFS
def dfs(grafo, vertice, visitados):
    if vertice not in visitados:
        print(vertice)
        visitados.add(vertice)
        for vizinho in grafo.neighbors(vertice):
            dfs(grafo, vizinho, visitados)

def bfs(grafo, vertice_inicial):
    fila = deque([vertice_inicial])
  
    visitados = set([vertice_inicial])

    while fila:
        vertice_atual = fila.popleft()
        print(vertice_atual)

        for vizinho in grafo.neighbors(vertice_atual):
            if vizinho not in visitados:
                fila.append(vizinho)
                visitados.add(vizinho)

# Escolher um vértice inicial para começar a busca em largura
vertice_inicial = list(grafo.nodes)[0]
# Escolher um vértice inicial para começar a busca em profundidade
vertice_inicial = list(grafo.nodes)[0]

# Iniciar a busca em profundidade
visitados = set()
dfs(grafo, vertice_inicial, visitados)
