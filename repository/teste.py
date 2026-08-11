from database.conexao import getConexao





def salvarTeste(carros):
    conexao = getConexao()
    cursor = conexao.cursor()
    inserirCarros = """
    INSERT INTO carros (modelo, dataFabri, preco)
    VALUES (%s, %s, %s)
    """
    try:
        cursor.executemany(inserirCarros, carros)
        conexao.commit()
        return "Dados inseridos com sucesso!"
    
    except:
        return False
    
    finally:
        cursor.close()
        conexao.close()
    