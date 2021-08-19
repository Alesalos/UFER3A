import pandas as pd
import matplotlib.pyplot as plt
import investpy
from datetime import date, timedelta
import json
import inspect


class Acao:

	def __init__(self, ticker, pais):
		self.ticker = ticker
		self.pais = pais

	def _data_hoje():
		_data_hoje = date.today()
		return _data_hoje.strftime("%d/%m/%Y")

	def _data_5_meses():
		data_hj = date.today()
		_data_5_meses = data_hj - timedelta(days = 153)
		return _data_5_meses.strftime("%d/%m/%Y")

	# Criado como redundancia para funcionar como metodo do objeto Acao
	#dd/mm/yyyy # interval = 'Daily, Weekly or Monthly'
	
	def dados_historicos(self, data_inicial, data_final, interval = 'Daily'):
		print(f'dados do ticker: {self.ticker}')
		return investpy.stocks.get_stock_historical_data(self.ticker, self.pais ,data_inicial, data_final, as_json = False, order = 'descending', interval=interval)
	
	# Retornar o Beta Atualizado de um espaço de tempo definido, padrão 5 meses
	def beta(self, referencia,data_inicial = _data_5_meses(), data_final = _data_hoje(), interval = 'Monthly'):
		dados_acao = self.dados_historicos(data_inicial = data_inicial, data_final = data_final)


	def bollinger_band(self):
		pass


class ETF:

	def __init__(self, ticker, pais):
		self.ticker = ticker
		self.pais = pais

	def _encontrar_etf(self):
		#print(f'Resultado de Busca por : {self.ticker}')
		dados_nome = investpy.search_quotes(text = self.ticker, products = ['etfs'], countries = [self.pais], n_results=1)
		dados_nome = json.loads(dados_nome.__str__())
		return dados_nome['name']

	def dados_historicos(self, data_inicial, data_final, interval = 'Daily'):
		print(f'dados historicos do ETF: {self.ticker}')

		return investpy.etfs.get_etf_historical_data(self._encontrar_etf(), self.pais, data_inicial, data_final, stock_exchange=None, as_json=False, order='descending', interval=interval)


class Indicadores:
	def __init__(self):
		pass

class Cripto:
	def __init__(self):
		pass




pais = 'brazil'
# stock1 = ETF('Ishares Ibovespa', pais)
# stock2 = Acao('FLRY3', pais)
# print(stock1.dados_historicos( Acao._data_5_meses(), Acao._data_hoje()))
# print(stock2.beta(stock1))

a = ETF('bova11', pais)
print('-----------')
print(a.dados_historicos('10/08/2021','18/08/2021'))
print('-----------')

# ---- TODO ----  
# Confirmar se terá de funcionar sempre online( fazendo pedidos de api pelo investpy ou alphavantage )
# Offline ( fazendo copias diarias dos preços para manter uma data base de testes)