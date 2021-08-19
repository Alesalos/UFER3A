# teste de beta 01 - https://python.plainenglish.io/measure-stock-volatility-using-betas-in-python-d6411612e7bd

x = np.array(df['stock_pct_change']).reshape((-1,1))
y = np.array(df['bovespa_pct_change'])
model = LinearRegression().fit(x, y)
print('Beta test 01 ')
print('Beta: ',model.coef_)

plt.scatter(y, x, color ='g')
plt.xlabel('Bovespa')
plt.ylabel('Stock')
plt.title('Stock VS Bovespa')
plt.plot(x, model.predict(x), color='k')
plt.show()

# teste de beta 02

# fórmula do Beta = Cov(Rs,Rm) / Var(Rm)

# calculando a covariancia do Rs retorno do stock e Rm retorno do mercado

Rs = df['stock_pct_change']
Rm = df['bovespa_pct_change']
cov = np.cov(Rs,Rm)
var = np.var(Rm)
Beta = cov/var
print(f'Beta 02 = {Beta}')

# teste Beta 03 - https://www.codingfinance.com/post/2018-04-25-portfolio-beta-py/
(BEET,APLHA) = stats.linregress(Rm,Rs)[0:2]
print('Beta03 = ',round(BEET,4))
print('APLHA = ',round(APLHA,5))
sns.regplot(x = Rm,y = Rs)
plt.xlabel('Bovespa return')
plt.ylabel('Stock return')
plt.title('Stock VS Bovespa')
plt.show()

# Beta test 04 - https://www.investopedia.com/ask/answers/070615/what-formula-calculating-beta.asp