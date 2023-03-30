import random
from telegram.ext import Updater, CommandHandler
from telegram import Voice

# функция для обработки команды /дамой
def damoi_response(update, context):
    voices = ['voice1.ogg', 'voice2.ogg', 'voice3.ogg', 'voice4.ogg']
    voice = random.choice(voices)
    audio = open(voice, 'rb')
    voice_message = Voice(audio)
    update.message.reply_voice(voice_message)

# создаем объект для работы с Telegram API
updater = Updater(token='6119106732:AAESLt8PGqZTPwV8JgYRHWmkcAaN-DN84hc', use_context=True)

# создаем обработчик для команды /дамой
damoi_handler = CommandHandler('\u0434\u0430\u043C\u043E\u0439', damoi_response)

# регистрируем обработчик в объекте updater
updater.dispatcher.add_handler(damoi_handler)

# запускаем бота
updater.start_polling()

# останавливаем бота при получении сигнала SIGINT (Ctrl+C)
updater.idle()
