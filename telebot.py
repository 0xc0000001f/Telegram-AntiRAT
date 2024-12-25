import telebot

bot = telebot.TeleBot("token")


@bot.message_handler(commands=['basla', 'yardim'])
def send_welcome(message):
    bot.reply_to(message, "Selam")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
