import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np
from scipy import stats
import datetime 

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Path e stocks a serem calculados
PATH = '/home/nero/Desktop/B3_API/csv_data/'
stock = 'FLRY3.SA.csv'
bovespa_usd = 'INDX.SAO.csv'

# Criação de Dataframes e manipulação inicial de dados
df = pd.DataFrame()
data_bovespa = pd.DataFrame()
data_stock = pd.DataFrame()
stock_data = pd.read_csv(PATH+stock)
bovespa_data = pd.read_csv(PATH+bovespa_usd)
date_end = bovespa_data['timestamp'][0]
date_start = '2016-06-28'
dates_index = pd.date_range(start = date_start, end =date_end, freq = 'M' )
print(dates_index)
# criando DataFrame menor para facilitar organização de dados
data_bovespa['timestamp'] = bovespa_data['timestamp']
data_bovespa['bov_preço'] = bovespa_data['adjusted_close']
data_stock['timestamp'] = stock_data['timestamp']
data_stock['stock_preço'] = stock_data['adjusted_close']
# junta os dataframes menores corrigindo as datas desalinhadas
data = pd.merge(data_bovespa, data_stock, on='timestamp', how='left').dropna()
data['timestamp'] = pd.to_datetime(data['timestamp'])
print(data.head(),data.tail())
# calcula a variancia proporcinal em porcentagem dos preços em fechamento e retira o valor NaN
df['stock_pct_change'] = data['stock_preço'].pct_change().dropna().values
df['bovespa_pct_change'] = data['bov_preço'].pct_change().dropna().values
#print(df.head(),df.tail())

# calcula de regressão linear usando o scipy Y = BX + A
beta, ALPHA, r, p, std_err = stats.linregress(df['bovespa_pct_change'],df['stock_pct_change'])
# calculo para o valor de X e Y
x = np.linspace(np.amin(df['bovespa_pct_change']), np.amax(df['bovespa_pct_change']))
y = beta * x + ALPHA
print(f'Beta = {beta}, Alpha = {ALPHA}')

plt.plot(df['bovespa_pct_change'],df['stock_pct_change'], 'b.', alpha = 0.2)
plt.plot(x, y, 'k')
plt.grid()
plt.title('stock_pct_change VS bovespa_pct_change')
plt.xlabel('bovespa_pct_change')
plt.ylabel('stock_pct_change')
plt.show()