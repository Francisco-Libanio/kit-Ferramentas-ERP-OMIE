from datetime import datetime, timedelta
import Omie
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from gspread_dataframe import get_as_dataframe, set_with_dataframe

lojas = ['Empresa1', 'Empresa2', 'Empresa3']

data_frames_vendas_por_loja = {}

for loja in lojas:
    exemplo = Omie.Omie(loja).ListarCuponsFiscais
    exec = exemplo.todos()

    vendas = []

    for i, item in enumerate(exec):
        data_hoje = datetime.now()
        data_ontem = data_hoje - timedelta(days=1)
        data_ontem_formatada = data_ontem.strftime("%d/%m/%Y")

        data = exec[i]['cabecalhoCupom']['dDtEmissaoCupom']

        if data == data_ontem_formatada:
            itens_por_compra = len(exec[i]['itensCupom'])
            data_da_venda = exec[i]['cabecalhoCupom']['dDtEmissaoCupom']
            hora_da_venda = exec[i]['cabecalhoCupom']['cHrEmissaoCupom']
            n_nota = exec[i]['cabecalhoCupom']['nNumCupom']
            nota_canc = exec[i]['cabecalhoCupom']['info']['cCupomCancelado']
            valor_do_cupom = round(exec[i]['cabecalhoCupom']['nValorCupom'] / itens_por_compra, 4)

            # Iterar sobre os produtos da venda (itensCupom)
            for produto in exec[i]['itensCupom']:
                nome_produto = produto['xProd']
                codigo_produto = produto['cCodigo']
                qtd_item = produto['nQuant']
                total_mercadoria = produto['vItem']
                valor_desconto = produto['vDesc']

                # Criar um dicionário para cada produto com as informações
                venda_produto = {
                    'Data da venda': data_da_venda,
                    'Hora da venda': hora_da_venda,
                    'Numero da nota': n_nota,
                    'Nota Cancelada': nota_canc,
                    'Nome do produto': nome_produto,
                    'Código do produto': codigo_produto,
                    'Qtd do Item': qtd_item,
                    'Total da mercadoria': total_mercadoria,
                    'Valor de desconto': valor_desconto,
                    'valor total da compra': valor_do_cupom
                }

                vendas.append(venda_produto)

    df_vendas = pd.DataFrame(vendas)
    data_frames_vendas_por_loja[loja] = df_vendas

for loja, df in data_frames_vendas_por_loja.items():
    print(df)
    print(loja)

# enviando dados para google sheets
scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('credential.json', scope)

gc = gspread.authorize(credentials)

# Abrindo a planilha
wks = gc.open_by_key('Id-planilha')

aba = 1

for loja, df in data_frames_vendas_por_loja.items():
    df = df.assign(Loja=loja)

    # Selecionando a primeira página da planilha
    worksheet = wks.get_worksheet(aba)
    aba += 1
    # Obter os valores da coluna b
    column_b_values = worksheet.col_values(1)

    # Contar as linhas com células não vazias na coluna B
    linhas_com_conteudo_na_coluna_b = sum(1 for cell in column_b_values if cell)

    linha_inicio_dataframe = linhas_com_conteudo_na_coluna_b + 1

    set_with_dataframe(worksheet, df, row=linha_inicio_dataframe, include_index=False, include_column_header=False)
    print('Planilha atualizada')
