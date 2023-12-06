import networkx as nx
import matplotlib.pyplot as plt
def dfs(grafo, vertice, visitados, tempos):
    print(f"Visitando {vertice} - Tempo Inicial: {tempos['tempo']}")
    visitados.add(vertice)
    tempos['descoberta'][vertice] = tempos['tempo']
    tempos['tempo'] += 1

    for vizinho in grafo.neighbors(vertice):
        if vizinho not in visitados:
            dfs(grafo, vizinho, visitados, tempos)

    tempos['finalizacao'][vertice] = tempos['tempo']
    tempos['tempo'] += 1
    print(f"Finalizando {vertice} - Tempo Final: {tempos['tempo']}")
# Função DFS para o algoritmo de Tarjan
def dfs_tarjan(grafo, v, index, lowlink, stack, on_stack, components):
    index[v] = len(index)
    lowlink[v] = index[v]
    stack.append(v)
    on_stack.add(v)

    for neighbor in grafo.neighbors(v):
        if neighbor not in index:
            dfs_tarjan(grafo, neighbor, index, lowlink, stack, on_stack, components)
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

# Carregar o grafo a partir do arquivo GraphML
caminho_arquivo = 'grafos/Grafo-Trabalho4.graphml'
grafo = nx.read_graphml(caminho_arquivo)

# Mostrar o grafo original
plt.figure(figsize=(10, 5))
plt.subplot(121)
plt.title('Grafo Original')
pos = nx.spring_layout(grafo)
nx.draw(grafo, pos, with_labels=True, font_weight='bold')

# Inicializar tempos
tempos_dfs_original = {'descoberta': {}, 'finalizacao': {}, 'tempo': 1}

# Escolher um vértice inicial que exista no grafo original
vertice_inicial_dfs_original = list(grafo.nodes)[0]

# Executar DFS no grafo original
visitados_dfs_original = set()
dfs(grafo, vertice_inicial_dfs_original, visitados_dfs_original, tempos_dfs_original)

# Mostrar o grafo transposto
grafo_transposto = grafo.reverse()

plt.subplot(122)
plt.title('Grafo Transposto')
pos_transposto = nx.spring_layout(grafo_transposto)
nx.draw(grafo_transposto, pos_transposto, with_labels=True, font_weight='bold')
plt.show()

# Exibir tempos para o grafo original
print("\nTempos de execução para o grafo original:")
print("Tempos de descoberta:", tempos_dfs_original['descoberta'])
print("Tempos de finalização:", tempos_dfs_original['finalizacao'])

# Aplicar o algoritmo de Tarjan no grafo original
index_tarjan = {}
lowlink_tarjan = {}
stack_tarjan = []
on_stack_tarjan = set()
components_tarjan = []

for node in grafo.nodes:
    if node not in index_tarjan:
        dfs_tarjan(grafo, node, index_tarjan, lowlink_tarjan, stack_tarjan, on_stack_tarjan, components_tarjan)

# Criar grafo dos componentes fortemente conectados
grafo_scc = nx.DiGraph()
for component in components_tarjan:
    if len(component) > 1:
        for i in range(len(component) - 1):
            grafo_scc.add_edge(component[i], component[i + 1])

# Mostrar o grafo dos componentes fortemente conectados
plt.figure(figsize=(6, 6))
plt.title('Grafo dos Componentes Fortemente Conectados')
pos_scc = nx.spring_layout(grafo_scc)
nx.draw(grafo_scc, pos_scc, with_labels=True, font_weight='bold')
plt.show()
