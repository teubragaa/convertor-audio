import yt_dlp


def baixar_audio(url):

    opcoes = {

        # Baixa o melhor áudio disponível
        "format": "bestaudio/best",

        # Nome e local do arquivo
        "outtmpl": "/app/downloads/%(title)s.%(ext)s",

        # Evita baixar playlist inteira
        "noplaylist": True,

        # Converte para MP3 usando FFmpeg
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "320",
            }
        ],
    }

    try:

        print("\nBaixando áudio...\n")

        with yt_dlp.YoutubeDL(opcoes) as ydl:
            ydl.download([url])

        print("\nDownload concluído!")
        print("Arquivo salvo na pasta downloads.\n")

    except Exception as erro:

        print("\nOcorreu um erro:")
        print(erro)


def main():

    print("==============================")
    print("         AUDIOFORGE")
    print("==============================")

    url = input("\nCole a URL do vídeo: ")

    if not url:
        print("URL não informada.")
        return

    baixar_audio(url)


if __name__ == "__main__":
    main()