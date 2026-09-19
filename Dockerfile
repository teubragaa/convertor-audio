FROM python:3.12-slim

WORKDIR /app

# Instala o FFmpeg dentro do container
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    rm -rf /var/lib/apt/lists/*

# Copia as dependências
COPY requirements.txt .

# Instala as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia o projeto
COPY app/ ./app/

# Cria pasta onde os áudios serão salvos
RUN mkdir -p /app/downloads

CMD ["python", "app/main.py"]