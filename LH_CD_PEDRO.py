import pandas as pd
import matplotlib.pyplot as plt
import pickle

def carregar_dados(caminho):
    try:
        return pd.read_csv(caminho)
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return None
    
caminho = 'desafio_indicium_imdb.csv'
df = carregar_dados(caminho)

# Análise exploratória dos dados (EDA)
print(df.head())
print(df.tail())

# Saber sobre os dados, os tipos de dados e os nulos
print(df.info())
df[df['Gross'].isna()]
df[df['Certificate'].isna()]
df[df['Meta_score'].isna()]

# Usei uma abordagem em que como faltava muitas informações em 'Gross', 'Meta_score' e 'Certificate', pensei que eles não iria ajudar e dropei essas colunas

df_tratado = df.drop(columns=['Certificate', 'Meta_score', 'Gross'])

# Salvar o DataFrame em um arquivo .pkl
#with open('df_tratado.pkl', 'wb') as arquivo:
#    pickle.dump(df_tratado, arquivo)

# Colunas dropadas
df_tratado.info()

# Faltava trocar o tipo de dados, pois por exemplo a data de lançamento estava em tipo object
# Mas antes nessa coluna tinha um filme que o ano estava errado, estava com letras, então alterei manualmente primeiro
# Alterar data apollo 13
df_tratado.loc[df_tratado['Series_Title'] == 'Apollo 13', 'Released_Year'] = 1995

# Alterando o tipo de dados da coluna
df_tratado['Released_Year'] = pd.to_numeric(df_tratado['Released_Year'])
print(df_tratado[df_tratado['Series_Title'] == 'Apollo 13'])

# Necessário  trocar o tipo de dado do 'Runtime' mas como tinha que tirar a palavra 'min' foi diferente
df_tratado['Runtime'] = df_tratado['Runtime'].str.extract('(\d+)').astype(int)

print(df_tratado['Runtime'].head())

# Descrição dos fatos, podendo ver que os filmes a grande maioria são entre os anos de 1976 e 2020, sobre o rating do imdb também, grande parte dos filmes dessa época tem um imdb bom
print(df_tratado.describe())

# Função para correlacionar
def funcao_correlacionar(df, colunas):
    return print(df[colunas].corr())

# Plotar a distribuição de filmes 
def funcao_plotar(serie, title, legenda_x, legenda_y):
    plt.figure(figsize=(10, 6))
    serie.plot(kind='bar')
    plt.xlabel(legenda_x)
    plt.ylabel(legenda_y)
    plt.title(title)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
# Algumas hipoteses que fiz foi cruzar alguns dados e criar tabelas

# Primeiro deixei em ordem por IMDB, aparentemente ja estava mas para ter certeza fiz mesmo assim
df_decrescente_imdb = df_tratado.sort_values(by='IMDB_Rating', ascending=False)
print(df_decrescente_imdb.head(30))
print(df_decrescente_imdb.tail(30))

# Buscar o ano dos filmes mais bem avaliados
print(df_decrescente_imdb['Released_Year'].head(30))

# Selecionar os 100 melhores filmes
top_100_imdb = df_decrescente_imdb.head(100)
genre_distribution = top_100_imdb['Genre'].value_counts()
funcao_plotar(genre_distribution, 'Distribuição dos Gêneros nos 100 Melhores Filmes por IMDB', 'Gênero','Número de Filmes')

# Guarda a lista dos anos dos filmes no top 100 de melhors imdb
released_year_filter = top_100_imdb['Released_Year'].value_counts()

# Separa usando como parametro o ano 2000
before_2000 = released_year_filter[released_year_filter.index < 2000]
funcao_plotar(before_2000, 'Distribuição dos Gêneros nos 100 Melhores Filmes do IMDb (Antes de 2000)', 'Ano de Lançamento', 'Número de Filmes')

after_2000 = released_year_filter[released_year_filter.index >= 2000]
funcao_plotar(after_2000, 'Distribuição dos Gêneros nos 100 Melhores Filmes do IMDb (Depois de 2000)', 'Ano de Lançamento', 'Número de Filmes')

# Nessa parte de analise de dados também fiz a média de votos dos melhores filmes para os 'piores'
# Votos do top 100
top_100 = df_decrescente_imdb.head(100)
votos_do_top_100 = top_100['No_of_Votes']
print("A média de votos do top 100 : ")
print(votos_do_top_100.mean())

# Votos dos 100 "piores"
top_100_ruim = df_decrescente_imdb.tail(100)
votos_top_100_ruim = top_100_ruim['No_of_Votes']
print("A média de votos do top 100 'piores' : ")
print(votos_top_100_ruim.mean())
# Tem mais votos nos melhores filmes (IMDB)

# Cruzei dados para ver se conseguia algum padrão também, Curiosamente todos filmes com mais votos tem nota mais alta no IMDB
funcao_correlacionar(df_tratado, ['IMDB_Rating', 'No_of_Votes'])

# Cruzei os diretores com o imdb fazendo uma media do IMDB de cada diretor 
medias_imdb = {}

for diretor in df_tratado['Director']:
    filmes_diretor = df_tratado[df_tratado['Director'] == diretor]
    media_imdb = filmes_diretor['IMDB_Rating'].mean()
    medias_imdb[diretor] = media_imdb
    
medias_ordenadas = pd.DataFrame(list(medias_imdb.items()), columns=['Director', 'IMDB_rating'])

print(medias_ordenadas.sort_values(by='IMDB_rating', ascending=False))
#9        Lana Wachowski          8.7 - acaba por ser a melhor em média com um filme a mais que o Steven Spielberg ela fica na frente

# Também olhei o overview dos filmes, tentei procurar palavras chaves para achar algum padrão entre os gêneros e o que está escrito
palavras_chave_romance = ['Love', 'love', 'sweetheart', 'relationship', 'affair', 'passion', 'romantic', 'heart', 'couple', 'dating', 'valentine', 'wedding', 'marriage', 'soulmate', 'sweetheart', '_romance']
top_100.loc[top_100['Overview'].str.contains('|'.join(palavras_chave_romance)), ['Genre', 'Series_Title']]

palavras_chave_acao_ou_drama = ['action', 'adventure', 'battle', 'fight', 'hero', 'war', 'explosion', 'chase', 'mission', 'weapon', 'attack', 'soldier', 'combat', 'conflict', 'danger', 'rescue', 'survival', 'villain', 'battlefield', 'spy']
top_100.loc[top_100['Overview'].str.contains('|'.join(palavras_chave_acao_ou_drama)), ['Genre', 'Series_Title']]