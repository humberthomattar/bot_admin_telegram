#!/usr/bin/python
# encoding: iso-8859-1

import os
import logging
from bot_admin import utils

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s [%(levelname)-8s]: %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S'
)

logger = logging.getLogger(__name__)

msg = utils.load_json('bot_admin/messages.json')

url_api = 'https://api.telegram.org/bot%s/' % os.environ['TELEGRAM_TOKEN']

