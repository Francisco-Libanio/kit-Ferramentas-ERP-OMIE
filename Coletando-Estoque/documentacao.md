# Objetivo 
Esse script tem como objetivo realizar a coleta as infomrações de estoque de um determinado  app no ERP-OMIE e porteriormente cadastra-los em uma planilha do google sheets, essa é uma opção foi escolhida com foco em uma opção para operações que possuem poucos recursos de investimentos em tecnologia e equipe reduzida. 

## Dependências Externas:
- `os`: Biblioteca Python para interação com o sistema operacional, utilizada para manipulação de arquivos.
- `requests`: Biblioteca Python para realizar requisições HTTP, utilizada para acessar a API do ERP-OMIE.
- `dotenv`: Biblioteca Python para carregar variáveis de ambiente de um arquivo `.env`.
- `pandas`: Biblioteca Python para manipulação e análise de dados, utilizada para criar e manipular estruturas de dados tabulares.
- `gspread`: Biblioteca Python para interagir com o Google Sheets.
- `oauth2client`: Biblioteca Python para lidar com a autenticação OAuth 2.0.
- `gspread_dataframe`: Extensão da biblioteca `gspread` para facilitar a integração com DataFrames do pandas.
- `Omie`: Módulo contendo a classe `Omie` para interação com a API do ERP-OMIE.

## Variáveis de ambiante:
Crie um arquivo .env e cadastre dentro dele : 
credenciais de acesso do google sheets Para saber como obter sua credencial (clique aqui)[https://www.linkedin.com/pulse/conectando-ao-google-sheets-utilizando-api-francisco-libanio-rrhuf/?trackingId=Rx%2BjPn1USMu8zguoPr5o2Q%3D%3D]
Id da planilha que receberá o ID da planilha.
Credenciais de acesso OMIE (Api_key e Api_Screts ).
Dentro deste diretório tem um exemplo de arquivo 


## Tabela de Dados:
O DataFrame criado será composto pelas seguintes colunas:
- **Código do produto**: O código identificador único do produto.
- **Estoque**: A quantidade em estoque do produto.
- **Preço**: O preço unitário do produto.
- **Descrição**: A descrição do produto.
- **Valor do estoque**: O valor total do estoque do produto (calculado como o produto da quantidade em estoque pelo preço unitário).

Exemplo de estrutura do DataFrame:
| Código do produto | Estoque | Preço | Descrição | Valor do estoque |
|-------------------|---------|-------|-----------|------------------|
| 001               | 100     | $10   | Produto A | R$ 1000            |
| 002               | 75      | $15   | Produto B | R$ 1125            |
| 003               | 50      | $20   | Produto C | R$ 1000            |



## Fluxo de Execução:
1. O script importa as bibliotecas necessárias e carrega as variáveis de ambiente do arquivo `.env`.
2. Utiliza a classe `Omie` para acessar a API do ERP-OMIE e obter a lista de produtos em estoque.
3. Itera sobre a lista de produtos e extrai as informações necessárias, como código do produto, quantidade em estoque, preço e descrição.
4. Calcula o valor total do estoque de cada produto.
5. Cria um DataFrame do pandas com as informações coletadas.
6. Autentica no Google Sheets utilizando as credenciais fornecidas.
7. Abre a planilha especificada pelo ID e seleciona a primeira página da planilha.
8. Exporta o DataFrame para a planilha do Google Sheets.

## Saída:
A saída do script é um DataFrame do pandas contendo informações detalhadas sobre o estoque de produtos do ERP-OMIE, incluindo código do produto, quantidade em estoque, preço, descrição e valor total do estoque de cada produto. Além disso, os dados são exportados para uma planilha do Google Sheets especificada.

## Posibilidades
- Com os dados cadastrados pode se criar uma dashboard utilizando a ferramenta Google looker Studio
- Pode se Realizar a automação de execuçaõ do Script utilizando a biblioteca schedule, Cron em sistemas Linux ou Gerenciados de tarefas em sistemas Windows.