import config
import markup as markup
import telebot
import requests
from bs4 import BeautifulSoup as BS
from telebot import types

bot = telebot. TeleBot(config.token)
response = requests.get(config.url).json()

@bot.message_handler(commands=['start', 'help'])
def main(message):
 markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
 itembtn1 = types.KeyboardButton( "Погода")
 itembtn2 = types.KeyboardButton('Курс валют')
markup.add(itembtn1, itembtn2)
msg = bot.send_message(message.chat.id, 'Привіт, виберіть дію', reply_markup-markup)
bot.register_next_step_handler(msg, process_switch_step)
def process_switch_step(message):
 if (sessage.text 'Погода'):
weather (message)
elif (message.text 'Курс валют'):
coins(message)
def weather (message):
    '''Це функція погоди'''
    markup = types.ReplyKeyboardRemove(selective = False)
    r = requests.get("https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BB%D1%83%D1%86%D0%BA")
    for el in html.select(#content'):
         t_min = el.select('.temperature .min')[0].text
         t_max = el.select('.temperature .max')[0].text
         text = el.select('.wDescription .description')[0].text
         bot.send_message(message.chat.id, "Привіт, погода на сьогодні:/n" + t_min + ', ' + t_max + '/n' + text, reply_markup)

def coins(message):
    '''Це функція курса валют'''
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_idth=2)
    itembtn1 - types.KeyboardButton('USD')
    itembtn2 - types.KeyboardButton('EUR')
    itembtn3 = types.KeyboardButton('RUR')
    itembtn4 - types.KeyboardButton('BTC')
    markup.add(itenbtn1, itembtn2, itenbtn3, iterbtn4)
msg = bot.send_message(message.chat.id, "Визначити готівковий курс ПриватБанка", reply_markup = markup)
bot.register_next_step_handler(msg, process_coin_step)
def process_coin_step(message):
    try: markup = types.ReplykeyboardRemove(selective = False)
    for coin in response:
        if (message.text ==  coin['ccy']):
                bot.send_message(message.chat.id, printCoin(coin['buy' ], coin['sale']),
        reply_markup=markup, parse_mode="Markdown")
except Exception as e:
bot.reply_to(message, 'ooops!')
def printCoin(buy, sale):
    return "Курс покупки:" + str(buy) + "/n Курс продажу:" + str(sale)