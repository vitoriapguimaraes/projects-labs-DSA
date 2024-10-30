# Utilizar imagem base Python
FROM python:3.10.11

# Definir o diretório de trabalho
WORKDIR /app

# Copiar arquivos necessários
COPY requirements.txt requirements.txt
COPY 4-analysis_with_flask.py 4-analysis_with_flask.py
COPY 4-dados/ 4-dados/

# Instalar as dependências
RUN pip install -r requirements.txt

# Expor a porta do Flask
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["python", "4-analysis_with_flask.py"]