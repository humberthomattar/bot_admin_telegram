#!/usr/bin/python
# encoding: iso-8859-1

import os
from telegram.ext import CommandHandler
from telegram.ext import Updater, MessageHandler, Filters
from bot_admin import actions


updater = Updater(token=os.environ['TELEGRAM_TOKEN'])
dispatcher = updater.dispatcher


dispatcher.add_handler(CommandHandler('menu', actions.menu))
dispatcher.add_handler(CommandHandler('restart', actions.restart))
dispatcher.add_handler(MessageHandler(Filters.photo, actions.unknown))



