from database.conexao import getConexao

conexao=getConexao()
cursor=conexao.cursor()

criarTablea= """
create table if not exists carros(
    id int auto_increment primary key,
    modelo varchar(100) not null,
    dataFabri date not null,
    preco decimal(10,2) not null

)"""


inserirCarros = """
INSERT INTO carros (modelo, dataFabri, preco)
VALUES (%s, %s, %s)
"""

carros = [
    ("Corolla", "2024-05-20", 125000.00),
    ("Civic", "2023-08-15", 140000.00),
    ("Onix", "2025-01-10", 85000.00)
]

cursor.executemany(inserirCarros, carros)

