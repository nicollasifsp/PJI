import mysql.connector, os
from dotenv import load_dotenv
load_dotenv()

def getConexao():

    try:
        conexao=mysql.connector.connect(
            host=os.getenv("HOST"),
            port=int(os.getenv("PORT")),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            database=os.getenv("DATABASE"),
            raise_on_warnings=True,
            use_pure=True
        )

        if conexao.is_connected:
            print("conectado com o banco com sucesso")
        return conexao
    except Exception as erro:
        print(f"foi constatado esse erro: {erro}")
