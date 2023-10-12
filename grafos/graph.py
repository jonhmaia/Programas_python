from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt
"""
Um grafo é bipartido se for possível dividir seus vértices em dois conjuntos disjuntos, 
chamados de "conjunto A" e "conjunto B".
Todas as arestas do grafo devem conectar um vértice do "conjunto A" a um vértice do "conjunto B". 
Não deve haver arestas que conectem vértices do mesmo conjunto.
Não deve haver ciclos ímpares no grafo. 
o comprimento de qualquer ciclo no grafo deve ser um número par. 
Isso ocorre porque, em um grafo bipartido, os vértices em qualquer ciclo devem alternar 
entre os conjuntos A e B para evitar que os vértices do mesmo conjunto se conectem diretamente.
"""


class Grafo:
    def __init__(self):  # inicializa o grafo
    # cria o dicinário que é uma lsita vazia para adicionar as arestas
        self.grafo = defaultdict(list)  #

    # recebe o método self e os parametros u e v que são as arestas do grafo
    def adicionar_aresta(self, u, v):
        self.grafo[u].append(v)
        self.grafo[v].append(u)

    # usando a lógica de colorir e que vertices vizinho não podem ter a mesma cor, cria-se a lista
    # cor que recebe -1 para todos os vertices, e a cor do vertice inicial recebe 1
    """
    Usa-se uma fila para percorrer( primeiro a entrar é o primeiro a sair, ou seja,
    o primeiro a entrar é o primeiro a ser processado) para atribuir cores aos vértices.
    Usa um loop enquanto a fila não estiver vazia.
    Retira o primeiro vértice da fila e o armazenamos em u.
    pelos vértices adjacentes a u e verifica-se se eles têm uma cor atribuída.
    Se o vértice v não tiver cor, atribuímos uma cor oposta à de u (0 se u for 1, e vice-versa) 
    e adiciona v à fila para processamento.
    Se v tiver a mesma cor que u, o grafo não é bipartido, e retornamos False."""

    def e_bipartido(self, vertice):  # recebe o vertice
        cor = [-1] * (max(self.grafo) + 1)
        # cria uma lista de cores com -1 para todos os vertices
        cor[vertice] = 1
        # o vertice inicial recebe 1
        fila = [vertice]
        # cria uma fila com o vertice inicial

        while fila:
            # enquanto a fila não estiver vazia
            u = fila.pop(0)
            # retira o primeiro vertice da fila e armazena em u
            for v in self.grafo[u]:
                # percorre os vertices adjacentes a u
                if cor[v] == -1:
                    # se o vertice não tiver cor
                    cor[v] = 1 - cor[u]
                    # atribui uma cor oposta a de u
                    fila.append(v)
                    # adiciona v a fila para processamento
                elif cor[v] == cor[u]:
                    # se v tiver a mesma cor que u
                    return False
                # o grafo não é bipartido

        return True


    def bipartido(self):
        for vertice in self.grafo:
            if not self.e_bipartido(vertice):
                return False
        return True
    def desenhar_grafo(self):# desenha o grafo
            G = nx.Graph()
            # cria um grafo
            for u, vizinhos in self.grafo.items():
                # percorre os vertices e seus vizinhos
                for v in vizinhos:
                    # percorre os vizinhos
                    G.add_edge(u, v)
                    # adiciona as arestas

            pos = nx.spring_layout(G)
            # define a posição dos vertices
            cores = [cor if cor == 1 else 0 for cor in [self.e_bipartido(vertice) for vertice in G.nodes()]]
            # define as cores
            nx.draw(G, pos, with_labels=True, node_color=cores, cmap=plt.get_cmap("coolwarm"), node_size=500)
            # desenha o grafo
            plt.show()
"""
Para verificar se um grafo é bipartido, percorremos todos os vértices do grafo 
e verificamos se cada vértice é bipartido. em termos de cores, se o grafo for bipartido,
não havera vértices adjacentes com a mesma cor.se for n bipartido haverá vértices adjacentescom a mesma cor
"""
# Exemplo de uso
"""
grafo = Grafo()
grafo.adicionar_aresta(1, 2)
grafo.adicionar_aresta(2, 3)
grafo.adicionar_aresta(3, 4)

"""
# Exemplo de um grafo não bipartido
# a forma de criar o grafo é grafo = Grafo()
# a forma de inserir é grafo.adicionar_aresta(vertice1, vertice2)
grafo = Grafo()
grafo.adicionar_aresta(1, 2)
grafo.adicionar_aresta(2, 3)
grafo.adicionar_aresta(3, 4)
grafo.adicionar_aresta(4, 1)
grafo.adicionar_aresta(1, 3)  # (1 -> 2 -> 3 -> 4 -> 1)

if grafo.bipartido():
    print("O grafo é bipartido.")
else:
    print("O grafo não é bipartido.")
grafo.desenhar_grafo()