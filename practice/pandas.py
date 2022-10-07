import pandas as pd
import numpy as np

df = pd.read_csv('아파트(매매)__실거래가_20221006165646.csv', encoding = 'cp949', header = 15)
print(df.shape)
print(df)
df=df.rename(columns={'분양가격(㎡)':'분양가'})
print("*******************************")
print(df.describe())
