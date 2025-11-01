from bancoDadosProjeto import *
from datetime import date
session.query(Tweet).delete()
session.query(Aplicativo).delete()
session.query(Sentimento).delete()
session.query(PalavraChave).delete()
try:
    # Inserindo Tweets
    tweets = [
        Tweet("Hoje o dia está incrível!", date(2025, 9, 20), "user1", date(2025, 9, 19)),
        Tweet("Estou muito cansado da rotina.", date(2025, 9, 21), "user2", date(2025, 9, 20)),
        Tweet("Python facilita muito a vida.", date(2025, 9, 22), "user3", date(2025, 9, 20)),
        Tweet("O céu está lindo hoje.", date(2025, 9, 23), "user4", date(2025, 9, 22)),
        Tweet("Não consigo dormir direito.", date(2025, 9, 24), "user5", date(2025, 9, 22)),
        Tweet("Ganhei uma oportunidade no estágio!", date(2025, 9, 24), "user6", date(2025, 9, 23)),
        Tweet("Estou me sentindo sozinho ultimamente.", date(2025, 9, 24), "user7", date(2025, 9, 23)),
        Tweet("Adoro estudar programação!", date(2025, 9, 24), "user8", date(2025, 9, 23)),
    ]
    session.add_all(tweets)
    session.commit()

    # Inserindo Aplicativos
    aplicativos = [
        Aplicativo("Twitter", 1),
        Aplicativo("Twitter", 2),
        Aplicativo("Twitter", 3),
        Aplicativo("Instagram", 4),
        Aplicativo("Facebook", 5),
        Aplicativo("Twitter", 6),
        Aplicativo("Instagram", 7),
        Aplicativo("TikTok", 8),
    ]
    session.add_all(aplicativos)
    session.commit()

    # Inserindo Sentimentos
    sentimentos = [
        Sentimento("Positivo", 95.00,1),
        Sentimento("Negativo", 85.00,2),
        Sentimento("Positivo", 90.00,3),
        Sentimento("Positivo", 88.00,4),
        Sentimento("Negativo", 80.00,5),
        Sentimento("Positivo", 92.00,6),
        Sentimento("Negativo", 89.00,7),
        Sentimento("Positivo", 96.00,8),
    ]
    session.add_all(sentimentos)
    session.commit()

    # Inserindo Palavras-Chave
    palavras = [
        PalavraChave("dia", 1),
        PalavraChave("rotina", 2),
        PalavraChave("python", 3),
        PalavraChave("céu", 4),
        PalavraChave("dormir", 5),
        PalavraChave("estágio", 6),
        PalavraChave("sozinho", 7),
        PalavraChave("programação", 8),
    ]
    session.add_all(palavras)
    session.commit()

except Exception as erro:
    print(f"Infelizmente aconteceu um erro: {erro}")


print("Tentativa de registro de dados.")

print("visualização dos dados:".upper())
print("visualização da tabela Tweet:\n")
tweets=session.query(Tweet).all()
for tweet in tweets:
    print(f"id:{tweet.id}\t nome usuario:{tweet.nomeUsuario}\t criado em{tweet.dataCriacao} coletado em:{tweet.dataColeta} \t texto:{tweet.texto}\n")

print("visualização da tabela Aplicativo")
aplicativos=session.query(Aplicativo).all()
for redeSocial in aplicativos:
    print(f"idAplicativo: {redeSocial.idAplicativo}\tAplicativo{redeSocial.aplicativo}\tAplicativo pertecnete a o idTexto{redeSocial.idTexto}\n")

print("visualização da tabela Sentimentos")
sentimentos=session.query(Sentimento).all()
for sent in sentimentos:
    print(f"idSentimento:{sent.idSentimento}\t Polaridade:{sent.sentimento}\tPrecisão:{sent.acuracia}\tPertecente ao idTexto:{sent.idTexto}\n")

print("visualização da tabela PalavrasChave")
palavras=session.query(PalavraChave).all()
for chave in palavras:
    print(f"idPalavra:{chave.idPalavra}\tPalavra chave:{chave.palavra}\t Pertecente ao idTexto:{chave.idTexto}")
