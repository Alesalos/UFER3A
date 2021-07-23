import requests

url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/AAPL/financial-data"

headers = {
    'x-rapidapi-key': "696f5e2327msh80afe13652c9f69p167d48jsn1c394d9d2153",
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)