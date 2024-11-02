# Avaliar o motivo do cancelamento do cartão a partir da base de dados dos clientes

import pandas as pd
import plotly.express as px
import datetime
import os
import PyPDF2

# passo 1 = importar a base de dados

tabela = pd.read_csv('data-bank.csv', encoding="latin1")

# passo 2 = visualizar e tratar essa base de dados

    # retirando colunas sem interesse para análise do "motivo para cancelamento do cartão"
tabela = tabela.drop("CLIENTNUM", axis=1)
tabela = tabela.drop("Sexo", axis=1)

    # avaliando a qualidade dos dados (se há informação vazia)
tabela = tabela.dropna()
print("Informação da tabela")
print(tabela.info())
print("-"*100)

    # visualizando a tabela final
pd.set_option('display.max_columns', None)
print("Toda tabela final")
print(tabela)
print("-"*100)
   
    # avaliando estatísticas gerais dos dados
print("Descrição da tabela")
print(tabela.describe().round(1))
print("-"*100)

    # visualizando o nome das colunas
nome_colunas = list(tabela.columns.values)
print("Nome das colunas restantes")
print(nome_colunas)
print("-"*100)

# passo 3 - construir uma análise para identificar o motivo de cancelamento

    # avaliar a relação de clientes x cancelados
    
print("Relação de clientes x cancelados")

qtde_categoria = tabela["Categoria"].value_counts()
print(qtde_categoria)

qtde_categoria_perc = tabela["Categoria"].value_counts(normalize=True)
qtde_categoria_perc_dec = qtde_categoria_perc.round(decimals=2)
print(qtde_categoria_perc_dec)

print("-"*100)

    # identificar qual o motivo ou os principais motivos dos clientes estarem cancelando o cartão de crédito
    # método: comparar clientes x cancelados, em cada uma das colunas da base de dados -> 
    # a partir de histogramas:

data_atual = datetime.datetime.today().strftime("%Y-%m-%d_%H%M%S")

caminho = (f'histogram/{data_atual}')
if not os.path.exists(caminho):
    os.makedirs(caminho)
    print(f'Pasta {caminho} criada')
else:
    print(f'A pasta {caminho} já existe')
print("-"*100)
    
for coluna in tabela:
    grafico = px.histogram(tabela, x=coluna, color="Categoria",color_discrete_sequence=px.colors.qualitative.D3)
    grafico.write_image(f"HISTOGRAM/{data_atual}/{coluna}.pdf")
    # grafico.show()

print(f"Histogramas geradas. Procure por eles na pasta {caminho}")

        # reunindo os histogramas em apenas um pdf:
        
lista_histogramas = os.listdir(f"HISTOGRAM/{data_atual}/")
merger = PyPDF2.PdfMerger()
for histograma in lista_histogramas:
    merger.append(f"HISTOGRAM/{data_atual}/{histograma}") 
merger.write(f"HISTOGRAM/{data_atual}-Histogram.pdf")

print(f"PDF combinado criado com sucesso: {data_atual}-Histogramas.pdf")
print("-"*100)