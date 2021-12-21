import requests
import json
from config import keys

class ConvertionException(Exception):
    pass


class ValuteConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):

    
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Неверно указано количество валюты {amount}')


        r = requests.get(f'https://free.currconv.com/api/v7/convert?q={quote_ticker}_{base_ticker}&compact=ultra&apiKey=a7f29e076bb4816202bd')
        total_base = json.loads(r.content)[f'{quote_ticker}_{base_ticker}']
        total_valut = float(total_base) * float(amount)
        return total_valut

