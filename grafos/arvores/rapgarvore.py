import tkinter as tk
from tkinter import ttk
class Item:
    def __init__(self, nome, descricao, atributos):
        self.nome = nome
        self.descricao = descricao
        self.atributos = atributos
        self.filhos = []

    def adicionar_item(self, item):
        self.filhos.append(item)

class ArvoreDeItens:
    def __init__(self, item_inicial):
        self.raiz = item_inicial

# Função para exibir a árvore de itens em uma janela Tkinter
def exibir_arvore(item, nivel, tree_view):
    tree_view.insert("", "end", item.nome, text=item.nome)
    for filho in item.filhos:
        exibir_arvore(filho, nivel + 1, tree_view)

# Exemplo de uso
item_inicial = Item("Espada de Ferro", "Uma espada simples de ferro", {"Ataque": 10, "Defesa": 5})
arvore = ArvoreDeItens(item_inicial)

# Adicionar itens à árvore
item1 = Item("Espada Mágica", "Uma espada mágica com poderes especiais", {"Ataque": 20, "Defesa": 10})
item2 = Item("Armadura de Platina", "Uma armadura de platina resistente", {"Ataque": 5, "Defesa": 25})
item_inicial.adicionar_item(item1)
item_inicial.adicionar_item(item2)

# Criar uma janela Tkinter
root = tk.Tk()
root.title("Árvore de Itens de RPG")

# Criar uma estrutura de árvore visual com Tkinter Treeview
tree_view = tk.ttk.Treeview(root)

tree_view.heading("#0", text="Itens")
tree_view.pack()

# Exibir a árvore de itens na interface gráfica
exibir_arvore(item_inicial, 0, tree_view)

root.mainloop()
