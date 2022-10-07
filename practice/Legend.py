import pandas as pd
import numpy as np

df = pd.read_csv('아파트(매매)__실거래가_20221006165646.csv', encoding = 'cp949', header = 15)
print(df.shape)
#print(df)
df=df.rename(columns={'분양가격(㎡)':'분양가'})
print("*******************************")
print(df.describe())
print(df.sort_index(axis=0, ascending=True)[:5])
print(df[df['건축년도'] == 2006][:5])
print("*******************************")
print(df[df['전용면적(㎡)'] >= 20000][:5])
