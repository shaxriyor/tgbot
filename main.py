import telebot
from telebot import types

bot = telebot.TeleBot('5494535504:AAHEgpiPD3_94Ep1fj14c14tdVxGo8Yp28U')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'*Hello,* [{message.from_user.first_name}](https://t.me/{message.from_user.username})'
    bot.send_message(message.chat.id, mess, parse_mode='markdown')

@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text=="Hello" or message.text=="hello":
        bot.send_message(message.chat.id, "И тебе привет!", parse_mode='html')
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Твой ИД: {message.from_user.id}", parse_mode='html' )
    else:
        bot.send_message(message.chat.id,"я тебя не понимаю", parse_mode='html' )

@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Wow!')

@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить Inha.uz", url="https://inha.uz"))
    bot.send_message(message.chat.id, 'Наш сайт', reply_markup=markup)

@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton("Веб сайт")
    start = types.KeyboardButton("start")

    markup.add(website, start)
    bot.send_message(message.chat.id, 'Наш сайт', reply_markup=markup)


bot.polling(none_stop=True)


