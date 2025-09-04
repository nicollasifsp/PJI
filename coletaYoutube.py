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
            item = response["items"] 
            video_id = item["id"]["videoId"]
            titulo = item["snippet"]["title"]
            canal = item["snippet"]["channelTitle"]
            time.sleep(2)
    except:
        print("ocorreu um erro. Esperando 15 minutos para voltar a rodar.")
        contagem(15*60)

    return {"id": video_id, "titulo": titulo, "canal": canal}

# Função para pegar até 10 comentários de um vídeo
def pegar_comentarios(video_id, max_comentarios):
    
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
            session.fash()

            dadosAplicativo=Aplicativo("YOUTUBE",dadosTweet.id)
            session.add(dadosAplicativo)
            session.commit()
        
#Tweet=(self,texto,dataColeta,nomeUsuario,dataCriacao)
#Aplicativo=(self,aplicativo,IdTexto)
    

# Tema que você quer pesquisar
tema = "depressão"

# Busca 1 vídeo
video = buscar_video(tema,maxResul=100)
print(f"Vídeo encontrado: {video['titulo']} (Canal: {video['canal']})")
print(f"Link: https://www.youtube.com/watch?v={video['id']}\n")

# Coleta 10 comentários desse vídeo
comentarios = pegar_comentarios(video["id"], max_comentarios=10)

print(f"Foram coletados {len(comentarios)} comentários:\n")
for c in comentarios:
    print("-", c.replace("\n", " "))
