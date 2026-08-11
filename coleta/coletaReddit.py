seguranca={
    "clientaId":"XXX",
    "clientSecret":"XXX",
    "userAgent":"XXX"
}
#Não esta com as chaves pois ainda não foi liberado a autorização do reedit
import praw
import datetime

from coleta.coletaTweet import contagem

data=datetime.datetime.today()

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

                    
            except Exception as erro:
                print(f"ocorreu esse esso esperando {1.5*60}s")
                contagem(1.5*60)