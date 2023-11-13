from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

class Grafo:
    def __init__(self):
        self.grafo = defaultdict(list)

    def adicionar_aresta(self, u, v):
        self.grafo[u].append(v)
        self.grafo[v].append(u)

    def e_bipartido(self, vertice):
        cor = [-1] * (max(self.grafo) + 1)
        cor[vertice] = 1
        fila = [vertice]

        while fila:
            u = fila.pop(0)
            for v in self.grafo[u]:
                if cor[v] == -1:
                    cor[v] = 1 - cor[u]
                    fila.append(v)
                elif cor[v] == cor[u]:
                    return False

        return True

    def bipartido(self):
        for vertice in self.grafo:
            if not self.e_bipartido(vertice):
                return False
        return True

    def desenhar_grafo(self):
        G = nx.Graph()
        for u, vizinhos in self.grafo.items():
            for v in vizinhos:
                G.add_edge(u, v)

        pos = nx.spring_layout(G)
        cores = [cor if cor == 1 else 0 for cor in [self.e_bipartido(vertice) for vertice in G.nodes()]]
        nx.draw(G, pos, with_labels=True, node_color=cores, cmap=plt.get_cmap("coolwarm"), node_size=500)
        plt.show()

    def prim(self, vertice_inicial):
        chave = {v: float('inf') for v in self.grafo}
        chave[vertice_inicial] = 0
        mst = set()
        fila = [(0, vertice_inicial)]

        while fila:
            peso, u = fila.pop(0)
            if u not in mst:
                mst.add(u)
                for v in self.grafo[u]:
                    peso_aresta = 1  # Peso padrão, você pode ajustar isso conforme necessário
                    if v not in mst and peso_aresta < chave[v]:
                        chave[v] = peso_aresta
                        fila.append((peso_aresta, v))

        return mst

    def kruskal(self):
        arestas = []
        for u in self.grafo:
            for v in self.grafo[u]:
                arestas.append((u, v))

        arvore_geradora = set()
        conjuntos = {v: {v} for v in self.grafo}

        for u, v in arestas:
            if conjuntos[u] != conjuntos[v]:
                arvore_geradora.add((u, v))
                conjunto_u = conjuntos[u]
                conjunto_v = conjuntos[v]
                conjunto_u.update(conjunto_v)
                for w in conjunto_v:
                    conjuntos[w] = conjunto_u

        return arvore_geradora

    def desenhar_arvore_geradora(self, arvore_geradora):
        
        G = nx.Graph()
    
        for item in arvore_geradora:
            if len(item) == 2:
                u, v = item
                peso_aresta = 1  # Peso padrão, você pode ajustar isso conforme necessário
            elif len(item) == 3:
                u, v, peso_aresta = item
            else:
                raise ValueError("A árvore geradora deve conter tuplas de 2 ou 3 elementos.")

            G.add_edge(u, v, weight=peso_aresta)

        pos = nx.spring_layout(G)
        labels = {(u, v): peso['weight'] for u, v, peso in G.edges(data=True)}
        nx.draw(G, pos, with_labels=True)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()












# Exemplo de uso
grafo = Grafo()
grafo.adicionar_aresta(1, 2)
grafo.adicionar_aresta(2, 3)
grafo.adicionar_aresta(3, 4)

if grafo.bipartido():
    print("O grafo é bipartido.")
else:
    print("O grafo não é bipartido.")
grafo.desenhar_grafo()

# Exemplo de uso com árvores geradoras mínimas
arvore_geradora_kruskal = grafo.kruskal()
print("Árvore Geradora Mínima (Kruskal):", arvore_geradora_kruskal)
grafo.desenhar_arvore_geradora(arvore_geradora_kruskal)

arvore_geradora_prim = grafo.prim(1)
print("Árvore Geradora Mínima (Prim):", arvore_geradora_prim)
grafo.desenhar_arvore_geradora(arvore_geradora_prim)
