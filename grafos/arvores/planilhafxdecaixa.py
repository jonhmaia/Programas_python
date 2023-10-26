import pandas as pd

# Defina os valores iniciais e as entradas/saídas para cada semana
saldo_inicial = [1000, 2500, 3100, 3300]
entradas = [2000, 1800, 2200, 2500]
saidas = [1500, 1200, 2000, 1700]

# Crie um dicionário com os dados
data = {
    'Saldo Inicial ($)': saldo_inicial,
    'Entradas ($)': entradas,
    'Saídas ($)': saidas
}

# Crie um DataFrame do Pandas com os dados
df = pd.DataFrame(data)

# Calcule o saldo final para cada semana
df['Saldo Final ($)'] = df['Saldo Inicial ($)'] + df['Entradas ($)'] - df['Saídas ($)']

# Adicione uma coluna para representar as semanas
semanas = ['Semana 1', 'Semana 2', 'Semana 3', 'Semana 4']
df.insert(0, 'Semanas', semanas)

# Exiba o DataFrame
print(df)
# Especifique o nome do arquivo Excel
nome_arquivo_excel = "fluxo_de_caixa.xlsx"

# Salve o DataFrame no arquivo Excel
df.to_excel(nome_arquivo_excel, index=False)

print(f"Planilha salva como '{nome_arquivo_excel}'")