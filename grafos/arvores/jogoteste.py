import tkinter as tk
from PIL import Image, ImageTk

class CasaNobre:
    def __init__(self, nome, brasao, lema):
        self.nome = nome
        self.brasao = brasao
        self.lema = lema
        self.esquerda = None
        self.direita = None

# Sua lógica para inserir casas nobres na árvore aqui
def inserir_casa(root, nome, brasao, lema):
    if root is None:
        return CasaNobre(nome, brasao, lema)
    
    if nome < root.nome:
        root.esquerda = inserir_casa(root.esquerda, nome, brasao, lema)
    elif nome > root.nome:
        root.direita = inserir_casa(root.direita, nome, brasao, lema)
    
    return root
def buscar_casa(root, nome):
    if root is None or root.nome == nome:
        return root
    
    if nome < root.nome:
        return buscar_casa(root.esquerda, nome)
    
    return buscar_casa(root.direita, nome)

def mostrar_informacoes():
    casa = buscar_casa(raiz, nome_casa.get())
    if casa:
        info_label.config(text=f"Nome: {casa.nome}\nBrasão: {casa.brasao}\nLema: {casa.lema}")
        imagem = Image.open(f"brasoes/{casa.brasao}.png")
        imagem = imagem.resize((100, 100), Image.ANTIALIAS)
        foto = ImageTk.PhotoImage(imagem)
        imagem_label.config(image=foto)
        imagem_label.image = foto
    else:
        info_label.config(text="Casa não encontrada.")

# Cria a janela principal
janela = tk.Tk()
janela.title("Game of Thrones Houses")

# Cria elementos na janela
nome_label = tk.Label(janela, text="Nome da Casa:")
nome_label.pack()

nome_casa = tk.Entry(janela)
nome_casa.pack()

mostrar_info_botao = tk.Button(janela, text="Mostrar Informações", command=mostrar_informacoes)
mostrar_info_botao.pack()

info_label = tk.Label(janela, text="")
info_label.pack()

imagem_label = tk.Label(janela)
imagem_label.pack()

# Exemplo de uso:
raiz = None
raiz = inserir_casa(raiz, "Stark", "Lobo Gigante", "O inverno está chegando")
raiz = inserir_casa(raiz, "Lannister", "Leão Dourado", "Ou você vence, ou você morre")
raiz = inserir_casa(raiz, "Targaryen", "Dragão Vermelho", "Fogo e Sangue")

# Inicie a interface gráfica
janela.mainloop()
