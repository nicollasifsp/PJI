# Guia de Comandos — Projeto PJI / Análise de Sentimentos

Este arquivo é uma referência para desenvolvimento do projeto usando **Windows + PowerShell + VS Code + Python + MySQL + Git/GitHub**.

Inclui:

- ambiente virtual Python;
- instalação de bibliotecas;
- problemas de segurança do PowerShell;
- Git e GitHub;
- padrão de commits;
- MySQL;
- `.env`;
- execução com `python -m`;
- Repository;
- erros comuns e diagnóstico;
- comandos úteis.

---

# 1. ESTRUTURA RECOMENDADA

```text
PJI/
│
├── database/
│   ├── __init__.py
│   └── conexao.py
│
├── repository/
│   ├── __init__.py
│   ├── textosRepository.py
│   ├── avaliacaoRepository.py
│   ├── processamentoRepository.py
│   └── resultadosRepository.py
│
├── coleta/
│   ├── __init__.py
│   ├── coletaReddit.py
│   ├── coletaX.py
│   ├── coletaBluesky.py
│   └── coletaMastodon.py
│
├── processamento/
│   ├── __init__.py
│   └── ...
│
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

Responsabilidades:

```text
coleta
  ↓
obtém dados das APIs

repository
  ↓
salva/busca dados no banco

database
  ↓
faz a conexão com o MySQL

processamento
  ↓
limpa/prepara os textos

classificação
  ↓
classifica os sentimentos
```

Regra importante:

> O coletor não deve ter SQL espalhado pelo código. Ele chama o Repository.

Fluxo:

```text
coletaReddit.py
      ↓
textosRepository.py
      ↓
database/conexao.py
      ↓
MySQL
```

---

# 2. ABRINDO O PROJETO

```powershell
cd "C:\Users\nicol\OneDrive\Área de Trabalho\PJI"
```

Ver onde está:

```powershell
pwd
```

Listar arquivos:

```powershell
dir
```

ou:

```powershell
ls
```

---

# 3. AMBIENTE VIRTUAL PYTHON

Criar:

```powershell
python -m venv .venv
```

Ativar no PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Se aparecer:

```text
(.venv) PS C:\...
```

o ambiente está ativo.

O `.venv` deve estar no `.gitignore`:

```text
.venv/
```

---

# 4. ERRO DE SEGURANÇA AO ATIVAR O VENV

Se aparecer:

```text
running scripts is disabled on this system
```

ou:

```text
ExecutionPolicy
```

use:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Depois:

```powershell
.\.venv\Scripts\Activate.ps1
```

`-Scope Process` altera a política somente para o PowerShell atual. Ao fechar o terminal, ela volta ao estado anterior.

---

# 5. CONFERIR QUAL PYTHON ESTÁ SENDO USADO

```powershell
python --version
```

```powershell
where.exe python
```

Ou:

```powershell
python -c "import sys; print(sys.executable)"
```

O caminho deve apontar para algo parecido com:

```text
PJI\.venv\Scripts\python.exe
```

---

# 6. PIP

Atualizar:

```powershell
python -m pip install --upgrade pip
```

É preferível usar:

```powershell
python -m pip
```

em vez de simplesmente:

```powershell
pip
```

porque isso deixa claro qual Python está usando o `pip`.

---

# 7. INSTALAR BIBLIOTECAS

MySQL:

```powershell
python -m pip install mysql-connector-python
```

dotenv:

```powershell
python -m pip install python-dotenv
```

Várias:

```powershell
python -m pip install mysql-connector-python python-dotenv
```

---

# 8. ERRO DE PERMISSÃO AO INSTALAR BIBLIOTECA

Se aparecer:

```text
Permission denied
```

ou:

```text
Access is denied
```

primeiro confira:

```powershell
python -c "import sys; print(sys.executable)"
```

Se estiver usando `.venv`, tente:

```powershell
python -m pip install nome-da-biblioteca
```

Evite instalar globalmente com privilégios de administrador sem necessidade.

---

# 9. `ModuleNotFoundError`

Exemplo:

```text
ModuleNotFoundError: No module named 'mysql'
```

ou:

```text
ModuleNotFoundError: No module named 'dotenv'
```

Verifique:

```powershell
python -m pip show mysql-connector-python
```

```powershell
python -m pip show python-dotenv
```

Se não aparecer:

```powershell
python -m pip install mysql-connector-python python-dotenv
```

---

# 10. REQUIREMENTS.TXT

Gerar:

```powershell
python -m pip freeze > requirements.txt
```

Instalar todas as dependências:

```powershell
python -m pip install -r requirements.txt
```

Isso facilita levar o projeto para outro computador.

---

# 11. GIT — CONFIGURAÇÃO INICIAL

Verificar instalação:

```powershell
git --version
```

Configurar nome:

```powershell
git config --global user.name "Seu Nome"
```

Configurar e-mail:

```powershell
git config --global user.email "seu@email.com"
```

Ver configurações:

```powershell
git config --global --list
```

---

# 12. CRIAR REPOSITÓRIO GIT

Na raiz do PJI:

```powershell
git init
```

Ver situação:

```powershell
git status
```

---

# 13. `.GITIGNORE`

Exemplo:

```text
.venv/
__pycache__/
*.pyc

.env

.vscode/
```

Nunca coloque sua senha do MySQL no Git.

---

# 14. `.ENV.EXAMPLE`

Exemplo:

```text
HOST=localhost
PORT=3306
USER=root
PASSWORD=
DATABASE=analiseSentimentos
```

O `.env.example` pode ser compartilhado.

O `.env` com a senha real não deve ser enviado ao Git.

---

# 15. PRIMEIRO COMMIT

```powershell
git status
```

Adicionar:

```powershell
git add .
```

Conferir:

```powershell
git status
```

Commit:

```powershell
git commit -m "feat: estrutura inicial do projeto"
```

---

# 16. PADRÃO DE COMMITS

Formato:

```text
tipo: mensagem
```

## `feat`

Nova funcionalidade:

```text
feat: adiciona coleta de dados do Reddit
```

```text
feat: adiciona conexão com MySQL
```

## `fix`

Correção de bug:

```text
fix: corrige conexão com banco de dados
```

## `refactor`

Reorganização sem mudar a funcionalidade principal:

```text
refactor: reorganiza estrutura dos repositories
```

## `docs`

Documentação:

```text
docs: adiciona documentação do projeto
```

## `test`

Testes:

```text
test: adiciona teste do repository de textos
```

## `chore`

Configuração/manutenção:

```text
chore: adiciona requirements.txt
```

## `style`

Formatação:

```text
style: ajusta formatação dos repositories
```

## `perf`

Desempenho:

```text
perf: otimiza inserção dos textos coletados
```

Para o PJI, provavelmente você usará principalmente:

```text
feat:
fix:
refactor:
test:
docs:
chore:
```

---

# 17. VER COMMITS

Completo:

```powershell
git log
```

Resumido:

```powershell
git log --oneline
```

---

# 18. VER ALTERAÇÕES

```powershell
git status
```

```powershell
git diff
```

---

# 19. DESCARTAR ALTERAÇÕES

Um arquivo:

```powershell
git restore arquivo.py
```

Todas as alterações não commitadas:

```powershell
git restore .
```

**Cuidado:** isso pode apagar alterações que ainda não foram commitadas.

---

# 20. GITHUB

Adicionar repositório remoto:

```powershell
git remote add origin https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
```

Ver:

```powershell
git remote -v
```

Definir `main`:

```powershell
git branch -M main
```

Primeiro push:

```powershell
git push -u origin main
```

Depois:

```powershell
git push
```

---

# 21. CLONAR

```powershell
git clone URL_DO_REPOSITORIO
```

Depois:

```powershell
cd REPOSITORIO
```

Criar ambiente:

```powershell
python -m venv .venv
```

Ativar:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instalar:

```powershell
python -m pip install -r requirements.txt
```

Criar `.env` a partir do `.env.example`.

---

# 22. PULL

Trazer alterações do GitHub:

```powershell
git pull
```

Fluxo recomendado:

```text
git pull
↓
desenvolver
↓
git status
↓
git add .
↓
git commit -m "tipo: mensagem"
↓
git push
```

---

# 23. BRANCHES

Criar e entrar:

```powershell
git switch -c coleta-reddit
```

Listar:

```powershell
git branch
```

Voltar:

```powershell
git switch main
```

---

# 24. MYSQL — VERIFICAR SERVIÇO

Iniciar:

```powershell
net start MySQL80
```

Se aparecer:

```text
O serviço solicitado já foi iniciado.
```

o serviço está rodando.

Parar:

```powershell
net stop MySQL80
```

---

# 25. MYSQL — CLIENTE NÃO ENCONTRADO

Se:

```powershell
mysql -u root -p
```

retornar:

```text
mysql : O termo 'mysql' não é reconhecido...
```

o executável provavelmente não está no PATH.

Execute diretamente:

```powershell
& "C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe" -u root -p
```

---

# 26. MYSQL — TESTAR LOGIN

```powershell
& "C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe" -u root -p
```

Se aparecer:

```text
Welcome to the MySQL monitor.
```

o login funcionou.

---

# 27. MYSQL — COMANDOS BÁSICOS

Mostrar bancos:

```sql
SHOW DATABASES;
```

Selecionar banco:

```sql
USE analiseSentimentos;
```

Mostrar tabelas:

```sql
SHOW TABLES;
```

Ver estrutura:

```sql
DESCRIBE textosColetados;
```

Ver dados:

```sql
SELECT * FROM textosColetados;
```

Sair:

```sql
EXIT;
```

---

# 28. MYSQL — BANCO FORA DO AR

Se o Python apresentar algo parecido com:

```text
Can't connect to MySQL server
```

verifique:

```powershell
net start MySQL80
```

Depois teste o login:

```powershell
& "C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe" -u root -p
```

Se o login funcionar, o servidor está funcionando e o problema provavelmente está na configuração do Python.

---

# 29. MYSQL — `UNKNOWN DATABASE`

Erro:

```text
1049 (42000): Unknown database '...'
```

Significa que o banco informado não existe com aquele nome.

Verifique:

```sql
SHOW DATABASES;
```

Se necessário:

```sql
CREATE DATABASE analiseSentimentos;
```

No `.env`:

```text
DATABASE=analiseSentimentos
```

Tenha cuidado com:

```text
analiseSentimento
analiseSentimentos
```

São nomes diferentes.

---

# 30. MYSQL — `ACCESS DENIED`

Erro:

```text
Access denied for user 'root'@'localhost'
```

Pode indicar:

- usuário incorreto;
- senha incorreta;
- permissões;
- configuração de autenticação.

Teste manualmente:

```powershell
& "C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe" -u root -p
```

Se falhar também, provavelmente o problema não está no Python.

---

# 31. MYSQL — PORTA

A porta padrão:

```text
3306
```

`.env`:

```text
PORT=3306
```

Python:

```python
port=int(os.getenv("PORT"))
```

No MySQL:

```sql
SHOW VARIABLES LIKE 'port';
```

---

# 32. `NoneType` E `cursor`

Erro:

```text
AttributeError: 'NoneType' object has no attribute 'cursor'
```

Se você tem:

```python
conexao = getConexao()
cursor = conexao.cursor()
```

isso normalmente significa que:

```python
getConexao()
```

retornou:

```python
None
```

A função precisa fazer:

```python
return conexao
```

Se estiver tratando erros:

```python
except Exception as erro:
    print(f"Erro ao conectar: {erro}")
    return None
```

No Repository, pode verificar:

```python
conexao = getConexao()

if conexao is None:
    return False

cursor = conexao.cursor()
```

---

# 33. NÃO ESCONDER ERROS

Evite:

```python
except:
    print("deu erro.")
```

Prefira:

```python
except Exception as erro:
    print(f"Erro: {erro}")
```

Assim você vê a mensagem real.

---

# 34. CONEXÃO MYSQL RECOMENDADA

```python
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()


def getConexao():
    try:
        conexao = mysql.connector.connect(
            host=os.getenv("HOST"),
            port=int(os.getenv("PORT")),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            database=os.getenv("DATABASE"),
            raise_on_warnings=True,
            use_pure=True
        )

        if conexao.is_connected():
            print("Conectado com o banco com sucesso")

        return conexao

    except Exception as erro:
        print(f"Erro ao conectar com o banco: {erro}")
        return None
```

---

# 35. `.ENV` RETORNANDO `NONE`

Se:

```python
print(os.getenv("HOST"))
```

retornar:

```text
None
```

verifique:

1. O arquivo se chama exatamente `.env`.
2. Não está como `.env.txt`.
3. O `.env` está na localização esperada.
4. `load_dotenv()` foi executado.
5. Os nomes das variáveis coincidem.

`.env`:

```text
HOST=localhost
PORT=3306
USER=root
PASSWORD=sua_senha
DATABASE=analiseSentimentos
```

Python:

```python
os.getenv("HOST")
os.getenv("PORT")
os.getenv("USER")
os.getenv("PASSWORD")
os.getenv("DATABASE")
```

---

# 36. SEGURANÇA DO `.ENV`

Nunca coloque:

```python
password="minhaSenha"
```

no código compartilhado.

Prefira:

```python
password=os.getenv("PASSWORD")
```

Nunca envie `.env` ao Git.

`.gitignore`:

```text
.env
```

Se o `.env` já foi adicionado ao Git:

```powershell
git rm --cached .env
```

Depois:

```powershell
git commit -m "chore: remove arquivo env do controle de versão"
```

Se uma senha real já foi enviada para um repositório remoto, trate essa senha como comprometida e altere-a.

---

# 37. `PYTHON -M`

Para sua estrutura:

```text
PJI/
├── database/
├── repository/
└── coleta/
```

e:

```text
database/__init__.py
repository/__init__.py
coleta/__init__.py
```

Execute a partir da raiz:

```powershell
python -m coleta.testeColeta
```

ou:

```powershell
python -m coleta.coletaReddit
```

Em vez de:

```powershell
python coleta/coletaReddit.py
```

`-m` faz o Python tratar o arquivo como módulo do projeto, facilitando os imports entre `coleta`, `repository` e `database`.

---

# 38. `MODULE NOT FOUND`

Erro:

```text
ModuleNotFoundError: No module named 'database'
```

ou:

```text
ModuleNotFoundError: No module named 'repository'
```

Verifique:

```text
PJI/
├── database/
│   └── __init__.py
├── repository/
│   └── __init__.py
└── coleta/
    └── __init__.py
```

Esteja na raiz:

```text
PS ...\PJI>
```

Execute:

```powershell
python -m coleta.testeColeta
```

Evite corrigir isso adicionando caminhos absolutos ou `sys.path` sem necessidade.

---

# 39. REPOSITORY

O Repository é responsável pelo acesso aos dados.

Exemplo:

```python
def salvarTexto(...):
    ...
```

O coletor chama:

```python
salvarTexto(...)
```

e não precisa conhecer SQL.

Arquitetura:

```text
coleta
  ↓
repository
  ↓
database/conexao
  ↓
MySQL
```

---

# 40. CURSOR

Criar:

```python
conexao = getConexao()
cursor = conexao.cursor()
```

Executar SQL:

```python
cursor.execute(sql)
```

Vários registros:

```python
cursor.executemany(sql, dados)
```

Finalizar:

```python
cursor.close()
conexao.close()
```

---

# 41. COMMIT

Depois de:

```text
INSERT
UPDATE
DELETE
```

use:

```python
conexao.commit()
```

---

# 42. ROLLBACK

Em caso de erro:

```python
conexao.rollback()
```

Exemplo:

```python
try:
    cursor.execute(sql)
    conexao.commit()

except Exception as erro:
    conexao.rollback()
    print(erro)
```

---

# 43. INSERT COM PARÂMETROS

Prefira:

```python
sql = """
INSERT INTO carros (modelo, dataFabri, preco)
VALUES (%s, %s, %s)
"""

dados = ("Corolla", "2024-05-20", 125000.00)

cursor.execute(sql, dados)
```

Evite montar SQL concatenando strings com dados externos.

---

# 44. `EXECUTEMANY`

Para vários registros:

```python
carros = [
    ("Corolla", "2024-05-20", 125000.00),
    ("Civic", "2023-08-15", 140000.00),
    ("Onix", "2025-01-10", 85000.00)
]

cursor.executemany(sql, carros)
conexao.commit()
```

Isso será útil para os dados retornados pelas APIs.

---

# 45. TESTAR DADOS INSERIDOS

Python:

```python
cursor.execute("SELECT * FROM carros")

dados = cursor.fetchall()

for dado in dados:
    print(dado)
```

MySQL:

```sql
USE analiseSentimentos;

SELECT * FROM carros;
```

---

# 46. ERRO DE SINTAXE SQL

Erro:

```text
You have an error in your SQL syntax
```

Confira:

- vírgulas;
- parênteses;
- nomes das colunas;
- `;`;
- tipos de dados;
- palavras reservadas.

Se possível, teste o SQL diretamente no MySQL para separar problemas de SQL de problemas do Python.

---

# 47. TABELA NÃO EXISTE

Erro:

```text
Table 'analiseSentimentos.carros' doesn't exist
```

Verifique:

```sql
USE analiseSentimentos;
SHOW TABLES;
```

Estrutura:

```sql
DESCRIBE carros;
```

---

# 48. DATAS

`DATE`:

```text
2024-05-20
```

`DATETIME`:

```text
2026-08-09 22:30:00
```

No projeto:

```sql
dataPost DATETIME
dataColeta DATETIME
```

são adequados quando você precisa guardar data e horário.

---

# 49. `DECIMAL(10,2)`

```sql
DECIMAL(10,2)
```

significa:

```text
10 = total de dígitos
2  = casas decimais
```

Exemplo:

```text
125000.00
```

---

# 50. COMANDOS GIT — RESUMO

```powershell
git init
git status
git add .
git commit -m "tipo: mensagem"
git log --oneline
git clone URL
git pull
git push
git branch
git switch main
git switch -c nova-branch
git diff
git restore arquivo
git remote -v
```

---

# 51. COMANDOS PYTHON — RESUMO

```powershell
python --version
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install pacote
python -m pip freeze
python -m pip freeze > requirements.txt
python -m pip install -r requirements.txt
python -m coleta.coletaReddit
```

---

# 52. COMANDOS MYSQL — RESUMO

PowerShell:

```powershell
net start MySQL80
net stop MySQL80
```

Cliente:

```powershell
& "C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe" -u root -p
```

MySQL:

```sql
SHOW DATABASES;
USE analiseSentimentos;
SHOW TABLES;
DESCRIBE nomeTabela;
SELECT * FROM nomeTabela;
SHOW VARIABLES LIKE 'port';
EXIT;
```

---

# 53. CHECKLIST — PROBLEMA NO PYTHON

```text
[ ] O .venv está ativo?
[ ] python --version funciona?
[ ] sys.executable aponta para .venv?
[ ] A biblioteca está instalada?
[ ] Estou na raiz PJI?
[ ] Preciso usar python -m?
[ ] Os __init__.py existem?
[ ] O import está correto?
```

---

# 54. CHECKLIST — PROBLEMA NO MYSQL

```text
[ ] O serviço MySQL80 está iniciado?
[ ] Consigo entrar usando mysql.exe?
[ ] HOST está correto?
[ ] PORT está correto?
[ ] USER está correto?
[ ] PASSWORD está correta?
[ ] DATABASE existe?
[ ] A tabela existe?
[ ] Os nomes das colunas estão corretos?
```

---

# 55. CHECKLIST — `.ENV`

```text
[ ] O arquivo se chama exatamente .env?
[ ] Não está como .env.txt?
[ ] O .env está no local correto?
[ ] load_dotenv() foi executado?
[ ] Os nomes das variáveis coincidem?
[ ] O .env está no .gitignore?
[ ] Estou usando o ambiente Python correto?
```

---

# 56. CHECKLIST — ANTES DO COMMIT

```powershell
git status
```

Confirme que não aparecem:

```text
.env
.venv/
__pycache__/
```

Depois:

```powershell
git add .
git status
```

Confira o que será enviado.

Depois:

```powershell
git commit -m "tipo: mensagem"
git push
```

---

# 57. FLUXO COMPLETO DE DESENVOLVIMENTO

Começar:

```powershell
cd "C:\Users\nicol\OneDrive\Área de Trabalho\PJI"
```

Ativar:

```powershell
.\.venv\Scripts\Activate.ps1
```

Atualizar:

```powershell
git pull
```

Testar:

```powershell
python -m coleta.testeColeta
```

Conferir:

```powershell
git status
git diff
```

Adicionar:

```powershell
git add .
```

Commit:

```powershell
git commit -m "feat: adiciona coleta do Reddit"
```

Enviar:

```powershell
git push
```

---

# 58. CONFIGURAR O PROJETO EM OUTRO COMPUTADOR

```powershell
git clone URL_DO_REPOSITORIO
cd PJI
```

Criar:

```powershell
python -m venv .venv
```

Se necessário:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Ativar:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instalar:

```powershell
python -m pip install -r requirements.txt
```

Criar `.env` usando `.env.example`.

Configurar MySQL.

Testar:

```powershell
python -m coleta.testeColeta
```

---

# 59. REGRA PARA INVESTIGAR ERROS

Quando aparecer um erro:

```text
1. Leia a última linha.
2. Veja o tipo do erro.
3. Veja o arquivo e a linha.
4. Identifique qual componente falhou.
5. Teste essa parte isoladamente.
6. Só então altere o código.
```

Exemplos:

```text
ModuleNotFoundError
↓
problema de importação ou biblioteca

Unknown database
↓
banco inexistente/nome errado

Access denied
↓
usuário/senha/permissões

NoneType has no attribute cursor
↓
getConexao() provavelmente retornou None

Can't connect to MySQL server
↓
serviço/host/porta

No module named ...
↓
biblioteca ou ambiente virtual
```

---

# 60. COMANDOS DE EMERGÊNCIA

Ver Python:

```powershell
python -c "import sys; print(sys.executable)"
```

Ver pip:

```powershell
python -m pip --version
```

Ver pacote:

```powershell
python -m pip show NOME_DO_PACOTE
```

Ver Git:

```powershell
git --version
```

Ver estado:

```powershell
git status
```

Ver branch:

```powershell
git branch
```

Ver cliente MySQL:

```powershell
& "C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe" -u root -p
```

Ver serviço:

```powershell
net start MySQL80
```

---

# 61. ARQUITETURA DO PJI

```text
                    APIs
                     │
          ┌──────────┼──────────┐
          ↓          ↓          ↓
       Reddit         X      Mastodon
          │          │          │
          └──────────┼──────────┘
                     ↓
                  Coleta
                     ↓
                Repository
                     ↓
              database/conexao
                     ↓
                   MySQL
                     ↓
              textosColetados
                     ↓
               Processamento
                     ↓
             dadosProcessados
                     ↓
               Classificação
                     ↓
                 resultados
```

Responsabilidades:

```text
Coleta:
"Eu pego os dados."

Repository:
"Eu salvo e busco os dados."

Database:
"Eu conecto no banco."

Processamento:
"Eu preparo os textos."

Classificação:
"Eu classifico os sentimentos."
```

A separação facilita testes, manutenção e a explicação da arquitetura na apresentação da FEMIC.
