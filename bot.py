import telebot;

from telebot import types

TOKEN = '1887842441:AAGN81A2jQzghUsZpKdOlTgRLO2II8_1cQk'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):    
	
	#keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton("Start performance")
    
    markup.add(item1)
    
    bot.send_message(message.chat.id, "Hello, {0.first_name}!\n I am a bot, that will show you perfomance.".format(message.from_user, bot.get_me()), reply_markup = markup)

@bot.message_handler(content_types=['text'])
def write_text(message):    
	if message.text == "Start performance":
		bot.send_message(message.chat.id, 'Sorry, bot is still under development.\n Please, try again later, good luck!')

bot.polling(none_stop=True)