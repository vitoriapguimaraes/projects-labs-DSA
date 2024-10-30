### Exploratory Data Analysis with Python Applied to Retail ###

from flask import Flask, jsonify, request, render_template_string
import pandas as pd
import numpy as np
import seaborn as sns
import os
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import io
import base64


app = Flask(__name__)

### Carregando os dados com pandas em Linguagem Python ###
df = pd.read_csv("4-analysis/4-dados/dataset.csv")

# Função auxiliar para verificar se o dataset está carregado
def check_data_loaded():
    if df.empty:
        return {"error": "Dataset could not be loaded or is empty"}, 500
    return None

# Formatação gráfica
font_path = "Roboto/Roboto-Regular.ttf"
fontprop = fm.FontProperties(fname=font_path)
fg_fontsize_title = 16
fg_fontsize_text = 12
fg_fontsize_labelx = 10

### ==> HOME <==

@app.route('/')
def home():
    textoinicial = """
    <h1>Flask App Running.</h1>
    <p>Acesse as pergunta de negócio de forma individual a partir de <code>/questaoNUMERO</code></p>
    <ul>
        <li>1: Qual Cidade com Maior Valor de Venda de Produtos da Categoria 'Office Supplies'?</li>
        <li>2: Qual o Total de Vendas Por Data do Pedido? Demonstre o resultado através de um gráfico de barras.</li>
        <li>3: Qual o Total de Vendas por Estado? Demonstre o resultado através de um gráfico de barras.</li>
        <li>4: Quais São as 10 Cidades com Maior Total de Vendas? Demonstre o resultado através de um gráfico de barras.</li>
        <li>5: Qual Segmento Teve o Maior Total de Vendas? Demonstre o resultado através de um gráfico de pizza.</li>
        <li>6: Qual o Total de Vendas Por Segmento e Por Ano?</li>
        <li>7: Os gestores da empresa estão considerando conceder diferentes faixas de descontos e gostariam de fazer uma simulação com base na regra abaixo:
            <ul>
                <li>Se o Valor_Venda for maior que 1000 recebe 15% de desconto.</li>
                <li>Se o Valor_Venda for menor que 1000 recebe 10% de desconto.</li>
            </ul>
            Quantas Vendas Receberiam 15% de Desconto?
        </li>
        <li>8: Considere Que a Empresa Decida Conceder o Desconto de 15% do Item Anterior.
            Qual seria a Média do Valor de Venda Antes e Depois do Desconto?
        </li>
        <li>9: Qual o Média de Vendas Por Segmento, Por Ano e Por Mês? Demonstre o resultado através de gráfico de linha.</li>
        <li>10:Qual o Total de Vendas Por Categomente das Top 12 SubCategorias? Demonstre tudo através de um único gráfico.</li>
    </ul>
    """
    return render_template_string(textoinicial)


### ==> QUESTÃO 1 <==
@app.route("/questao1", methods=["GET"])
def question1():
    data_check = check_data_loaded()
    if data_check:
        return data_check

    df_p1 = df[df['Categoria'] == 'Office Supplies']
    df_p1_total = df_p1.groupby("Cidade")["Valor_Venda"].sum()
    cidade_maior_venda = df_p1_total.idxmax()
    df_p1_sorted = df_p1_total.sort_values(ascending=False).to_dict()

    texto_1 = """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>Pergunta de Negócio 1</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    </head>
    <body>
        <h2>Pergunta de Negócio 1</h2>
        <p><strong>Qual Cidade com Maior Valor de Venda de Produtos da Categoria 'Office Supplies'?</strong></p>
        <p><strong>Cidade com Maior Valor de Venda:</strong> {{ cidade_maior_venda }}</p>
        
        <h3>Para conferir o resultado, segue a lista do maior para o menor valor de venda:</h3>
        <table>
            <thead>
                <tr>
                    <th>Cidade</th>
                    <th>Total de Vendas (R$)</th>
                </tr>
            </thead>
            <tbody>
                {% for cidade, valor in df_p1_sorted.items() %}
                <tr>
                    <td>{{ cidade }}</td>
                    <td>{{ valor }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </body>
    </html>
    """

    return render_template_string(texto_1, cidade_maior_venda=cidade_maior_venda, df_p1_sorted=df_p1_sorted)



### ==> QUESTÃO 2 <==

@app.route("/questao2", methods=["GET"])
def question2():

    # Agrupando e somando o valor das vendas por data
    df_p2 = df.groupby("Data_Pedido")["Valor_Venda"].sum()
    df_p2_head = df_p2.head().to_dict()

    # Gerando o gráfico e convertendo para base64
    fig, ax = plt.subplots(figsize=(10, 6))
    df_p2.plot(ax=ax, color='blue')
    ax.set_title('Total de Vendas Por Data do Pedido', fontproperties=fontprop, fontsize = fg_fontsize_title)
    ax.set_xlabel("Data do Pedido", fontproperties=fontprop, fontsize = fg_fontsize_text)
    ax.set_ylabel("Total do Valor de Venda (R$)", fontproperties=fontprop, fontsize = fg_fontsize_text)
    for label in ax.get_xticklabels():
        label.set_fontproperties(fontprop)
        label.set_fontsize(fg_fontsize_labelx)

    # Convertendo o gráfico para uma imagem em base64
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()

    # Template HTML para exibir o gráfico e os dados
    texto_2 = """
    <h2>Pergunta de Negócio 2</h2>
    <p><strong>Qual o Total de Vendas Por Data do Pedido?</strong></p>
    <p>O gráfico abaixo mostra o total de vendas por data do pedido.</p>
    <img src="data:image/png;base64,{{ graph_url }}" alt="Gráfico de Total de Vendas por Data do Pedido" style="width:80%; margin-bottom:20px;">
    
    <h3>Dados das Primeiras Cinco Linhas:</h3>
    <table border="1">
        <thead>
            <tr>
                <th>Data do Pedido</th>
                <th>Total de Vendas (R$)</th>
            </tr>
        </thead>
        <tbody>
            {% for data, valor in df_p2_head.items() %}
            <tr>
                <td>{{ 'Data_Pedido' }}</td>
                <td>{{ 'Valor_Venda' }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
    """
    return render_template_string(texto_2, df_p2_head=df_p2_head, graph_url=graph_url)



### ==> QUESTÃO 3 <==

@app.route("/questao3", methods=["GET"])
def question3():

    # Agrupando e somando o valor das vendas por estadi
    df_p3 = df.groupby("Estado")["Valor_Venda"].sum().reset_index()
    df_p3_head = df_p3.head().to_dict(orient="records")

    # Gerando o gráfico e convertendo para base64
    fig, ax = plt.subplots(figsize=(12, 12))
    sns.barplot(data=df_p3,
                x = 'Estado',
                y = 'Valor_Venda',
                hue= 'Estado',
                palette=sns.color_palette("husl", n_colors=len(df_p3)),
                dodge=False,
                ax=ax)
    ax.set_title('Total de Vendas Por Estado', fontproperties=fontprop, fontsize = fg_fontsize_title)
    ax.set_xlabel("Estado", fontproperties=fontprop, fontsize = fg_fontsize_text)
    ax.set_ylabel("Total do Valor de Venda (R$)", fontproperties=fontprop, fontsize = fg_fontsize_text)
    for index, label in enumerate(ax.get_xticklabels()):
        if index % 2 != 0:
            label.set_visible(False)
    for label in ax.get_xticklabels():
        label.set_fontproperties(fontprop)
        label.set_rotation(80)
        label.set_fontsize(fg_fontsize_labelx)

    # Convertendo o gráfico para uma imagem em base64
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()

    # Template HTML para exibir o gráfico e os dados
    texto_3 = """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>Pergunta de Negócio 3</title>
        @font-face {
            font-family: 'Roboto';
            src: url('Roboto/Roboto-Regular.ttf') format('truetype');
        }
        body {
            font-family: 'Roboto', sans-serif;
            }
            h2, p, table {
                text-align: center;
                margin-top: 20px;
            }
            table {
                width: 80%;
                margin: auto;
                border-collapse: collapse;
            }
            th, td {
                padding: 10px;
                border: 1px solid #333;
            }
        </style>
    </head>
    <body>
        <h2>Pergunta de Negócio 3</h2>
        <p><strong>Qual o Total de Vendas por Estado?</strong></p>
        <p>O gráfico abaixo mostra o total de vendas por estado.</p>
        <img src="data:image/png;base64,{{ graph_url }}" alt="Gráfico de Total de Vendas por Estado" style="width:80%; margin-bottom:20px;">
        
        <h3>Dados das Primeiras Cinco Linhas:</h3>
        <table>
            <thead>
                <tr>
                    <th>Estado</th>
                    <th>Total de Vendas (R$)</th>
                </tr>
            </thead>
            <tbody>
                {% for row in df_p3_head %}
                <tr>
                    <td>{{ row['Estado'] }}</td>
                    <td>{{ row['Valor_Venda'] }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </body>
    </html>
    """

    return render_template_string(texto_3, df_p3_head=df_p3_head, graph_url=graph_url)







if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)