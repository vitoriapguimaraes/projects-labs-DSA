faturamento = 1000
custo = 700

lucro = faturamento - custo

# print(f"Faturamento: {faturamento}, Custo: {custo}, Lucro: {lucro}")
# print("Faturamento:" + str(faturamento) + ", Custo:" + str(custo) + ", Lucro: " + str(lucro))

email = "EMAIL_falso@gmail.com"

print(email.lower())
print(email.find("@")) # -1, se não encontrar o elemento. Se encontrar: a posição

posicao = email.find("@")
servidor = email[posicao+1:]
print(servidor)

# tamanho de um texto
tamanho = len(email)
print(tamanho)

# trocar um pedaço do texto
email_trocado = email.replace("gmail.com", "hotmail.com")
print(email_trocado)

nome = "joao lira"
print(nome.capitalize()) # Joao lira
print(nome.title()) # Joao Lira

# especiais - formatação numerico
margem = lucro / faturamento
print(f"Faturamento: R${faturamento:,.2f}\n Custo: {custo}\n Lucro: {lucro}")
print(f"Margem: {margem:.1%}")

# exercícios
nome = "Joao Paulo Lira"
email = "joaofalso@gmail.com"

# descubra o servidor do email 
posicao = email.find("@")
servidor = email[posicao:]
print(servidor)

# pegar o 1º nome do usuário
posicao = nome.find(" ")
primeiro_nome = nome[:posicao]
print(primeiro_nome)

# construa uma mensagem: Usuario primeiro_nome cadastrado com sucesso com o email tal
mensagem = f"Usuario {primeiro_nome} cadastrado com sucesso com o email: {email}"
print(mensagem)

# construa uma mensagem: Enviamos um link de confirmação para o email j***@gmail.com
primeira_letra = email[0]
print(primeira_letra)
mensagem2 = f"Enviamos um link de confirmação para o email {primeira_letra}***{servidor}"
print(mensagem2)