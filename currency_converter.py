import requests

def currency_converter(amount, from_currency, to_currency):
    api_key = '383b7d13d483ecaa9e1c6ca2'
    base_url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}'
    try:
        response = requests.get(base_url)
        if response.status_code == 200:
            data = response.json()
            if data['result'] == 'success':
                conversion_rate = data['conversion_rates'].get(to_currency)
                if conversion_rate is not None:
                    converted_amount = amount * conversion_rate
                    return converted_amount
        return None
    except requests.exceptions.RequestException:
        return None

amount = float(input("Enter the amount to convert: "))
from_currency = input("Enter the currency to convert from: ").upper()
to_currency = input("Enter the currency to convert to: ").upper()

converted_amount = currency_converter(amount, from_currency, to_currency)

if converted_amount is not None:
    print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}.")
else:
    print("Conversion failed. Please check your input.")
