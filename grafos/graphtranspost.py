import networkx as nx
import matplotlib.pyplot as plt

# Função DFS
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

# Inicializar tempos para o grafo transposto
tempos_dfs_transposto = {'descoberta': {}, 'finalizacao': {}, 'tempo': 1}

# Escolher um vértice inicial que exista no grafo transposto
vertice_inicial_dfs_transposto = list(grafo_transposto.nodes)[0]

# Executar DFS no grafo transposto
visitados_dfs_transposto = set()
dfs(grafo_transposto, vertice_inicial_dfs_transposto, visitados_dfs_transposto, tempos_dfs_transposto)

plt.show()

# Exibir tempos para o grafo original
print("\nTempos de execução para o grafo original:")
print("Tempos de descoberta:", tempos_dfs_original['descoberta'])
print("Tempos de finalização:", tempos_dfs_original['finalizacao'])
print("################\n################")
# Exibir tempos para o grafo transposto
print("\nTempos de execução para o grafo transposto:")
print("Tempos de descoberta:", tempos_dfs_transposto['descoberta'])
print("Tempos de finalização:", tempos_dfs_transposto['finalizacao'])
