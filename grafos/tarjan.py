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
def dfs(grafo, vertice, visitados, stack):
    if vertice not in visitados:
        print(vertice)
        visitados.add(vertice)
        stack.append(vertice)

        for vizinho in grafo.neighbors(vertice):
            dfs(grafo, vizinho, visitados, stack)

def dfs_visit(grafo, nodo, visitados, componente):
    print(f"Visitando nó {nodo}")
    visitados.add(nodo)
    componente.add(nodo)

    for vizinho in grafo.neighbors(nodo):
        if vizinho not in visitados:
            print(f"Explorando aresta de {nodo} para {vizinho}")
            dfs_visit(grafo, vizinho, visitados, componente)

# Algoritmo de Tarjan
def tarjan(grafo):
    index = {}
    lowlink = {}
    stack = []
    on_stack = set()
    components = []

    def dfs_tarjan(v):
        nonlocal index, lowlink, stack, on_stack, components

        index[v] = len(index)
        lowlink[v] = index[v]
        stack.append(v)
        on_stack.add(v)

        for neighbor in grafo.neighbors(v):
            if neighbor not in index:
                dfs_tarjan(neighbor)
                lowlink[v] = min(lowlink[v], lowlink[neighbor])
            elif neighbor in on_stack:
                lowlink[v] = min(lowlink[v], index[neighbor])

        if lowlink[v] == index[v]:
            component = []
            while True:
                w = stack.pop()
                on_stack.remove(w)
                component.append(w)
                if w == v:
                    break
            components.append(component)

    for node in grafo.nodes:
        if node not in index:
            dfs_tarjan(node)

    return components

# Algoritmo de Tarjan
components_tarjan = tarjan(grafo)
print("Componentes fortemente conectados:")
for component in components_tarjan:
    print(component)



vertice_inicial_dfs = list(grafo.nodes)[0]

visitados_dfs = set()
stack_dfs = []
dfs(grafo, vertice_inicial_dfs, visitados_dfs, stack_dfs)
visitados_dfs = set()
componente_dfs = set()
dfs_visit(grafo, vertice_inicial_dfs, visitados_dfs, componente_dfs)

print("Resultado da busca em profundidade (abordagem recursiva):")
print(componente_dfs)
