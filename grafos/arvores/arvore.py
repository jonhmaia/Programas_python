import matplotlib.pyplot as plt

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self, raiz):
        self.raiz = No(raiz)

    def inserir(self, valor):
        self._inserir_recursivamente(self.raiz, valor)

    def _inserir_recursivamente(self, no, valor):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else:
                self._inserir_recursivamente(no.esquerda, valor)
        else:
            if no.direita is None:
                no.direita = No(valor)
            else:
                self._inserir_recursivamente(no.direita, valor)

    def buscar(self, valor):
        return self._buscar_recursivamente(self.raiz, valor)

    def _buscar_recursivamente(self, no, valor):
        if no is None:
            return False
        if no.valor == valor:
            return True
        if valor < no.valor:
            return self._buscar_recursivamente(no.esquerda, valor)
        return self._buscar_recursivamente(no.direita, valor)

    def desenhar_arvore(self):
        fig, ax = plt.subplots()
        self._desenhar_recursivamente(ax, self.raiz, 0, 0, 1000)
        plt.show()

    def _desenhar_recursivamente(self, ax, no, x, y, dx):
        if no is not None:
            ax.text(x, y, str(no.valor), fontsize=12, ha='center', va='center')
            if no.esquerda:
                ax.plot([x, x - dx], [y - 50, y - 100], 'k-')
                self._desenhar_recursivamente(ax, no.esquerda, x - dx, y - 100, dx // 2)
            if no.direita:
                ax.plot([x, x + dx], [y - 50, y - 100], 'k-')
                self._desenhar_recursivamente(ax, no.direita, x + dx, y - 100, dx // 2)

# Exemplo de uso
arvore = ArvoreBinaria(10)
arvore.inserir(5)
arvore.inserir(15)
arvore.inserir(3)
arvore.inserir(7)
arvore.inserir(12)
arvore.inserir(18)

print(arvore.buscar(7))  # Saída: True
print(arvore.buscar(8))  # Saída: False

arvore.desenhar_arvore()
