
investment_in_bitcoin = 1.2
bitcoin_to_usd = 40000

# 1) write a function to calculate bitcoin to usd
def bitcoinToUSD(bitcoin_amount, bitcoin_value_usd):
  s = bitcoin_amount * bitcoin_value_usd
  return s
  
answer = bitcoinToUSD(1.2, 20000) 

# 2) use function to calculate if the investment is below $30,000
if answer < 30000:
  print("alert")
