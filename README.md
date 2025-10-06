# 📚 CRUD com PostgreSQL + Python

Este projeto é um exemplo prático de um **CRUD** (Create, Read, Update, Delete) utilizando:

- 🗄️ **Banco de dados:** PostgreSQL  
- 🔌 **Conexão:** psycopg2  
- 🌐 **Interface web:** Streamlit  



### ⚙️ Como Executar

# 1. Clonar o repositório
```bash
git clone https://github.com/DEVdamas97/Aula-PostGresql.git
```

##

# 2. Criar ambiente virtual(opcional, mas recomendado)

``` bash
# Criar ambiente virtual
python -m venv .venv

# Ativar no Windows
.venv\Scripts\activate

# Ativar no macOS/Linux
source .venv/bin/activate
```

##

# 3. Instalar dependências

```bash
pip install -r requirements.txt
```

##

# 4. Configurar variáveis de ambiente

### Crie um arquivo .env na raiz do projeto com o seguinte conteúdo:

```bash
DB_NAME=nome_banco
DB_USER=postgres
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432
```

##

# 5. Rodar a aplicação 

```bash
python -m streamlit run app.py
```

# 🚀 Funcionalidades

   - Conexão com o banco de dados: PostgreSQL via psycopg2 🔗

   - Criar alunos: inserir novos registros 📝

   - Listar alunos: visualizar registros existentes 📋

   - Atualizar alunos: editar informações ✏️

   - Deletar alunos: remover registros ❌

   - Interface: simples e intuitiva com Streamlit 🎨
   
   ##

# 👨‍🏫 Autor

Projeto: desenvolvido em aula para treinar integração entre Python e PostgreSQL 🎓

Professor: Gabriel Brito de Sousa 🧑‍💻