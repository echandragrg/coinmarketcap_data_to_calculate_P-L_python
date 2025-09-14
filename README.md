Crypto Portfolio P/L Calculator

This Python script fetches real-time cryptocurrency prices from the CoinMarketCap API and calculates the Profit/Loss (P/L) for your portfolio.

Features

Connects to the CoinMarketCap API to get the latest cryptocurrency data.

Supports multiple coins in your portfolio.

Calculates:

Total amount invested

Current portfolio value

Profit/Loss per coin

Total portfolio P/L

Requirements

Python 3.x

Libraries:

requests

json

Install dependencies using:

pip install requests

Setup

Get a free API key from CoinMarketCap
.

Replace the CMC_PRO_API_KEY in the script with your own key:

api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5&convert=USD&CMC_PRO_API_KEY=YOUR_API_KEY")


Update your portfolio inside the script:

coins = [
    {
        "symbol": "BTC",
        "amount_owned": 2,
        "price_per_coin": 100000
    },
    {
        "symbol": "ETH",
        "amount_owned": 10,
        "price_per_coin": 3000
    }
]

Usage

Run the script:

python portfolio_pl.py


Example output:

Bitcoin - BTC
Price - $64,321.50
Number of Coin: 2
Total Amount Paid: $200,000.00
Current Value: $128,643.00
P/L Per Coin: -$35,678.50
-------
Ethereum - ETH
Price - $3,412.25
Number of Coin: 10
Total Amount Paid: $30,000.00
Current Value: $34,122.50
P/L Per Coin: +$412.25
-------
Total P/L For Portfolio: -167.25
