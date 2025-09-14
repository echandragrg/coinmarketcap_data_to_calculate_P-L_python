import requests
import json

api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5&convert=USD&CMC_PRO_API_KEY=4dc0de7e-4fae-46fa-974c-97c6a77e3abd")

api = json.loads(api_request.content)

coins = [
    {
        "symbol":"BTC",
        "amount_owned":2,
        "price_per_coin":100000
    },
    {
        "symbol":"ETH",
        "amount_owned":10,
        "price_per_coin":3000
    }
]

total_pl = 0

for i in range(0, 5):
    for coin in coins:
        if api["data"][i]["symbol"] == coin["symbol"]:
            total_paid = coin["amount_owned"] * coin["price_per_coin"]
            current_value = coin["amount_owned"] * api["data"][i]["quote"]["USD"]["price"]
            pl_percoin = api["data"][i]["quote"]["USD"]["price"] - coin["price_per_coin"]
            total_pl_coin = pl_percoin * coin["amount_owned"]

            total_pl = total_pl + total_pl_coin

            print(api["data"][i]["name"] + " - " + api["data"][i]["symbol"])
            print("Price - ${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))
            print("Number of Coin:", coin["amount_owned"])
            print("Total Amount Paid:","${0:.2f}".format(total_paid))
            print("Current Value:","${0:.2f}".format(current_value))
            print("P\L Per Coint:","${0:.2f}".format(pl_percoin))
            print("-------")

print("Total P/L For Portfolio:", total_pl)
