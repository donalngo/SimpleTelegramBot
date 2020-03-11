# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 15:19:05 2020

@author: Donal
"""
import telegram
from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import utils.utterance as utterance
from Training import Training

if __name__ == '__main__':
    Training.train()
    TokenKey = "<token key here>"
    
    updater = Updater(token=TokenKey, use_context=True)
    
    dispatcher = updater.dispatcher
    
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                         level=logging.INFO)
    
    
    def chat(update, context):
        reply = utterance.getreply(update.message.text)
        print(reply)
        context.bot.send_message(chat_id=update.effective_chat.id, text=reply["Reply"])
    
    echo_handler = MessageHandler(Filters.text, chat)
    dispatcher.add_handler(echo_handler)
    
    
    updater.start_polling()
