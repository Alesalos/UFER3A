import pandas as pd 
import matplotlib.pyplot as plt


#NUMERO DE DIAS A SER MEDIDO
dias = 200

#PATH para dados baixados pela api
PATH = '/home/nero/Desktop/B3_API/csv_data/'
File_name = 'FLRY3.SA.csv'

# lê os arquivos fornecidos
stock_data = pd.read_csv(PATH+File_name)
#print(stock_data.head())

#Main data frame for graph ploting
bollinger_df = pd.DataFrame()

#pega os dias dos preços
bollinger_df['Data'] = stock_data['timestamp'][:dias]

#separa os ultimos 20 dias do preço ajustado
bollinger_df['Price'] = stock_data['adjusted_close'][:dias]

#calcula a moving average para definir limites superiores e inferiores.
bollinger_df['Moving Average'] = bollinger_df['Price'].rolling(dias, min_periods=1).mean()

#calcula o desvio médio standard deviation
bollinger_df['Standard Deviation'] = bollinger_df['Price'].rolling(dias, min_periods=1).std()

# bandas inferior e superior
bollinger_df['Upper band'] = bollinger_df['Moving Average'] + (bollinger_df['Standard Deviation']*2)
bollinger_df['Lower Band'] = bollinger_df['Moving Average'] - (bollinger_df['Standard Deviation']*2)


#bollinger_df = bollinger_df.set_index('Data')
bollinger_df['Data'] = pd.to_datetime(bollinger_df['Data'])

# montagem do gráfico
print(bollinger_df.info())
print(bollinger_df)

x = bollinger_df['Data']
plt.plot(x, bollinger_df['Price'], label = 'Preço')
plt.plot(x, bollinger_df['Moving Average'], label = 'Moving Average')
plt.plot(x, bollinger_df['Upper band'], label = 'Upper band')
plt.plot(x, bollinger_df['Lower Band'], label = 'Lower Band')
plt.legend()
plt.title(f'{File_name} bollinger band')
plt.show()