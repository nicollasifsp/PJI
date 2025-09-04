from sqlalchemy import create_engine,Column, String,Integer,DATE,ForeignKey
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

Base.metadata.create_all(bind=bd)