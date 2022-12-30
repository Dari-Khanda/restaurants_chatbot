import telegram as telegram
import numpy as np
import pandas as pd
from telegram.ext import Updater, CommandHandler

Token = '5961342193:AAHSKbWve55wMb8Z6mNFq44tQCGDW6Trnjs'
updater = Updater('5961342193:AAHSKbWve55wMb8Z6mNFq44tQCGDW6Trnjs', use_context='True')
dispatcher = updater.dispatcher


def start(update, context):
    update.message.reply_text('This is a restaurant advisor bot')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.start_polling()
