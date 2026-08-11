seguranca={ "bearerToken":"AAAAAAAAAAAAAAAAAAAAADMQ3QEAAAAAfXq1Zp5%2F5SyTJDyV5ZHy%2BJRA7ic%3DAgSZOZ04qJXUtkY9IGJZHjURYSS1slpFdcmwgNgUUKqccajPyQ",
           "apiKey":"wEpZllmGiYn0UCJMP3cPX3jMc",
           "apiKeySecret":"pLpis5csG6pKpmH31jmuldDJ8eOJvb3GHZf8N3U1MRL4o5PLzw",
           "accessToken":"1445886306257625088-BGhzo8e9czayHiozy5DA85UnXE4ba0",
           "accessTokenSecret":"PAEOVLyN51nLWlTKXYGBlkLh25xJPL9pOxvzBm8HBIl6Q" }

import datetime
import tweepy as tw
import time



def contagem(segundos):
    while segundos > 0:
        mins, secs = divmod(segundos, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(f"Esperando... {timer} minutos", end="\r")
        time.sleep(1)
        segundos -= 1
    print("\nTempo de espera concluído.\n")

cliente=tw.Client(seguranca["bearerToken"])

data=datetime.datetime.today()

def coletaTweet(tema, maxResult):
    tentativa=1
    if isinstance(tema, str):
        tema = [tema]
    for palavra in tema:   
        try:
            response = cliente.search_recent_tweets( 
                query=f'{palavra} lang:pt -is:retweet',
                max_results=maxResult,
                tweet_fields=["created_at", "lang", "text"],
                expansions=["author_id"],
                user_fields=["username"])
            
            if response.data:
                users = {u["id"]: u for u in response.includes["users"]}
                print(f"response.data: {response.data}\n")
                print(f"users: {users}\n")
                for tweet in response.data:
                    user = users[tweet.author_id]
                   
            else:
                if tentativa == 1:
                    print(f"Nenhum tweet encontrado para '{palavra}', esperando 15 minutos...")
                    tentativa -= 1
                    contagem(15*60)
                    coletaTweet(palavra, 100)
                else:
                    tentativa = 1
                    exit()

        except tw.TooManyRequests:
            print("Limite atingido, esperando 15 minutos...\n")
            contagem(15*60)
            coletaTweet(palavra, maxResult)

# a varial tema vai guardar as palavras chaves ainda a declarar
tema = [""]
# teste
# coletaTweet("muniz é o melhor professor",10)
coletaTweet(["python"], 10)        
