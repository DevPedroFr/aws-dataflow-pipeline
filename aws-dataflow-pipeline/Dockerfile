# Imagem base com Python
FROM python:3.10

# Diretório de trabalho dentro do container
WORKDIR /app

# Copia todos os arquivos para dentro do container
COPY . .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Comando padrão ao rodar o container
CMD ["python", "main.py"]
