import yfinance as yf

msft = yf.Ticker("PETR4.SA")

#for item in msft.info:
#    print('{0} : {1}'.format(item,msft.info[item]))

print('====================')
#print(msft.splits)
print(msft.history(period="1d"))
print((msft.history(period="1d")).iat[0,0])
print((msft.history(period="1d")).iat[0,1])
print((msft.history(period="1d")).iat[0,2])
print((msft.history(period="1d")).iat[0,3])
print((msft.history(period="1d")).iat[0,4])
print((msft.history(period="1d")).iat[0,5])
print((msft.history(period="1d")).iat[0,6])
print((msft.history(period="1d")).head(1))
print('====================')
print(str((msft.history(period="1d"))))
