from SCRIPTS.Omie import OmieListarNF, OmieListarNotaEnt, OmieListarProdutoFornecedor, OmieListarRecebimentos,OmieListarProjetos
import requests
from unittest.mock import patch
import os
from datetime import date
from dotenv import load_dotenv
import httpx


def test_a_resposta_do_metodo_OmieListarNF_executar():
    consulta = OmieListarNF('EmpresaTeste')
    resposta = consulta.executar()
    assert isinstance(resposta, dict)


def test_a_resposta_do_metodo_OmieListarNF_todos():
    consulta = OmieListarNF('EmpresaTeste')
    resposta = consulta.todos()
    assert isinstance(resposta, list)


def test_a_respostas_da_funcao_OmieListarNotaEnt_metodo_executar():
    consulta = OmieListarNotaEnt('EmpresaTeste')
    resposta = consulta.executar()
    assert isinstance(resposta, dict)


def test_a_resposta_da_funcao_ListarProdutoFornecedor_metodo_executar():
    consulta = OmieListarProdutoFornecedor('EmpresaTeste')
    resposta = consulta.executar()
    assert isinstance(resposta, dict)


def test_a_resposta_da_funcao_ListarProdutoFornecedor_metodo_todos():
    consulta = OmieListarProdutoFornecedor('EmpresaTeste')
    resposta = consulta.todos()
    assert isinstance(resposta, list)


def test_a_resposta_da_funcao_ListarRecebimnetos_metodo_executar():
    consulta = OmieListarRecebimentos('EmpresaTeste')
    resposta = consulta.executar()
    assert isinstance(resposta, dict)

def test_a_resposta_da_funcao_OmieListarProjetos_metodo_executar():
    consulta = OmieListarProjetos('EmpresaTeste')
    resposta = consulta.executar()
    assert isinstance(resposta, dict)

def test_a_resposta_da_funcao_OmieListarProjetos_metodo_todos():
    consulta = OmieListarProjetos('EmpresaTeste')
    resposta = consulta.todos()
    assert isinstance(resposta, list)