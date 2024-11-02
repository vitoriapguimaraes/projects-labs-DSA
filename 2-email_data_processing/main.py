# Exemplo de extração/tratamento de dados para envio de relatório em e-mail

import pandas as pd

# importar a base de dados
tabela_vendas = pd.read_excel('exemplo_vendas.xlsx')

# visualiar a base de dados
# pd.set_option('display.max_columns', None)

# faturamento por loja
faturamento_loja = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()

# quantidade de produtos vendidos por loja
quantidade_prod_loja = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()

# ticket médio por produto em cada loja
ticket_medio = (faturamento_loja['Valor Final'] / quantidade_prod_loja['Quantidade']).to_frame()
ticket_medio = ticket_medio.rename(columns={0: 'Ticket Médio'})

# enviar um email com o relatório
import win32com.client as win32

outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'vipistori@gmail.com'
mail.Subject = 'Relatório de Vendas por Loja'
mail.HTMLBody = f'''
<p>Prezados,</p>

<p>Segue o Relatório de Vendas por cada Loja.</p>

<p>Faturamento:</p>
{faturamento_loja.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})}

<p>Quantidade Vendida:</p>
{quantidade_prod_loja.to_html()}

<p>Ticket Médio dos Produtos em cada Loja:</p>
{ticket_medio.to_html(formatters={'Ticket Médio': 'R${:,.2f}'.format})}

<p>Qualquer dúvida, estou a disposição.</p>

<p>Att,</p>
<p>Vitória.</p>
'''
mail.Send()

print("Email enviado")