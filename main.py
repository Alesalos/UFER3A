from module import Ticker


data_inicial = '16/08/2021'
data_final = '17/08/2021'
pais = 'brazil'
stock = Ticker('FBOK34', pais)


hist = stock.dados_historicos(data_inicial,data_final, interval = 'Daily')

print(hist)