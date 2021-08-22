from module import *
import investpy
import mplfinance as mpf
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

pais = 'brazil'
eft = ETF('bova11', pais)
acao = Acao('VALE3', pais)
data_inicial = '21/08/2016'
data_final = '21/08/2021'
acao1 = Acao('BBSE3', pais)

ref = acao.dados_historicos(data_inicial, data_final)

lista = [eft, acao]

# print('-----------')
#
# print('-----------')
print(ref)
# print('-----------')
#print(eft.beta(acao))
# print('-----------')
# print(eft.beta(acao))

