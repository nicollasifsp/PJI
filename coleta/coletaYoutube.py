seguranca={"IDCliente":"237758416533-pd9u0fv8t7ijqv31n1rqrqh69f87q8kl.apps.googleusercontent.com",
"chaveApi":"AIzaSyDAY_OO3EZ9acazqXqxPzJmxyt_36JgXx0"
}

from googleapiclient.discovery import build
import time
import datetime
data=datetime.date.today()


# Constrói cliente YouTube
youtube = build("youtube", "v3", developerKey=seguranca["chaveApi"])


def buscarVideo(tema,maxResul):
    try:
        if isinstance(tema, str):
            tema = [tema]
        for palavra in tema: 
            request = youtube.search().list(
                part="snippet",
                q=palavra,
                type="video",
                maxResults=maxResul  
            )
        
            response = request.execute()
            for item in response.get("items",[]):
                video_id = item["id"]["videoId"]
                titulo = item["snippet"]["title"]
                canal = item["snippet"]["channelTitle"]
            time.sleep(2)
    except Exception as e:
        print(f"ocorreu um erro.{e}")

    return {"id": video_id, "titulo": titulo, "canal": canal}


def pegarComentarios(video_id, maxComentarios):
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        textFormat="plainText",
        maxResults=maxComentarios
    )
    response = request.execute()
    i=1
    for item in response.get("items", []):
        comentario = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        autor = item["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"]
        dataCriacao=item["snippet"]["topLevelComment"]["snippet"]["publishedAt"]
        dataCriacao = datetime.datetime.fromisoformat(dataCriacao.replace("Z", "+00:00")).date()
        dataColeta=data
        
        print(f"\ndados coletados na {i}º tentativa\n")
        print(f"comentario: {comentario}\n")
        print(f"autor: {autor}\n")
        print(f"dataCriacao: {dataCriacao}\n")
        print(f"dataColeta: {dataColeta}\n")
        i=+1       
#Tweet=(self,texto,dataColeta,nomeUsuario,dataCriacao)
#Aplicativo=(self,aplicativo,IdTexto)

# Tema que você quer pesquisar
tema = ["mano deyvin"]

maxResul=100
maxComentario=100
video = buscarVideo(tema,maxResul=5)
# Coleta 10 comentários desse vídeo
comentarios = pegarComentarios(video["id"], maxComentarios=10)
print("videos salvos com sucesso.")

