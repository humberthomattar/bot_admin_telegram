#!/usr/bin/python
# encoding: iso-8859-1

from bot_admin.control import updater
from bot_admin import logger


if __name__ == '__main__':
    logger.info('start bot.')
    updater.start_polling()
    updater.idle()
