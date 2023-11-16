import networkx as nx
import matplotlib.pyplot as plt

def transformar_grafo_nao_direcionado(grafo_nao_direcionado):
    grafo_direcionado = nx.DiGraph()

    for aresta in grafo_nao_direcionado.edges():
        grafo_direcionado.add_edge(aresta[0], aresta[1])
        grafo_direcionado.add_edge(aresta[1], aresta[0])

    return grafo_direcionado


def explorar_componentes_fortemente_conexos(grafo):
    visitados = set()
    componentes_fortemente_conexos = []

    for nodo in grafo.nodes():
        if nodo not in visitados:
            componente = set()
            dfs_visit(grafo, nodo, visitados, componente)
            componentes_fortemente_conexos.append(componente)

    return componentes_fortemente_conexos

def dfs_visit(grafo, nodo, visitados, componente):
    print(f"Visitando nó {nodo}")
    visitados.add(nodo)
    componente.add(nodo)

    for vizinho in grafo.neighbors(nodo):
        if vizinho not in visitados:
            print(f"Explorando aresta de {nodo} para {vizinho}")
            dfs_visit(grafo, vizinho, visitados, componente)


caminho_arquivo = 'grafos\Grafo-Trabalho4.graphml'


grafo_nao_direcionado = nx.read_graphml(caminho_arquivo)

grafo_direcionado = transformar_grafo_nao_direcionado(grafo_nao_direcionado)


print("Grafo Não Direcionado - Nós:", grafo_nao_direcionado.nodes())
print("Grafo Não Direcionado - Arestas:", grafo_nao_direcionado.edges())


print("Grafo Direcionado - Nós:", grafo_direcionado.nodes())
print("Grafo Direcionado - Arestas:", grafo_direcionado.edges())


cfc = explorar_componentes_fortemente_conexos(grafo_direcionado)

print("Componentes Fortemente Conexos:", cfc)

plt.figure(figsize=(10, 6))
plt.title("Grafo Não Direcionado")
nx.draw(grafo_nao_direcionado, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black', font_size=8, edge_color='gray')
plt.show()
