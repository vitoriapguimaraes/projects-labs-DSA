### Exploratory Data Analysis with Python Applied to Retail ###


### Análise de dados associados a perguntas de negócios ###
### Análise Exploratória de Dados em Linguagem Python Para a Área de Varejo ###

# Fonte: https://community.tableau.com/s/question/0D54T00000CWeX8SAL/sample-superstore-sales-excelxls


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

### Carregando os dados com pandas em Linguagem Python ###

df = pd.read_csv("4-analysis/4-dados/dataset.csv")

print(f"\nShape dos dados é {df.shape}")
print("\nPrimeiras linhas dos dados:")
print(df.head())
print("\nÚltimas linhas dos dados:")
print(df.tail())

caminho = (f'4-analysis//4-graficos')

### Análise exploratória ###

# Colunas do conjunto de dados
print(f"\nAs colunas do conjunto de dados são {df.columns}")

# Verificando o tipo de dado de cada coluna
print("\nCujo tipo de dados são:")
print(df.dtypes)

# Resumo estatístico da coluna com o valor de venda
print("\nResumo estatístico da coluna com o valor de venda:")
print(df['Valor_Venda'].describe())

# Verificando se há registros duplicados
print(f"\nRegistros duplicados: {df[df.duplicated()]}")

# Verificando de há valores ausentes
print(f"\nValores ausentes: \n{df.isnull().sum()}")


### Perguntas de Negócio ###


print("\nPergunta de Negócio 1")
print("Qual Cidade com Maior Valor de Venda de Produtos da Categoria 'Office Supplies'?")

df_p1 = df[df['Categoria'] == 'Office Supplies']

df_p1_total = df_p1.groupby("Cidade")["Valor_Venda"].sum()

cidade_maior_venda = df_p1_total.idxmax()

print(f"\n>>> A Cidade com Maior Valor de Venda de Produtos da Categoria 'Office Supllies' é {cidade_maior_venda} <<<")

print(f"\nPara conferir o resultado, segue a lista do maior para menor: \n{df_p1_total.sort_values(ascending = False)}")


print("\nPergunta de Negócio 2")
print("Qual o Total de Vendas Por Data do Pedido?")
print("Demonstre o resultado através de um gráfico de linha.")

df_p2 = df.groupby("Data_Pedido")["Valor_Venda"].sum()
print(f"\n>>> Total de Vendas por Data do Pedido (primeiras cinco linhas): <<<\n{df_p2.head()}")

plt.figure(figsize= (12,6))
df_p2.plot(x = 'Data_Pedido', y = 'Valor_Venda', color = 'blue')
plt.title('Total de Vendas Por Data do Pedido')
plt.xlabel("Data do Pedido")
plt.ylabel("Total do Valor de Venda (R$)")
plt.savefig(f"{caminho}/Pergunta 2")
# plt.show()
print(f"\nGráfico da Pergunta 2 exportado para {caminho}.")


print("\nPergunta de Negócio 3")
print("Qual o Total de Vendas por Estado?")
print("Demonstre o resultado através de um gráfico de barras.")

df_p3 = df.groupby("Estado")["Valor_Venda"].sum().reset_index()
print(f"\n>>> Total de Vendas por Estado (primeiras cinco linhas): <<<\n{df_p3.head()}")

plt.figure(figsize= (12,12))
sns.barplot(data=df_p3,
            x = 'Estado',
            y = 'Valor_Venda',
            hue= 'Estado',
            palette=sns.color_palette("husl", n_colors=49, as_cmap=False),
            dodge=False,
            legend=False).set(title = "Total de Vendas Por Estado")
plt.xlabel("Estado")
plt.ylabel("Total do Valor de Venda (R$)")
plt.xticks(rotation = 80)
plt.savefig(f"{caminho}/Pergunta 3")
# plt.show()
print(f"\nGráfico da Pergunta 3 exportado para {caminho}.")


print("\nPergunta de Negócio 4")
print("Quais São as 10 Cidades com Maior Total de Vendas?")
print("Demonstre o resultado através de um gráfico de barras.")

df_p4 = df.groupby("Cidade")["Valor_Venda"].sum().reset_index().sort_values(by="Valor_Venda", ascending = False)[0:10]

print(f"\n>>> As 10 Cidades com Maior Total de Vendas: <<<\n{df_p4}")

plt.figure(figsize= (12,8))
sns.barplot(data=df_p4,
            x = 'Cidade',
            y = 'Valor_Venda',
            hue= 'Cidade',
            palette=sns.color_palette("Set1", n_colors=10, as_cmap=False),
            dodge=False,
            legend=False).set(title = "As 10 Cidades com Maior Total de Vendas")
plt.xlabel("Cidade")
plt.ylabel("Total do Valor de Venda (R$)")
plt.xticks(rotation = 45)
plt.savefig(f"{caminho}/Pergunta 4")
# plt.show()
print(f"\nGráfico da Pergunta 4 exportado para {caminho}.")


print("\nPergunta de Negócio 5")
print("Qual Segmento Teve o Maior Total de Vendas?")
print("Demonstre o resultado através de um gráfico de pizza.")

df_p5 = df.groupby("Segmento")["Valor_Venda"].sum().reset_index().sort_values(by= 'Valor_Venda', ascending= False)
df_p5['Valor_Venda_Formatado'] = df_p5['Valor_Venda'].apply(lambda x: f'{x:,.2f}')
df_p5_lista = df_p5["Segmento"].to_list()

print(f"\n>>> O Segmento com Maior Total de Vendas foi {df_p5_lista[0]}. <<<")

print(f"\n>>> Segmentos com Maiores Vendas: <<<\n{df_p5[['Segmento', 'Valor_Venda_Formatado']]}")

def autopct_format(values): 
    def my_format(pct): 
        total = sum(values) 
        val = int(round(pct * total / 100.0))
        return f'{pct:.1f}%\nR$ {val:,.0f}'
    return my_format

plt.figure(figsize= (12,6))
plt.pie(df_p5["Valor_Venda"],
        labels = df_p5['Segmento'],
        autopct=autopct_format(df_p5['Valor_Venda']),
        startangle = 90)
plt.title("Segmentos com Maiores Vendas")
plt.axis('equal')

centre_circle = plt.Circle((0, 0), 0.88, fc = 'white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.savefig(f"{caminho}/Pergunta 5")
# plt.show()
print(f"\nGráfico da Pergunta 5 exportado para {caminho}.")


print("\nPergunta de Negócio 6")
print("Qual o Total de Vendas Por Segmento e Por Ano?")

df['Ano'] = df['ID_Pedido'].str.split('-').str[1].astype(int)
# Conferindo a nova coluna criada
# print(df.head())
# print(df.dtypes)

df_p6 = df.groupby(["Ano", "Segmento"])["Valor_Venda"].sum()
print(f"\n>>> Total de Vendas Por Segmento e Por Ano: <<<\n{df_p6}")

# Outra resolução
# Extraímos o ano criando nova variável
# df['Ano'] = df['Data_Pedido'].dt.year
# Total de vendas por segmento e por ano
# df_p6 = df.groupby(['Ano', 'Segmento'])['Valor_Venda'].sum()


print("\nPergunta de Negócio 7")
print("""Os gestores da empresa estão considerando conceder diferentes faixas de descontos e
gostariam de fazer uma simulação com base na regra abaixo:
    Se o Valor_Venda for maior que 1000 recebe 15% de desconto.
    Se o Valor_Venda for menor que 1000 recebe 10% de desconto.
Quantas Vendas Receberiam 15% de Desconto?""")

df['Desconto'] = np.where(df['Valor_Venda'] > 1000, 0.15, 0.10)
df_p7 = df['Desconto'].value_counts().tolist()
print(f"\n>>> No Total {df_p7[1]} Vendas Receberiam Desconto de 15%. <<<")


print("\nPergunta de Negócio 8")
print("""Considere Que a Empresa Decida Conceder o Desconto de 15% do Item Anterior.
Qual seria a Média do Valor de Venda Antes e Depois do Desconto?""")

df['Valor_desconto_15'] = np.where(df['Desconto'] == 0.15, df['Valor_Venda']*(1-0.15), df['Valor_Venda'])

print(f"\n>>> A Média do Valor de TODAS as Vendas Antes do Desconto é R$ {round(df['Valor_Venda'].mean(), 2)}. <<<")
print(f">>> A Média do Valor de TODAS as Vendas Depois do Desconto é R$ {round(df['Valor_desconto_15'].mean(), 2)}. <<<")

df_p8 = df[df['Desconto'] == 0.15]

print(f"\n>>> A Média do Valor das Vendas, maiores que R$ 1000, Antes do Desconto é R$ {round(df_p8['Valor_Venda'].mean(), 2)}. <<<")
print(f">>> A Média do Valor das Vendas, maiores que R$ 1000, Depois do Desconto é R$ {round(df_p8['Valor_desconto_15'].mean(), 2)}. <<<")


print("\nPergunta de Negócio 9")
print("""Qual o Média de Vendas Por Segmento, Por Ano e Por Mês?
Demonstre o resultado através de gráfico de linha.""")

df['Data_Pedido'] = pd.to_datetime(df['Data_Pedido'], dayfirst=True)
df['Mes'] = df['Data_Pedido'].dt.month
# alternativa: df['Mes'] = df['Data_Pedido'].str.split('/').str[1].astype(int)

df['Ano_Mes'] = df['Ano'].astype(str) + '/' + df['Mes'].astype(str).str.zfill(2)

# Conferindo novas colunas criadas
# print(df.head())
# print(df.dtypes)

df_p9 = df.groupby(['Segmento', 'Ano_Mes'])['Valor_Venda'].mean().reset_index()

print(f"\n>>> Média de Vendas Por Segmento, Por Ano e Por Mês: <<<\n{df_p9}")

# figura 1
plt.figure(figsize= (12,8))
sns.set()
sns.lineplot(data=df_p9, x='Ano_Mes', y='Valor_Venda', hue='Segmento', marker= 'o')
plt.title("Média de Vendas Por Segmento, Por Ano e Por Mês")
plt.xlabel("Ano/Mês")
plt.ylabel("Média de Vendas (R$)")
plt.xticks(rotation=45)
plt.grid(True)
plt.savefig(f"{caminho}/Pergunta 9-1")
# plt.show()
print(f"\nO primeiro gráfico da Pergunta 9 exportado para {caminho}.")

# figura 2
df_p9_2 = df.groupby(['Segmento', 'Ano', 'Mes'])['Valor_Venda'].mean().reset_index()
fig1 = sns.relplot(kind = 'line',
                data = df_p9_2, 
                y = 'Valor_Venda', 
                x = 'Mes',
                hue = 'Segmento', 
                col = 'Ano',
                col_wrap = 4)
fig1.set_axis_labels("Mês", "Média de Vendas (R$)") \
    .set_titles("Média de Vendas de {col_name} Por Segmento e Por Mês")
plt.savefig(f"{caminho}/Pergunta 9-2")
# plt.show()
print(f"O segundo gráfico da Pergunta 9 exportado para {caminho}.")


print("\nPergunta de Negócio 10")
print("""Qual o Total de Vendas Por Categoria e SubCategoria, Considerando Somente as Top 12 SubCategorias?
Demonstre tudo através de um único gráfico.""")

# As top 12 subcategorias
df_p10_sub = df.groupby('SubCategoria')['Valor_Venda'].sum().sort_values(ascending= False).reset_index()
df_p10_sub_list = df_p10_sub['SubCategoria'][0:12].to_list()
df_p10_top12 = df[df['SubCategoria'].isin(df_p10_sub_list)]

# Dados para o gráfico
df_p10 = df_p10_top12.groupby(['Categoria', 'SubCategoria'])['Valor_Venda'].sum().reset_index()
df_p10_cat = df_p10.groupby('Categoria')['Valor_Venda'].sum().reset_index()

# Listas de cores
cores_categorias = ['#5d00de',
                    '#0ee84f',
                    '#e80e27']
cores_subcategorias = ['#aa8cd4',
                    '#aa8cd5',
                    '#aa8cd6',
                    '#aa8cd7',
                    '#26c957',
                    '#26c958',
                    '#26c959',
                    '#26c960',
                    '#e65e65',
                    '#e65e66',
                    '#e65e67',
                    '#e65e68']

# Criando o gráfico de pizza
fig, ax = plt.subplots(figsize=(16, 16))

p1 = ax.pie(df_p10_cat['Valor_Venda'],
            radius= 1,
            labels= df_p10_cat['Categoria'],
            wedgeprops= dict(edgecolor = 'white'),
            colors= cores_categorias,
            textprops={'fontsize': 16})

p2 = ax.pie(df_p10['Valor_Venda'],
            radius= 0.9,
            labels= df_p10['SubCategoria'],
            autopct= autopct_format(df_p10['Valor_Venda']),
            colors= cores_subcategorias,
            labeldistance= 0.7,
            wedgeprops= dict(edgecolor = 'white'),
            pctdistance= 0.53,
            rotatelabels= True,
            textprops={'fontsize': 12})

centre_circle = plt.Circle((0, 0), 0.6, fc = 'white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.annotate(text = 'Total de Vendas: ' + 'R$ ' + str(int(sum(df_p10['Valor_Venda']))), xy = (-0.2, 0))
plt.title('Total de Vendas Por Categoria e Top 12 SubCategorias', fontsize = 16)

plt.savefig(f"{caminho}/Pergunta 10")
# plt.show()
print(f"\nGráfico da Pergunta 10 exportado para {caminho}.")
print("-"*50)