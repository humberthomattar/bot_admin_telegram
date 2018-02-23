import os
import telegram
from telegram.ext import CommandHandler
from telegram.ext import Updater, MessageHandler, Filters
from utils import *


FILE_CHATS = 'chats.json'

def start(bot, update):
    try:
        bot.send_message(
            chat_id=update.message.chat_id,
            text=MSG["BOT_MSG_START"]
        )
        inscrever(update)
        menu_principal(bot, update)
    except Exception as e:
        print(str(e))


def inscrever(update):
    try:
        chats = load_json(FILE_CHATS)
        if update.message.chat_id not in chats['chat_id']:
            chats['chat_id'].append(update.message.chat_id)
            write_json(FILE_CHATS, chats)
            return
    except Exception as e:
        logger.error(str(e))
        return


def desinscrever(bot, update):
    try:
        chats = load_json(FILE_CHATS)
        if update.message.chat_id not in chats['chat_id']:
            bot.send_message(
                chat_id=update.message.chat_id,
                text=MSG['BOT_MSG_DESINSC_NOK']
            )
        else:
            chats['chat_id'].remove(update.message.chat_id)
            write_json(FILE_CHATS, chats)
            bot.send_message(
                chat_id=update.message.chat_id,
                text=MSG['BOT_MSG_DESINSC_OK']
            )
    except Exception as e:
        logger.error(str(e))


def menu_principal(bot, update):
    main_menu_keyboard = [
                       [telegram.KeyboardButton('/menu')],
                       [telegram.KeyboardButton('/inscrever')],
                       [telegram.KeyboardButton('/desinscrever')],
                       [telegram.KeyboardButton('/sistemas')]
    ]
    reply_kb_markup = telegram.ReplyKeyboardMarkup(
                    main_menu_keyboard,
                    resize_keyboard=True,
                    one_time_keyboard=True
    )
    bot.send_message(
        chat_id=update.message.chat_id,
        text=MSG['BOT_MSG_MENU'],
        reply_markup=reply_kb_markup
    )


def unknown(bot, update):
    try:

        bot.send_message(
            chat_id=update.message.chat_id,
            text=MSG['BOT_MSG_UNKNOWN']
        )
    except Exception as e:
        logger.error(e)


logger.info('Inicio do bot')
updater = Updater(token=os.environ['TELEGRAM_TOKEN'])
dispatcher = updater.dispatcher

# Criacao dos objetos de comando
start_handler = CommandHandler('start', start)
menu_principal_handler = CommandHandler('menu', menu_principal)
inscrever_handler = CommandHandler('inscrever', inscrever)
desinscrever_handler = CommandHandler('desinscrever', desinscrever)
unknown_handler = MessageHandler(Filters.command, unknown)

# add Comandos ao dispatcher
dispatcher.add_handler(start_handler)
dispatcher.add_handler(menu_principal_handler)
dispatcher.add_handler(inscrever_handler)
dispatcher.add_handler(desinscrever_handler)
dispatcher.add_handler(unknown_handler)

# start bot
updater.start_polling()
updater.idle()