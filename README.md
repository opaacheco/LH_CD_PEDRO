# Análise Exploratória de Dados - Desafio Indicium IMDB

Este projeto realiza uma análise exploratória de dados (EDA) em um conjunto de dados de filmes fornecido pelo Desafio Indicium IMDB. A análise inclui limpeza de dados, transformações de tipo, visualizações e correlações para descobrir padrões e insights relevantes.

## Requisitos

- Python 3.x
- Pandas
- Matplotlib

## Estrutura do Projeto

- `desafio_indicium_imdb.csv`: Arquivo CSV contendo os dados dos filmes.
- `main.py`: Script principal contendo o código de análise de dados.
- `README.md`: Documentação do projeto.

## Instalação

1. Clone o repositório para sua máquina local:

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Instale as dependências necessárias:

   ```bash
   pip install -r requirements.txt
   ```

3. Execute o script principal:

   ```bash
   python main.py
   ```

Para visualizar o notebook:

1. Certifique-se de ter o Jupyter Notebook instalado:

   ```bash
   pip install notebook
   ```

2. Execute o Jupyter Notebook:

   ```bash
   jupyter notebook EDA_IMDB.ipynb
   ```

3. Alternativamente, você pode visualizar o relatório em PDF:
   - Baixe o arquivo `EDA_IMDB.pdf` do repositório.

### Exportar Notebook para PDF

Se desejar exportar o notebook para PDF:

1. Instale o nbconvert:

   ```bash
   pip install nbconvert
   ```

2. Execute o comando:
   ```bash
   jupyter nbconvert --to pdf EDA_IMDB.ipynb
   ```

### Carregar e Visualizar os Dados

O script começa carregando os dados do arquivo CSV e exibindo as primeiras e últimas linhas para uma visualização inicial.

```python
import pandas as pd
import matplotlib.pyplot as plt

def carregar_dados(caminho):
    try:
        return pd.read_csv(caminho)
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return None

caminho = 'desafio_indicium_imdb.csv'
df = carregar_dados(caminho)

print(df.head())
print(df.tail())
```

### Perguntas de entregas

Qual filme você recomendaria para uma pessoa que você não conhece?

-Pelas análises no código, eu indicaria o melhor filme pelo IMDB, considerando uma direção que já produziu boas obras ao longo da carreira, uma boa média no IMDB e atores com boas avaliações também.

Quais são os principais fatores relacionados com alta expectativa de faturamento de um filme?

-Os principais fatores são o número de votos, o diretor e as estrelas do filme.

Quais insights podem ser obtidos com a coluna Overview? É possível inferir o gênero do filme a partir dessa coluna?

-Com a coluna de Overview, podemos identificar palavras-chave que indicam o tipo de filme que vamos assistir. Por exemplo, se Jason Statham estiver em um filme cujo Overview sugere muita ação, podemos esperar que o filme seja do gênero ação e ter expectativas sobre sua qualidade cruzando essas informações com as dos atores principais.

3 - Explique como você faria a previsão da nota do imdb a partir dos dados. Quais variáveis e/ou suas transformações você utilizou e por quê? Qual tipo de problema estamos resolvendo (regressão, classificação)? Qual modelo melhor se aproxima dos dados e quais seus prós e contras? Qual medida de performance do modelo foi escolhida e por quê?

-Estamos resolvendo umas questão de regressão, para prever o imdb eu iria sempre nos atores envolvidos, diretor do filme e numero de votos.
Regressão ajuda na Simplicidade e interpretabilidade: Fácil de entender e explicar como cada variável afeta a previsão.
Rápido treinamento e predição e atrapalha assumindo linearidade entre variáveis: Pode não capturar relações complexas e não lineares nos dados.
Sensível a outliers: Pode ser influenciado negativamente por valores extremos nos dados.

4 - Supondo um filme com as seguintes características:

{'Series_Title': 'The Shawshank Redemption',
'Released_Year': '1994',
'Certificate': 'A',
'Runtime': '142 min',
'Genre': 'Drama',
'Overview': 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
'Meta_score': 80.0,
'Director': 'Frank Darabont',
'Star1': 'Tim Robbins',
'Star2': 'Morgan Freeman',
'Star3': 'Bob Gunton',
'Star4': 'William Sadler',
'No_of_Votes': 2343110,
'Gross': '28,341,469'}

Qual seria a nota do IMDB?
-Analisando pelo que nos temos de número de votos fazer a mediana desse filme, seria 8.32 a nota IMDB como podemos analisar no notebook
