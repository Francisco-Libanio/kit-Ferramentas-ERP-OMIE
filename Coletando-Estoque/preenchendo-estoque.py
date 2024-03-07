import os
import requests
from dotenv import load_dotenv
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from gspread_dataframe import get_as_dataframe, set_with_dataframe
import Omie


data_frames_estoque = []  # Lista para armazenar os dataframes de cada loja

exemplo = Omie.Omie('loja').ListarPosEstoque
lista_estoque = exemplo.todos()

estoque = []
for i, c in enumerate(lista_estoque):
    codigo_do_produto = str(lista_estoque[i]['cCodigo'])
    qtd_estoque = lista_estoque[i]['nSaldo']
    preco = lista_estoque[i]['nPrecoUnitario']
    descricao = lista_estoque[i]['cDescricao']

    estoque_completo = [codigo_do_produto, qtd_estoque, preco, descricao]
    estoque.append(estoque_completo)

# Criando o DataFrame a partir da lista de estoque
df_estoque_loja = pd.DataFrame(estoque, columns=['Código do produto', 'Estoque', 'Preço', 'Descrição'])
df_estoque_loja['Total'] = df_estoque_loja['Preço'] * df_estoque_loja['Estoque']


# Escopo utilizado
scope = ['https://spreadsheets.google.com/feeds']

# Dados de autenticação
credentials = ServiceAccountCredentials.from_json_keyfile_name('credential.json', scope)

# Autenticando
gc = gspread.authorize(credentials)

# Abrindo a planilha
wks = gc.open_by_key('id_planilha')

# Selecionando a primeira página da planilha
worksheet = wks.get_worksheet(1)

set_with_dataframe(worksheet, df_estoque_loja, include_index=False)
