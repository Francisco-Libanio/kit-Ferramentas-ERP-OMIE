from SCRIPTS.Omie import OmieListarNF
import requests
from unittest.mock import patch
import os
from datetime import date
from dotenv import load_dotenv
import httpx

def test_a_resposta_do_metodo_OmieListarNF():
    consulta = OmieListarNF('EmpresaTeste')

    # Chama o método executar() da instância
    resposta = consulta.executar()
    # Verifica se a resposta é 200
    assert isinstance(resposta,dict)
