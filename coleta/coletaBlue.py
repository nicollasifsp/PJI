from atproto import Client
import os

def getPosts(palavraChave):
    client = Client()
    try:
        client.login(
            "heytorcarvalho19.bsky.social",
            "6fpb-ayyt-k3gn-zntx"
        )

        resultado = client.app.bsky.feed.search_posts(
            params={"q": palavraChave}
        )
        if resultado:

            for post in resultado.posts:
                print("=" * 50)
                print("Texto:", post.record.text)
                print("Autor:", post.author.handle)
                print("Data:", post.record.created_at)

                #gravar no banco.

        else:
            print(f"não encontramos dados com a palavra chave {palavraChave}")
    except Exception as erro:
        print(f"ocorreu esse erro: {erro}")

palavraChave = "educação a distância"
getPosts(palavraChave)