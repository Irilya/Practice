import telebot
from config import keys ,TOKEN
from extensions import ConvertionException, ValuteConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу, введите команду в следующем формате:\n<имя валюты> \
<в какую валюту перевести> \
<количество переводимой валюты>\n \
Чтобы узнать список доступных валют, воспользуйтесь коммандой /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Список доступных валют:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def get_price(message: telebot.types.Message):
    try: 
        values = message.text.split(' ')
        
        if len(values) != 3:
            raise ConvertionException('Неверное число параметров или лишние пробелы.')

        quote, base, amount = values  
        total_valut = ValuteConverter.get_price(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_valut}'
        bot.send_message(message.chat.id, text)


bot.polling()


