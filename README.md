# PandasDF
Gerenciador de Filmes 📽️
Este projeto tem como objetivo criar e gerenciar um banco de dados de filmes utilizando arquivos CSV. Ele garante que os arquivos sejam armazenados de forma organizada e acessível, independentemente do usuário.

📁 Estrutura do Projeto
/dados              # Diretório para armazenar arquivos CSV
  ├── filmes.csv   # Arquivo contendo informações sobre os filmes
script.py           # Código principal do projeto
README.md           # Este arquivo de documentação
⚙️ Funcionalidades
Criação automática de um diretório /dados para armazenar os arquivos CSV.

Armazenamento de títulos de filmes e anos de lançamento.

Exportação dos dados para um arquivo CSV.

🚀 Como Usar
Clone este repositório:

git clone <URL_DO_REPOSITORIO>
Instale as dependências (caso necessário):

pip install pandas
Execute o script:

python
import os
import pandas as pd

# Define o caminho do diretório e arquivo
pasta_dados = "/dados"
arquivo_csv = os.path.join(pasta_dados, "filmes.csv")

# Cria a pasta se não existir
os.makedirs(pasta_dados, exist_ok=True)

# Salva o DataFrame no CSV
df_filmes = pd.DataFrame({"Titulo": ["Filme A", "Filme B"], "Ano": [2021, 2022]})
df_filmes.to_csv(arquivo_csv, index=False)

print(f"Arquivo salvo em {arquivo_csv}")
O arquivo filmes.csv será criado no diretório /dados.

🛠️ Tecnologias Utilizadas
Python

Pandas

📜 Licença
Este projeto é de código aberto e pode ser utilizado livremente.

Feito com ❤️ para facilitar a organização de filmes!
