import os;
import pandas as pd;

# Criando um DataFrame com alguns dados
def criar_dataFrame():
    
    dados_filmes= {"Título": [
        "Ilha do Medo", "Parasita", "Corra!", "A Origem", "La La Land",
        "Mad Max: Estrada da Fúria", "Spotlight", "Pantera Negra", "O Grande Hotel Budapeste",
        "Divertida Mente", "Whiplash", "Gravidade", "O Lobo de Wall Street", "O Jogo da Imitação",
        "Boyhood", "Me Chame Pelo Seu Nome", "O Regresso", "Django Livre", "Ela", "Clube da Luta",
        "Forrest Gump", "A Teoria de Tudo", "O Destino de uma Nação", "O Senhor dos Anéis: O Retorno do Rei",
        "O Fabuloso Destino de Amélie Poulain", "A Rede Social", "A Chegada", "Gladiador",
        "O Pianista", "O Grande Truque"
    ],
    "Ano de lançamento": [
        2010, 2019, 2017, 2010, 2016,
        2015, 2015, 2018, 2014, 2015,
        2014, 2013, 2013, 2014, 2014,
        2017, 2015, 2012, 2013, 1999,
        1994, 2014, 2017, 2003, 2001,
        2010, 2016, 2000, 2002, 2006
    ],
    "Gênero": [
        "Suspense", "Suspense", "Terror", "Ficção Científica", "Musical",
        "Ação", "Drama", "Ação", "Comédia", "Animação",
        "Drama", "Ficção Científica", "Biografia", "Biografia", "Drama",
        "Romance", "Aventura", "Faroeste", "Romance", "Drama",
        "Drama", "Biografia", "Histórico", "Fantasia", "Romance",
        "Biografia", "Ficção Científica", "Épico", "Guerra", "Mistério"
    ],
    "Diretor": [
        "Martin Scorsese", "Bong Joon-ho", "Jordan Peele", "Christopher Nolan", "Damien Chazelle",
        "George Miller", "Tom McCarthy", "Ryan Coogler", "Wes Anderson", "Pete Docter",
        "Damien Chazelle", "Alfonso Cuarón", "Martin Scorsese", "Morten Tyldum", "Richard Linklater",
        "Luca Guadagnino", "Alejandro G. Iñárritu", "Quentin Tarantino", "Spike Jonze", "David Fincher",
        "Robert Zemeckis", "James Marsh", "Joe Wright", "Peter Jackson", "Jean-Pierre Jeunet",
        "David Fincher", "Denis Villeneuve", "Ridley Scott", "Roman Polanski", "Christopher Nolan"
    ],
    "Duração": [
        138, 132, 104, 148, 128,
        120, 129, 134, 99, 95,
        107, 91, 180, 113, 165,
        132, 156, 165, 126, 139,
        142, 123, 125, 201, 122,
        120, 116, 155, 150, 130
    ],
    "Bilheteria (milhões)": [
        294, 258, 255, 836, 447,
        378, 98, 1347, 173, 858,
        49, 723, 392, 233, 44,
        41, 533, 425, 48, 101,
        678, 123, 150, 1120, 174,
        224, 203, 460, 120, 109
    ],
    "Avaliação IMDb": [
        8.2, 8.6, 7.8, 8.8, 8.0,
        8.1, 8.2, 7.3, 8.1, 8.1,
        8.5, 7.7, 8.2, 8.0, 7.9,
        7.8, 8.0, 8.4, 8.0, 8.8,
        8.8, 7.7, 7.4, 9.0, 8.3,
        7.7, 7.9, 8.5, 8.5, 8.5
    ],
    "Avaliação Rotten Tomatoes": [
        68, 99, 98, 87, 91,
        97, 97, 96, 92, 98,
        94, 96, 79, 90, 97,
        94, 78, 87, 95, 79,
        71, 80, 84, 93, 89,
        96, 94, 77, 95, 76
    ],
    "Avaliação do público": [
        4.5, 4.8, 4.5, 4.6, 4.4,
        4.5, 4.3, 4.7, 4.2, 4.8,
        4.6, 4.5, 4.4, 4.3, 4.2,
        4.3, 4.4, 4.5, 4.4, 4.7,
        4.8, 4.3, 4.2, 4.9, 4.6,
        4.4, 4.5, 4.6, 4.7, 4.5
    ],
    "Plataforma de streaming": [
        "Amazon Prime, Apple TV", "Max, Looke", "Prime Video, Globoplay, Netflix", "Netflix, Prime Video",
        "Star+, Globoplay", "HBO Max", "GloboPlay", "Disney+, Star+", "Star+", "Disney+",
        "Amazon Prime Video", "Max", "Paramount+", "Prime Video", "Star+",
        "Prime Video, Netflix", "Star+", "Netflix", "Netflix", "Star+",
        "Star+, Netflix", "Globoplay", "Star+", "Max", "Looke",
        "Netflix", "Paramount+", "Netflix", "Globoplay", "HBO Max"
    ]
    }
    return pd.DataFrame(dados_filmes);



def salvar_dataframe(df, formato: int, caminho_pasta: str):
   
   # Verifica se a pasta existe, se não, cria
    if not os.path.exists(caminho_pasta):
        os.makedirs(caminho_pasta)
    
    # Caminho completo do arquivo CSV
    caminho_arquivo = os.path.join(caminho_pasta, 'filmes.csv');
   
   #Escolhendo formato do Data Frame
    match formato:
        case 1:
            df.to_csv(caminho_arquivo, index=False);
            print("Arquivo salvo com sucesso em:", caminho_arquivo);
        case 2:
            df.to_csv(caminho_arquivo, sep='\t', index=False);
            print("Arquivo salvo com sucesso em:", caminho_arquivo);
        case _:
            print("Escolha entre 1 e 2!");
            return 0
          

# Bloco principal
if __name__ == "__main__":
    df = criar_dataFrame();


print("1- CSV (Comma-Separated Values): Formato de texto onde os dados são separados por vírgulas.")
print("2- TSV (Tab-Separated Values): Igual ao CSV, mas os dados são separados por tabulações.\n")
formato = int(input("Escolha o formato: "));

caminho = r'C:\Users\Black\Downloads\DF Filmes\CSV';

salvar_dataframe(df, formato, caminho);

def ler_dataFrame(caminho_arquivo):
    return pd.read_csv(caminho_arquivo)

def visualizarDf(df):
    print(df)

def visualizarColuna(df, coluna):
    if coluna in df.columns:
        print(df[[coluna]])
    else:
        print("Coluna inválida!")

def ordemNotas(df):
    df['Avaliação IMDb'] = pd.to_numeric(df['Avaliação IMDb'], errors='coerce')
    ordenados = df.sort_values(by='Avaliação IMDb', ascending=False)
    print(ordenados[['Título', 'Avaliação IMDb']])

def contarFilmes(df):
    print(df['Gênero'].value_counts())

def filtrarPorGenero(df, genero):
    filtro = df[df['Gênero'] == genero]
    print(filtro)

def pesquisar_registros_por_coluna(df, coluna, valor):
    match coluna:
        case "Título":
            filtro = df[df["Título"].str.contains(valor, case=False, na=False)]
        case "Ano de lançamento":
            filtro = df[df["Ano de lançamento"] == int(valor)]
        case "Gênero":
            filtro = df[df["Gênero"].str.contains(valor, case=False, na=False)]
        case "Diretor":
            filtro = df[df["Diretor"].str.contains(valor, case=False, na=False)]
        case "Duração":
            filtro = df[df["Duração"] == int(valor)]
        case _:
            print("Coluna inválida! Escolha uma coluna correta.")
            return
    
    print(filtro)

def mediaBilheteira(df):
    df_sorted = df.sort_values(by="Bilheteria (milhões)", ascending=False)
    print(df_sorted[["Título", "Bilheteria (milhões)"]])

def menu():
    caminho_arquivo = r'D:\DF Filmes\CSV\filmes.csv'
    df = ler_dataFrame(caminho_arquivo)
    
    while True:
        print("\n=== MENU DE ANÁLISE DE FILMES ===")
        print("1 - Visualizar todo o DataFrame")
        print("2 - Visualizar todas as colunas")
        print("3 - Visualizar uma coluna específica")
        print("4 - Pesquisar registros por coluna")
        print("5 - Contar filmes por gênero")
        print("6 - Filtrar por gênero")
        print("7 - Ordenar por nota IMDb")
        print("8 - Média de bilheteria ordenada")
        print("0 - Sair")
        
        escolha = input("Escolha uma opção: ")
        
        match escolha:
            case "1":
                visualizarDf(df)
            case "2":
                print(list(df.columns))
            case "3":
                coluna = input("Digite o nome da coluna: ")
                visualizarColuna(df, coluna)
            case "4":
                coluna = input("Digite a coluna: ")
                valor = input("Digite o valor a pesquisar: ")
                pesquisar_registros_por_coluna(df, coluna, valor)
            case "5":
                contarFilmes(df)
            case "6":
                genero = input("Digite o gênero: ")
                filtrarPorGenero(df, genero)
            case "7":
                ordemNotas(df)
            case "8":
                mediaBilheteira(df)
            case "0":
                print("Saindo...")
                break
            case _:
                print("Opção inválida!")

if __name__ == "__main__":
    df = criar_dataFrame()
    salvar_dataframe(df, formato, caminho)
    menu()
