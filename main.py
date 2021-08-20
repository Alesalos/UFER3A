from module import Acao, ETF
import investpy


pais = 'brazil'
eft = ETF('bova11', pais)
acao = Acao('VALE3', pais)
data_inicial = '01/08/2020'
data_final = '30/08/2021'

# print('-----------')
# print(acao.dados_historicos(data_inicial, data_final))
# print('-----------')
# print(eft.dados_historicos(data_inicial, data_final))
# print('-----------')
# print(acao.beta(eft))
# print('-----------')
# print(eft.beta(acao))

print(eft.bollinger_band(data_inicial,data_final))