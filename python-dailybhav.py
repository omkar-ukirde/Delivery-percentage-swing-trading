cat *.csv > alldata.csv
import pandas as pd
df = pd.read_csv('/Users/omkar/Downloads/Bhavcopy/alldata.csv')
max_delivery = df.loc[df.groupby('SYMBOL')[' DELIV_PER'].transform(max) == df[' DELIV_PER']]
max_high = df.loc[df.groupby('SYMBOL')[' HIGH_PRICE'].transform(max) == df[' HIGH_PRICE']]
combinedf = pd.concat([max_high,max_delivery])
combinedf.drop_duplicates()
combinedf.to_csv('final.csv')
