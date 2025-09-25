from sqlalchemy import create_engine,Column, String,Integer,DATE,ForeignKey, Float
from sqlalchemy.orm import sessionmaker, declarative_base
bd=create_engine("sqlite:///bancoDados.db")
Session=sessionmaker(bind=bd)
session=Session()
Base=declarative_base()


class Tweet(Base):
    __tablename__="tweets"
    id=Column("id",Integer,primary_key=True,autoincrement=True)
    texto=Column("texto",String)
    dataColeta=Column("dataColeta",DATE)
    nomeUsuario=Column("nomeUsuario",String)
    dataCriacao=Column("dataCriacao",DATE)

    def __init__(self,texto,dataColeta,nomeUsuario,dataCriacao):
        self.texto=texto
        self.dataColeta=dataColeta
        self.nomeUsuario=nomeUsuario
        self.dataCriacao=dataCriacao

class Aplicativo(Base):
    __tablename__="aplicativos"
    idAplicativo=Column("idAplicativo",Integer,primary_key=True,autoincrement=True)
    aplicativo=Column("aplicativo",String)
    idTexto=Column("idTexto",ForeignKey("tweets.id"))
    def __init__(self,aplicativo,IdTexto):
        self.aplicativo=aplicativo
        self.idTexto=IdTexto

class Sentimento(Base):
    __tablename__="sentimentos"
    idSentimento=Column("idSentimento",Integer,primary_key=True,autoincrement=True)
    sentimento=Column("sentimento",String)
    acuracia=Column("acuracia",Float)
    def __init__(self,sentimento,acuracia):
        self.sentimento=sentimento
        self.acuracia=acuracia


class PalavraChave(Base):
    __tablename__="palavrasChave"
    idPalavra=Column("idPalavra",Integer, primary_key=True,autoincrement=True)
    palavra=Column("palavra", String)
    idTexto=Column("idTexto",ForeignKey("tweets.id"))
Base.metadata.create_all(bind=bd)