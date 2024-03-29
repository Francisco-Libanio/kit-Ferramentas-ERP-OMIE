from SCRIPTS.Omie import (
    OmieListarNF,
    OmieListarNotaEnt,
    OmieListarProdutoFornecedor,
    OmieListarRecebimentos,
    OmieAlterarPrecoItem,
    OmieListarProjetos,
    OmieAlterarProduto,
    OmieConsultarCliente,
    OmieConsultarProduto,
    OmieConsultarPedido,
    OmieConsultarVendedor,
    OmieListarAnexo,
    OmieListarCenarios,
    OmieListarClientes,
    OmieListarContasPagar,
)
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


def test_a_resposta_da_funcao_OmieAlterarPrecoItem_metodo_executar():
    consulta = OmieAlterarPrecoItem('EmpresaTeste')
    resposta = consulta.executar()
    assert isinstance(resposta, dict)


def test_a_resposta_da_funcao_OmieAlterarProduto_metodo_executar():
    consulta = OmieAlterarProduto('EmpresaTeste')
    resposta = consulta.executar()
    assert isinstance(resposta, dict)


def test_a_resposta_da_funcao_OmieConsultarCliente_metodo_executar():
    consulta = OmieConsultarCliente('EmpresaTeste')
    resposta = consulta.executar()
    assert isinstance(resposta, dict)


def test_a_resposta_da_funcao_OmieConsultarProduto_metodo_executar():
    consulta = OmieConsultarProduto('EmpresaTeste')
    resposta = consulta.executar()
    assert isinstance(resposta, dict)


def test_a_resposta_da_funcao_OmieConsultarPedido_metodo_executar():
    consulta = OmieConsultarPedido('EmpresaTeste')
    resposta = consulta.executar()
    assert isinstance(resposta, dict)


def test_a_resposta_da_funcao_OmieConsultarVendedor_metodo_executar():
    consulta = OmieConsultarVendedor('EmpresaTeste')
    resposta = consulta.executar()
    assert isinstance(resposta, dict)


def test_a_resposta_da_funcao_OmieListarAnexo_metodo_executar():
    consulta = OmieListarAnexo('EmpresaTeste')
    resposta = consulta.executar()
    assert isinstance(resposta, dict)


def test_a_resposta_da_funcao_OmieListarCenarios_metodo_executar():
    consulta = OmieListarCenarios('EmpresaTeste')
    resposta = consulta.executar()
    assert isinstance(resposta, dict)


def test_a_resposta_da_funcao_OmieListarClientes_metodo_executar():
    consulta = OmieListarClientes('EmpresaTeste')
    resposta = consulta.executar()
    assert isinstance(resposta, dict)


def test_a_resposta_da_funcao_OmieListarClientes_metodo_todos():
    consulta = OmieListarClientes('EmpresaTeste')
    resposta = consulta.todos()
    assert isinstance(resposta, list)


def test_a_resposta_da_funcao_OmieListarContasPagar_metodo_executar():
    consulta = OmieListarContasPagar('EmpresaTeste')
    resposta = consulta.executar()
    assert isinstance(resposta, dict)


def test_a_resposta_da_funcao_OmieListarContasPagar_metodo_todos():
    consulta = OmieListarContasPagar('EmpresaTeste')
    resposta = consulta.todos()
    assert isinstance(resposta, list)
