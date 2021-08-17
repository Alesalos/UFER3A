import pandas as pd
import matplotlib.pyplot as plt
import investpy


class Ticker:

	def __init__(self, ticker, pais):
		self.ticker = ticker
		self.pais = pais
	
	# Retornar o Beta Atualizado de um espaço de tempo definido, padrão 5 meses
	def beta(self):
		pass
	

	def bollinger_band(self):
		pass

	# Criado como redundancia para funcionar como metodo do objeto Ticker
	#dd/mm/yyyy # interval = 'Daily, Weekly or Monthly'
	def dados_historicos(self, data_inicial, data_final, interval = 'Monthly'):
		return investpy.stocks.get_stock_historical_data(self.ticker, self.pais ,data_inicial, data_final, as_json = False, order = 'descending', interval=interval)





# ---- TODO ----  
# Confirmar se terá de funcionar sempre online( fazendo pedidos de api pelo investpy ou alphavantage )
# Offline ( fazendo copias diarias dos preços para manter uma data base de testes)