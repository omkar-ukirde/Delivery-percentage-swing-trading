#Get 20 days data. Check for duplicate data.
#cat *.csv > alldata.csv
import pandas as pd
df = pd.read_csv('/Users/omkar/Downloads/Bhavcopy/alldata.csv')
max_deliv = df.loc[df.groupby('SYMBOL')[' DELIV_PER'].transform(max) == df[' DELIV_PER']]
max_deliv.to_csv('final.csv')
# open in excel
# Filter on Date for highest date
# Filter on series for EQ.
# copy this data to google sheets
# get marketcap and remove data having no market cap
# copy to excel and =close - open. Filter for positive values.  
