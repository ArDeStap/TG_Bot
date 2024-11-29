import telebot

BotToken = '8086375056:AAHkaBly0bz2OjSL9llLXIHKk75LcMQkWUE'

bot = telebot.TeleBot(BotToken)

@bot.message_handler(commands=['start'])
def Bot_Start(msg):
    bot.reply_to(msg, "Hello, I'm Telegram Bot")



bot.infinity_polling()