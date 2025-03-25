import requests
import telebot
import requests
tg_token='8138804444:AAGRDgF0oB9CY11YAlroAeQ1652t1SmsvOU'
bot=telebot.TeleBot(tg_token)
@bot.message_handler(commands=['start'])
def start_message(message):
   city=bot.send_message(message.chat.id, 'send me your city')
   bot.register_next_step_handler(city, get_weather )

def get_weather(city):
   params = {
      '?0': '',
      'lang': 'en',
      '?M': '',
   }
   weather = requests.get(f'https://wttr.in/{city.text}.png', params=params)
   with open('weather.png', 'wb') as image:
      image.write(weather.content)
   bot.send_photo(city.chat.id, open('weather.png', 'rb'),)
bot.infinity_polling()
