seguranca={"IDCliente":"237758416533-pd9u0fv8t7ijqv31n1rqrqh69f87q8kl.apps.googleusercontent.com",
"chaveApi":"AIzaSyDAY_OO3EZ9acazqXqxPzJmxyt_36JgXx0"
}

from googleapiclient.discovery import build
from testeColetaTweet import contagem
import time
from bancoDadosProjeto import session,Aplicativo,Tweet
import datetime
data=datetime.datetime.today()


# Constrói cliente YouTube
youtube = build("youtube", "v3", developerKey=seguranca["chaveApi"])


def buscar_video(tema,maxResul):
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
            item = response["items"][0]
            video_id = item["id"]["videoId"]
            titulo = item["snippet"]["title"]
            canal = item["snippet"]["channelTitle"]
            time.sleep(2)
    except Exception as e:
        print(f"ocorreu um erro.{e}")

    return {"id": video_id, "titulo": titulo, "canal": canal}


def pegar_comentarios(video_id, max_comentarios):
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        textFormat="plainText",
        maxResults=max_comentarios
    )
    response = request.execute()

    for item in response.get("items", []):
        comentario = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        autor = item["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"]
        dataCriacao=item["snippet"]["topLevelComment"]["snippet"]["publishedAt"]
        existe = session.query(Tweet).filter_by(
                        texto=comentario,
                        nomeUsuario=autor,
                        dataCriacao=dataCriacao
                    ).first()
        comentarios.append(comentario)
        if not existe:
            dadosTweet = Tweet(comentario, data, autor, dataCriacao)
            session.add(dadosTweet)
            session.commit()

            dadosAplicativo=Aplicativo("YOUTUBE",dadosTweet.id)
            session.add(dadosAplicativo)
            session.commit()
        
#Tweet=(self,texto,dataColeta,nomeUsuario,dataCriacao)
#Aplicativo=(self,aplicativo,IdTexto)

# Tema que você quer pesquisar
tema = "depressão"
# Busca 1 vídeo
maxResul=100
maxComentario=100
video = buscar_video(tema,maxResul=10)
# Coleta 10 comentários desse vídeo
comentarios = pegar_comentarios(video["id"], maxComentarios=10)

