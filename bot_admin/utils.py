#!/usr/bin/python
# encoding: iso-8859-1

import json
import requests
import logging


def write_json(file, data):
    try:
        with open(file, 'w') as outfile:
            json.dump(data, outfile)
    except Exception as e:
        logger.error(
            'Não foi possível gravar no arquivos \
            json as informações desejadas.'
        )
        logger.error(str(e))


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
            'Erro no parser das configurações!! - Detalhamento: ' + str(e)
        )


def post_with_query_string(**kwargs):
    """ Realizar a chamada REST - POST via módulo requests utilizando query string.

    :usage:
            t = utils.post_with_query_string(
                      url=url, params={'key1': int1, 'key2': value2}
            )
            OR
            params = {
                        'key_1': value_1,
                        'key_2': 'value_2'
                    }

            t = utils.post_with_query_string(url=url, params=params)

    :param:  Endereço da API/ metodo POST que será consumido.
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
        return False

MSG = load_json('bot_msg.json')

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s [%(levelname)-8s]: %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S'
)

logger = logging.getLogger(__name__)