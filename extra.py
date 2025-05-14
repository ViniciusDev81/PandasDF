import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Importar o CSV corretamente
csv_file = r"C:\Users\Black\Downloads\filme csv\filmes.csv"
df = pd.read_csv(csv_file)


# Criando Gráfico de Barras
def criarGraficoBarras():
    plt.figure(figsize=(10,6))
    sns.barplot(x="Bilheteria (milhões)", y="Título", data=df)
    plt.title("Bilheteria dos Filmes")
    plt.xlabel("(Milhões")
    plt.ylabel("Título")
    
    # Salvando o gráfico
    plt.savefig("Barras.png")
    plt.close()  # Fecha a figura para liberar memória

# Criando Gráficos Comparativos
def criarGraficoLinha():
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=df["Ano de lançamento"], y=df["Avaliação IMDb"], marker="o", sort=True)
    plt.xlabel("Ano de Lançamento")
    plt.ylabel("Avaliação IMDb")
    plt.title("Evolução das Avaliações IMDb ao Longo dos Anos")
    plt.grid(True)
    plt.show()

    # Salvando o gráfico
    plt.savefig("Linha.png")
    plt.close()

def criarGraficoDeDispersao():
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=df["Avaliação IMDb"], y=df["Avaliação Rotten Tomatoes"], hue=df["Gênero"], palette="tab10")
    plt.xlabel("Avaliação IMDb")
    plt.ylabel("Avaliação Rotten Tomatoes")
    plt.title("Correlação entre IMDb e Rotten Tomatoes")
    plt.show()

        # Salvando o gráfico
    plt.savefig("Dispersao.png")
    plt.close()  # Fecha a figura para liberar memória

def criarGraficoPizza():
    plt.figure(figsize=(10, 6))
    df["Gênero"].value_counts().plot(kind="pie", autopct="%1.1f%%", startangle=90, colormap="plasma")
    plt.ylabel("")  # Remove label do eixo Y
    plt.title("Distribuição dos Gêneros dos Filmes")
    plt.show()

        # Salvando o gráfico
    plt.savefig("Pizza.png")
    plt.close()  # Fecha a figura para liberar memória

# Chamando as funções para gerar os gráficos
criarGraficoBarras()
criarGraficoLinha()
criarGraficoDeDispersao()
criarGraficoPizza()