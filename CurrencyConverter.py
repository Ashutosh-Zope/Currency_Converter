import requests

api_key = 'VADGKWJV3ARNVSKK'

from_currency = "USD"
to_currency = "INR"

amount = input('Enter the amount: ')
print()

baseurl = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE'
main_url = baseurl + '&from_currency='+from_currency+ '&to_currency='+to_currency+'&apikey='+api_key

response = requests.get(main_url)
result = response.json()
key = result['Realtime Currency Exchange Rate']
price = float(key['5. Exchange Rate'])

print("Realtime exchange rate")
print(f'1 {from_currency} : {price} {to_currency}')

print()

print("Converted amount")
print(f'{amount} {from_currency} : {price * int(amount)} {to_currency}')



