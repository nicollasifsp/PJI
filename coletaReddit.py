seguranca={
    "clientaId":"XXX",
    "clientSecret":"XXX",
    "userAgent":"XXX"
}
#Não esta com as chaves pois ainda não foi liberado a autorização do reedit
import praw
import datetime
from bancoDadosProjeto import Session, Postagem, Aplicativo 
from coletaTweet import contagem
#Tweet=(self,texto,dataColeta,nomeUsuario,dataCriacao)
#Aplicativo=(self,aplicativo,IdTexto)
data=datetime.datetime.today()
session=Session()
def coletaReddit(tema, maxResult):
    if isinstance(tema, str):
        tema = [tema]
    for palavra in tema:
        try:
            reddit = praw.Reddit(
                client_id=seguranca["clientaId"],
                client_secret=seguranca["clientSecret"],
                user_agent=seguranca["userAgent"])
            resultados = reddit.subreddit("all").search(palavra, limit=maxResult)
        except Exception as erro:
            print(f"infelizmente ocorreu um erro {erro}")
            

        
        for post in resultados:
            try:
                texto=post.self.text.strip()
                autor=str(post.author) if post.author else "Autor desconhecido"
                dataCriação = datetime.datetime.fromtimestamp(post.created_utc)

                existe = session.query(Postagem).filter_by(
                            texto=texto,
                            nomeUsuario=autor,
                            dataCriacao=dataCriação
                        ).first()
                if not existe:
                    dadosReddit=Postagem(texto,data,autor, dataCriação)
                    Session.add(dadosReddit)
                    Session.commit()

                    dadosAplicativo=Aplicativo("Reddit",dadosReddit.id)
                    Session.add(dadosAplicativo)
                    Session.commit()
                else:
                    print("esse registros ja foram armazenados indo para outro dados")
                    
            except Exception as erro:
                print(f"ocorreu esse esso esperando {1.5*60}s")
                contagem(1.5*60)