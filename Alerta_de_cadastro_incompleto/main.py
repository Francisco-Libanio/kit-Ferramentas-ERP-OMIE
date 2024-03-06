import os
import requests
from datetime import date
from dotenv import load_dotenv
import dotenv
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from gspread_dataframe import get_as_dataframe, set_with_dataframe
from pprint import pprint
from Omie import OmieConsultarProduto, Omie
#from objeto_email import Enviandoemail

dotenv.load_dotenv(dotenv.find_dotenv())

# Escopo utilizado
scope = ['https://spreadsheets.google.com/feeds']
id_planilha = os.getenv('id-planilha')
credentials = ServiceAccountCredentials.from_json_keyfile_name('credential.json', scope)
gc = gspread.authorize(credentials)

id_planilha = (id_planilha)  # CORRIGIR ERRO DE ATRIBUIÇÃO

wks = gc.open_by_key(id_planilha)

# Selecionando a primeira página da planilha
worksheet = wks.get_worksheet(0)

# Obtendo todos os valores das colunas
values_id = worksheet.col_values(1)[1:]

print(values_id)
lista_de_resultados = []
credencial = Omie('credencial')

for codigo_planilha in values_id:
    consultar_produto = Omie('credencial').ConsultarProduto
    consultar_produto.codigo = codigo_planilha
    resultado_consulta = consultar_produto.executar()
    lista_de_resultados.append(resultado_consulta)

produtos_conf = []
lista_vazia =[]
for i, produto in enumerate(lista_de_resultados):
    # print(lista_de_resultados)
    info_faltantes = ()

    codigo_id = lista_de_resultados[i]['codigo']
    info_faltantes += (codigo_id,)

    nome = lista_de_resultados[i]['descricao']
    info_faltantes += (nome,)

    codigo_de_barras = lista_de_resultados[i]['ean']
    if codigo_de_barras == '':
        info_faltantes += (codigo_de_barras,)

    preco = lista_de_resultados[i]['valor_unitario']
    if preco == 0:
        info_faltantes += (preco,)

    venda_em_ecommerce = lista_de_resultados[i]['recomendacoes_fiscais']['market_place']
    if venda_em_ecommerce == 'N':
        info_faltantes += (venda_em_ecommerce,)

    peso_liquido = lista_de_resultados[i]['peso_liq']
    if peso_liquido == 0:
        info_faltantes += (peso_liquido,)

    peso_bruto = lista_de_resultados[i]['peso_bruto']
    if peso_bruto == 0:
        info_faltantes += (peso_bruto,)

    altura = lista_de_resultados[i]['altura']
    if altura == 0:
        info_faltantes += (altura,)

    largura = lista_de_resultados[i]['largura']
    if largura == 0:
        info_faltantes += (largura,)

    profundidade = lista_de_resultados[i]['profundidade']
    if profundidade == 0:
        info_faltantes += (profundidade,)

    marca = lista_de_resultados[i]['marca']
    if marca == '':
        info_faltantes += (marca,)

    modelo = lista_de_resultados[i]['modelo']
    if modelo == '':
        info_faltantes += (modelo,)

    imagem = lista_de_resultados[i]['imagens']
    if imagem == lista_vazia:
        info_faltantes +=(imagem,)

    caracteristica = lista_de_resultados[i]['caracteristicas']
    if caracteristica == None:
        info_faltantes +=(caracteristica,)

    familia = lista_de_resultados[i]['descricao_familia']
    if familia == '':
        info_faltantes += (familia,)
    produtos_conf.append(info_faltantes)
pprint(produtos_conf)

#TODO CRIAR FILTRO POR COLABORADOR E NÃO POR PRODUTO