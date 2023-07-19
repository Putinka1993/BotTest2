import telebot

from telebot import types

bot = telebot.TeleBot("6044281281:AAH0pb6vyjvoMyNznYQRRtEgS01kbc4pcyI")


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Перейти на сайт", url="https://google.com"))
    


    bot.reply_to(message, 'beautiful photo!')

bot.polling(none_stop=True)