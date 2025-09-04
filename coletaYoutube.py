seguranca={"IDCliente":"237758416533-pd9u0fv8t7ijqv31n1rqrqh69f87q8kl.apps.googleusercontent.com",
"chaveApi":"AIzaSyDAY_OO3EZ9acazqXqxPzJmxyt_36JgXx0"
}

from googleapiclient.discovery import build




# Constrói cliente YouTube
youtube = build("youtube", "v3", developerKey=seguranca["chaveApi"])

# Função para buscar 1 vídeo
def buscar_video(tema):
    request = youtube.search().list(
        part="snippet",
        q=tema,
        type="video",
        maxResults=1  # só 1 vídeo
    )
    response = request.execute()
    item = response["items"][0]  # pega o primeiro vídeo
    video_id = item["id"]["videoId"]
    titulo = item["snippet"]["title"]
    canal = item["snippet"]["channelTitle"]
    return {"id": video_id, "titulo": titulo, "canal": canal}

# Função para pegar até 10 comentários de um vídeo
def pegar_comentarios(video_id, max_comentarios=10):
    comentarios = []
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        textFormat="plainText",
        maxResults=max_comentarios
    )
    response = request.execute()

    for item in response.get("items", []):
        comentario = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        comentarios.append(comentario)

    return comentarios

# Tema que você quer pesquisar
tema = "depressão"

# Busca 1 vídeo
video = buscar_video(tema)
print(f"Vídeo encontrado: {video['titulo']} (Canal: {video['canal']})")
print(f"Link: https://www.youtube.com/watch?v={video['id']}\n")

# Coleta 10 comentários desse vídeo
comentarios = pegar_comentarios(video["id"], max_comentarios=10)

print(f"Foram coletados {len(comentarios)} comentários:\n")
for c in comentarios:
    print("-", c.replace("\n", " "))
