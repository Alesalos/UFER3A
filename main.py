from module import Acao, ETF
import investpy
import mplfinance as mpf
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

pais = 'United States'
eft = ETF('bova11', pais)
acao = Acao('TSLA', pais)
data_inicial = '01/01/2020'
data_final = '21/08/2021'

# print('-----------')
# print(acao.dados_historicos(data_inicial, data_final))
# print('-----------')
# print(eft.dados_historicos(data_inicial, data_final))
# print('-----------')
# print(acao.beta(eft))
# print('-----------')
# print(eft.beta(acao))

acao.bollinger_band(data_inicial,data_final, janela = 20 ,sigma = 2)
