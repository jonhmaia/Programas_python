arvore_genealogica_stark = {
    'Ned Stark': {
        'cônjuge': 'Catelyn Stark',
        'filhos': {
            'Robb Stark': {
                'cônjuge': 'Desconhecido',
                'filhos': {}
            },
            'Sansa Stark': {
                'cônjuge': 'Desconhecido',
                'filhos': {}
            },
            'Arya Stark': {
                'cônjuge': 'Desconhecido',
                'filhos': {}
            },
            'Bran Stark': {
                'cônjuge': 'Desconhecido',
                'filhos': {}
            },
            'Rickon Stark': {
                'cônjuge': 'Desconhecido',
                'filhos': {}
            }
        }
    }
}

# Função para pesquisar pais de um membro
def encontrar_pais(pessoa, arvore):
    for pai, dados in arvore.items():
        if 'filhos' in dados:
            if pessoa in dados['filhos']:
                return pai, dados['cônjuge']
    return None, None

# Função para pesquisar irmãos de uma pessoa
def encontrar_irmaos(pessoa, arvore):
    irmaos = []
    pais, _ = encontrar_pais(pessoa, arvore)
    if pais:
        for filho, dados in arvore[pais]['filhos'].items():
            if filho != pessoa:
                irmaos.append(filho)
    return irmaos

# Função para pesquisar mãe de uma pessoa
def encontrar_mae(pessoa, arvore):
    _, mae = encontrar_pais(pessoa, arvore)
    return mae

# Exemplo de uso
while True:
    pessoa = input("Digite o nome da pessoa da Casa Stark que você deseja informações (ou digite 'sair' para encerrar): ")
    
    if pessoa.lower() == 'sair':
        break
    
    if pessoa in arvore_genealogica_stark:
        print(f"Nome: {pessoa}")
        pais, mae = encontrar_pais(pessoa, arvore_genealogica_stark)
        irmaos = encontrar_irmaos(pessoa, arvore_genealogica_stark)
        print(f"Pais: {pais} e {mae}")
        print(f"Irmãos: {', '.join(irmaos)}")
    else:
        print("Pessoa não encontrada na árvore genealógica da Casa Stark.")

