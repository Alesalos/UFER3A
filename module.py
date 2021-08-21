import investpy, json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mpdates
from datetime import date, timedelta, datetime
from scipy import stats
import numpy as np

class Processaento:

	def _data_hoje():
		_data_hoje = date.today()
		return _data_hoje.strftime("%d/%m/%Y")

	def _data_5_meses():
		data_hj = date.today()
		_data_5_meses = data_hj - timedelta(days = 153)
		return _data_5_meses.strftime("%d/%m/%Y")

		# Retornar o Beta Atualizado de um espaço de tempo definido, padrão 5 meses
	def beta(self, referencia, data_inicial = _data_5_meses(), data_final = _data_hoje(), interval = 'Monthly'):
		dados_acao = self.dados_historicos(data_inicial = data_inicial, data_final = data_final)
		dados_referencia = referencia.dados_historicos(data_inicial = data_inicial, data_final = data_final)
		dados_acao = dados_acao['Close'].pct_change().dropna().values
		dados_referencia = dados_referencia['Close'].pct_change().dropna().values
		df = pd.DataFrame()
		df['dados_acao'] = dados_acao
		df['dados_referencia'] = dados_referencia
		beta, alpha, r, p, std_err = stats.linregress(df['dados_referencia'], df['dados_acao'])
		return 'beta: {}'.format(beta)

	def bollinger_band(self, data_inicial, data_final, janela = 20 ,sigma = 2):
		dados_acao = self.dados_historicos(data_inicial = data_inicial, data_final = data_final)
		data_inicial = datetime.strptime(data_inicial, "%d/%m/%Y")
		data_final = datetime.strptime(data_final, "%d/%m/%Y")
		dias_passados = data_final - data_inicial
		dias_passados = dias_passados.days
		bollinger_df = pd.DataFrame()		
		bollinger_df['Preço Fehamento'] = dados_acao['Close']
		bollinger_df['Média movel'] = dados_acao['Close'].rolling(janela).mean()
		bollinger_df['Desvio padrão'] = dados_acao['Close'].rolling(janela).std()
		bollinger_df['Banda superior'] = bollinger_df['Média movel'] + (bollinger_df['Desvio padrão'] * sigma)
		bollinger_df['Banda inferior'] = bollinger_df['Média movel'] - (bollinger_df['Desvio padrão'] * sigma)
		#bollinger_df = bollinger_df.dropna()
		del bollinger_df['Desvio padrão']
		bollinger_df.index = pd.to_datetime(bollinger_df.index)
		bollinger_df['Preço Fehamento'].plot(label = 'Preço Fehamento')
		bollinger_df['Média movel'].plot(label = 'Média movel')
		bollinger_df['Banda inferior'].plot(label = 'Banda inferior')
		bollinger_df['Banda superior'].plot(label = 'Banda superior')
		plt.title("Banda de Bollinger para {}".format(self.ticker))
		plt.grid()
		plt.show()
		return bollinger_df


class Acao(Processaento):

	def __init__(self, ticker, pais):
		self.ticker = ticker
		self.pais = pais

	# Criado como redundancia para funcionar como metodo do objeto Acao
	#dd/mm/yyyy # interval = 'Daily, Weekly or Monthly'
	
	def dados_historicos(self, data_inicial, data_final, interval = 'Daily'):
		print(f'carregando dados historicos do ticker: {self.ticker}')
		return investpy.stocks.get_stock_historical_data(self.ticker, self.pais ,data_inicial, data_final, as_json = False, order = 'ascending', interval=interval)
	



class ETF(Processaento):

	def __init__(self, ticker, pais):
		self.ticker = ticker
		self.pais = pais

	def _encontrar_etf(self):
		#print(f'Resultado de Busca por : {self.ticker}')
		dados_nome = investpy.search_quotes(text = self.ticker, products = ['etfs'], countries = [self.pais], n_results=1)
		dados_nome = json.loads(dados_nome.__str__())
		return dados_nome['name']

	def dados_historicos(self, data_inicial, data_final, interval = 'Daily'):
		print(f'carregando dados historicos do ETF: {self.ticker}')
		return investpy.etfs.get_etf_historical_data(self._encontrar_etf(), self.pais, data_inicial, data_final, 
										stock_exchange=None, as_json=False, order='descending', interval=interval)

class Indicadores:
	def __init__(self):
		pass

class Cripto:
	def __init__(self):
		pass





# ---- TODO ----  
# Confirmar se terá de funcionar sempre online( fazendo pedidos de api pelo investpy ou alphavantage )
# Offline ( fazendo copias diarias dos preços para manter uma data base de testes)