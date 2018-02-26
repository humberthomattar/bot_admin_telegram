#!/usr/bin/python
# encoding: iso-8859-1

import sys
import telegram
from threading import Thread
from bot_admin import control
from bot_admin import *


def menu(bot, update):
    main_menu_keyboard = [
                       [telegram.KeyboardButton('/menu')],
                       [telegram.KeyboardButton('/restart')]
    ]
    reply_kb_markup = telegram.ReplyKeyboardMarkup(
                    main_menu_keyboard,
                    resize_keyboard=True,
                    one_time_keyboard=True
    )
    bot.send_message(
        chat_id=update.message.chat_id,
        text=msg['menu'],
        reply_markup=reply_kb_markup
    )
    logger.debug('menu apresentado')

def unknown(bot, update):
    try:
        if update.message.caption is None:
            res = utils.post_with_query_string(
                url=url_api + 'deleteMessage',
                params={
                    'chat_id':update.message.chat_id,
                    'message_id':update.message.message_id
                },
                headers={
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
            )
            update.message.reply_text(msg['delete_media'])
            logger.info(res.text)
    except Exception as e:
        logger.error(str(e))


def stop_and_restart():
    control.updater.stop()
    os.execl(sys.executable, sys.executable, *sys.argv)


def restart(bot, update):
    logger.info('Reiniciando o bot...')
    Thread(target=stop_and_restart).start()
    logger.info('Bot reiniciado com sucesso!')
