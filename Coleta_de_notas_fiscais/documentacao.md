# Documentação Técnica

## Dependências
- Python 3.x
- Omie
- pandas
- gspread
- oauth2client

## Descrição

Esse script tem como objetivo a coleta de dados de vendas de vários OMIE-PDV O propósito é coletar os dados de vendas cadastrados
na nota fiscal do dia anterior. 
As vendas de cada PDV serão cadastradas dentro de uma planilha em abas separadas e presenversando os dados já existentes.

## Funcionalidades Principais
- Extrai dados de vendas de cupons fiscais de várias lojas.
- Filtra as vendas do dia anterior.
- Cria um DataFrame do pandas com os dados das vendas.
- Envia os dados das vendas para uma planilha do Google Sheets, uma para cada loja.

## Variáveis de ambiante:
 Crie um arquivo .env e cadastre dentro dele : 
 credenciais de acesso do google sheets Para saber como obter sua credencial [clique aqui](https://www.linkedin.com/pulse/conectando-ao-google-sheets-utilizando-api-francisco-libanio-rrhuf/?trackingId=Rx%2BjPn1USMu8zguoPr5o2Q%3D%3D)
 Id da planilha que receberá o ID da planilha.
1. Substitua `'Empresa1'`, `'Empresa2'`, `'Empresa3'` na lista `lojas` pelas lojas desejadas.
2. Substitua `'credential.json'` pelo caminho do arquivo de credenciais JSON do Google.
3. Substitua `'Id-planilha'` pelo ID da planilha do Google Sheets.
4. Execute o script Python.

## Tabela 
A tabela formada pelo script terá o seguinte formato.

```markdown
| Data       | Hora  | Número da Nota | Nota Cancelada | Descrição | Código | Quantidade | Valor do Produto | Desconto | Valor da Nota | Loja |
|------------|-------|----------------|----------------|-----------|--------|------------|------------------|----------|---------------|------|
| 2024-03-08 | 09:00 | 001            | Não            | Item A    | A001   | 2          | $10.00           | $1.00    | $19.00        | Loja A |
| 2024-03-08 | 09:15 | 002            | Sim            | Item B    | B002   | 1          | $25.00           | $0.00    | $0.00         | Loja B |
| 2024-03-08 | 09:30 | 003            | Não            | Item C    | C003   | 3          | $15.00           | $2.50    | $42.50        | Loja A |
| 2024-03-08 | 10:00 | 004            | Não            | Item D    | D004   | 1          | $30.00           | $5.00    | $25.00        | Loja C |
```

Nesta tabela:

- "Data" representa a data da transação.
- "Hora" indica o horário da transação.
- "Número da Nota" é o número identificador da nota fiscal.
- "Nota Cancelada" indica se a nota foi cancelada (S/N).
- "Descrição" é uma breve descrição do produto.
- "Código" é o código identificador do produto.
- "Quantidade" mostra a quantidade de produtos vendidos.
- "Valor do Produto" representa o preço unitário do produto.
- "Desconto" indica o desconto aplicado na transação.
- "Valor da Nota" é o valor total da nota fiscal.
- "Loja" é o nome da loja onde a transação ocorreu.

