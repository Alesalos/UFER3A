import investpy
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

stock = 'FLRY3'
country = 'brazil'
#x = investpy.stocks.get_stock_company_profile(stock, country=country, language='english')
#y = investpy.stocks.get_stock_dividends(stock, country)
z = investpy.stocks.get_stock_information(stock, country, as_json=True)
c = [q  for q in z.items()]

#{key:value for (key,value) in dictonary.items()}

w = {key:value for (key,value) in z.items() }

print(z.get('Beta'))