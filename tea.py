import random
import sqlite3
import telebot
import time

# Инициализируем бота
bot = telebot.TeleBot('YOUR_TOKEN')

# Функция для обработки команды "/чай"
@bot.message_handler(commands=['чай'])
def tea_handler(message):
    # Получаем имя пользователя и его ID
    user = message.from_user
    user_id = user.id

    # Соединяемся с базой данных
    conn = sqlite3.connect('tea_data.db')
    cursor = conn.cursor()

    # Создаем таблицу, если она не существует
    cursor.execute('''CREATE TABLE IF NOT EXISTS tea_records
                      (user_id INTEGER PRIMARY KEY,
                      total_tea_amount INTEGER,
                      last_tea_drink_time INTEGER)''')

    # Получаем время последнего выпитого чая пользователем
    cursor.execute("SELECT last_tea_drink_time FROM tea_records WHERE user_id = ?", (user_id,))
    last_tea_drink_time = cursor.fetchone()

    # Если пользователь уже пил чай в последние 30 минут, то выводим сообщение об ошибке
    if last_tea_drink_time is not None and time.time() - last_tea_drink_time[0] < 1800:
        bot.reply_to(message, "Вы уже пили чай недавно, попробуйте еще раз через 30 минут")
        conn.close()
        return

    # Генерируем случайное количество выпитого чая
    tea_amount = random.randint(1, 20)

    # Получаем количество выпитого чая пользователем всего
    cursor.execute("SELECT total_tea_amount FROM tea_records WHERE user_id = ?", (user_id,))
    total_tea_amount = cursor.fetchone()

    # Если пользователь еще не пил чай, то количество выпитого чая всего равно 0
    if total_tea_amount is None:
        total_tea_amount = 0
    else:
        total_tea_amount = total_tea_amount[0]

    # Обновляем количество выпитого чая пользователем всего и время последнего выпитого чая
    total_tea_amount += tea_amount
    last_tea_drink_time = int(time.time())
    cursor.execute("INSERT OR REPLACE INTO tea_records (user_id, total_tea_amount, last_tea_drink_time) VALUES (?, ?, ?)", (user_id, total_tea_amount, last_tea_drink_time))

    # Формируем текст сообщения
    message_text = f"{user.first_name} {user.last_name}, ты выпил {tea_amount} литров чая\nВыпито всего - {total_tea_amount} литров чая"

    # Отправляем сообщение пользователю
    bot.reply_to(message, message_text)

    # Сохраняем изменения в базе
    conn.commit()
    conn.close()

# Запускаем бота
bot.polling()