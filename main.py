from module import Acao, ETF
# from datetime import date, timedelta
import investpy

# data_inicial = '16/08/2021'
# data_final = '17/08/2021'
pais = 'brazil'
# stock = Acao('FBOK34', pais)

# print(stock.dados_historicos(data_inicial, data_final))

d = investpy.search_quotes(text='bova11', products=['etfs'],countries=['brazil'], n_results=1)
print(d)
