import telebot
import webbrowser
from telebot import types

bot = telebot.TeleBot("6044281281:AAH0pb6vyjvoMyNznYQRRtEgS01kbc4pcyI")


@bot.message_handler(content_types=['text'])
def get_photo(message):
    webbrowser.open("http://" + message.text)
    


    #bot.reply_to(message, 'beautiful photo!')

bot.polling(none_stop=True)