#!/usr/bin/python
# encoding: iso-8859-1

import json
import requests
from bot_admin import *


def load_json(file):
    """
    :objetivo: Funcao especializada na leitura do arquivo json especificado.
    :param file: Path do arquivo json que sera lido pela aplicacao.
    :return: Dicionario com as chaves e valores do arquivo json.
    """
    try:
        with open(file) as data:
            return json.load(data)
    except Exception as e:
        logger.error(
            'Erro no parser dos dados!! - Detalhamento: ' + str(e)
        )


def post_with_query_string(**kwargs):
    """ Realizar a chamada REST/POST via modulo requests utilizando query string.
    :param:  Endereco da API/ metodo POST que sera consumido.
    :param: params: params é uma dict utilizada na query string.
    :return: Retorna o objeto request com seus atributos.
    """
    try:
        return requests.post(
            kwargs['url'],
            data=kwargs['params'],
            headers=kwargs['headers'],
            timeout=30
        )
    except Exception as e:
        logger.error(str(e))
        return

