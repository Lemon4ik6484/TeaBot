import telebot
import random

bot = telebot.TeleBot('6247170055:AAEXI3ifNAP7lVVQofz3HShL0DT1d9V15Uk')

#----------------------------------
# .  Голос Списки
#----------------------------------

# Списки возможных голосовых сообщений
voice_messages_damoi = [
    'damoi1.ogg',
    'damoi2.ogg',
    'damoi3.ogg'
    # Добавьте остальные файлы в список
]

voice_messages_pirogi = [
    'pirogi1.ogg',
    'pirogi2.ogg',
    'pirogi3.ogg',
    'pirogi4.ogg',
    'pirogi5.ogg',
    'pirogi6.ogg'
    # Добавьте остальные файлы в список
]

#------------------------
# .   Команды
#------------------------
#----------
#дамой
#----------
@bot.message_handler(commands=['\u0414\u0430\u043C\u043E\u0439'])
def send_damoi(message):
    # Выбираем случайное голосовое сообщение из списка для команды /Дамой
    voice_file = random.choice(voice_messages_damoi)

    # Отправляем голосовое сообщение
    with open(voice_file, 'rb') as voice:
        bot.send_voice(message.chat.id, voice)

@bot.message_handler(commands=['\u0434\u0430\u043C\u043E\u0439'])
def send_damoi(message):
    # Выбираем случайное голосовое сообщение из списка для команды /дамой
    voice_file = random.choice(voice_messages_damoi)

    # Отправляем голосовое сообщение
    with open(voice_file, 'rb') as voice:
        bot.send_voice(message.chat.id, voice)

#---------
#пироги
#---------

@bot.message_handler(commands=['\u041f\u0438\u0440\u043e\u0433\u0438'])
def send_pirogi(message):
    # Выбираем случайное голосовое сообщение из списка для команды /Пироги
    voice_file = random.choice(voice_messages_pirogi)

    # Отправляем голосовое сообщение
    with open(voice_file, 'rb') as voice:
        bot.send_voice(message.chat.id, voice)

@bot.message_handler(commands=['\u043f\u0438\u0440\u043e\u0433\u0438'])
def send_pirogi(message):
    # Выбираем случайное голосовое сообщение из списка для команды /пироги
    voice_file = random.choice(voice_messages_pirogi)

    # Отправляем голосовое сообщение
    with open(voice_file, 'rb') as voice:
        bot.send_voice(message.chat.id, voice)



#-------------------
# . Запуск Бота
#-------------------

bot.polling(none_stop=True)
