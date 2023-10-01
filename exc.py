import requests
from datetime import datetime


cur_date = datetime.now().strftime("%d.%m.%Y")
URL = f"https://api.privatbank.ua/p24api/exchange_rates?json&date={cur_date}"


cur_to_change = "CAD"
val_to_change = 4
out_cur = 'USD'


def currency_ex(from_cal, amount, to_val):
    response = requests.get(URL)
    data = response.json()

    first_rate = 0
    second_rate = 0

    for i in data['exchangeRate']:

        if i['currency'] == cur_to_change:
            first_rate = i['saleRateNB']
            #print(first_rate)
            # if to_val == "UAH":
            #     result = round(first_rate * amount, 2)
            #     print(f"It will be {result} in {to_val}")
            #     break
        elif i['currency'] == to_val:
            second_rate = i['saleRateNB']

    if first_rate != 0 and second_rate !=0:
        print(f'{amount} {cur_to_change} will equal: {round(amount * first_rate / second_rate, 2)} {to_val}')



currency_ex(cur_to_change, val_to_change, out_cur)