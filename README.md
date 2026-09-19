````markdown
# 🎵 Convertor Audio

Aplicação simples desenvolvida em **Python** para extrair áudio de vídeos e convertê-lo para **MP3**.

O projeto utiliza **yt-dlp**, **FFmpeg** e **Docker**, permitindo executar a aplicação sem precisar instalar Python, FFmpeg ou as dependências diretamente na máquina.

---

## 🚀 Tecnologias

- Python 3.12
- yt-dlp
- FFmpeg
- Docker
- Docker Compose

---

## 📁 Estrutura do projeto

```text
convertor-audio/
│
├── app/
│   └── main.py
│
├── downloads/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .dockerignore
├── .gitignore
└── README.md
```

---

## ⚙️ Pré-requisitos

Para executar o projeto é necessário ter instalado:

- Docker
- Docker Compose

Verifique se o Docker está instalado:

```bash
docker --version
```

Verifique o Docker Compose:

```bash
docker compose version
```

---

## 📥 Clonando o projeto

Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/convertor-audio.git
```

Entre na pasta:

```bash
cd convertor-audio
```

---

## 🐳 Construindo a imagem

Na primeira execução, construa a imagem Docker:

```bash
docker compose build
```

Durante o build, o Docker irá:

- Baixar a imagem do Python
- Instalar o FFmpeg
- Instalar o yt-dlp
- Copiar o código da aplicação

---

## ▶️ Executando

Execute:

```bash
docker compose run --rm audioforge
```

A aplicação solicitará uma URL:

```text
==============================
       CONVERTOR AUDIO
==============================

Cole a URL do vídeo:
```

Cole a URL desejada e pressione `Enter`.

Exemplo:

```text
https://www.youtube.com/watch?v=XXXXXXXX
```

O funcionamento básico é:

```text
URL
 ↓
yt-dlp
 ↓
Melhor áudio disponível
 ↓
FFmpeg
 ↓
MP3
 ↓
downloads/
```

---

## 📂 Arquivos baixados

Os arquivos convertidos são armazenados dentro da pasta:

```text
downloads/
```

Exemplo:

```text
convertor-audio/
│
└── downloads/
    └── nome-do-audio.mp3
```

A pasta `downloads` é compartilhada entre o container Docker e o computador através de um volume configurado no `docker-compose.yml`.

---

## 🔄 Alterações no código

Caso você altere o código Python, será necessário reconstruir a imagem:

```bash
docker compose build
```

Depois execute novamente:

```bash
docker compose run --rm audioforge
```

Também é possível fazer as duas operações de uma vez:

```bash
docker compose run --build --rm audioforge
```

---

## 🧹 O que significa `--rm`?

O comando:

```bash
docker compose run --rm audioforge
```

cria um container temporário para executar a aplicação.

Quando o programa termina, o container é automaticamente removido.

Isso evita o acúmulo de containers parados no computador.

---

