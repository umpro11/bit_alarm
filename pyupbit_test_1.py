import pyupbit

#print(pyupbit.get_ohlcv(ticker="KRW-BTC"))  #get_ohlcv(ticker='KRW-BTC', interval='day', count=200, to=None, period=0.1) -> Union[DataFrame, None]

access = "PqQx5Z8ZqFYTTQu70QCtWiX9H96yfyTEb9IOZxgv" # access key 직접 입력 
secret = "dcD7cC0l7xHhAUQKzweOAxKBB9f6KcSLUUQeysmA" # secret key 직접 입력 

upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balances())
