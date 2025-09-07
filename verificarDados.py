from bancoDadosProjeto import Tweet, session,Aplicativo
tweets=session.query(Tweet).all()
for tweet in tweets:
    print(f"id:{tweet.id}\t nome usuario:{tweet.nomeUsuario}\t criado em{tweet.dataCriacao} coletado em:{tweet.dataColeta} \t texto:{tweet.texto}\n")

aplicativos=session.query(Aplicativo).all()
for aplicativo in aplicativos:
    print(f"idAplicatvo{aplicativo.idAplicativo}\taplicativo:{aplicativo.aplicativo}\tidTexto{aplicativo.idTexto}\n")
