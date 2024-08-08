import pandas as pd
import numpy as np
data = [[1, '2019-02-17', '2019-02-28', 5], [1, '2019-03-01', '2019-03-22', 20], [2, '2019-02-01', '2019-02-20', 15], [2, '2019-02-21', '2019-03-31', 30],[3,'2019-02-21','2019-03-31',30]]
prices = pd.DataFrame(data, columns=['product_id', 'start_date', 'end_date', 'price']).astype({'product_id':'Int64', 'start_date':'datetime64[ns]', 'end_date':'datetime64[ns]', 'price':'Int64'})
data = [[1, '2019-02-25', 100], [1, '2019-03-01', 15], [2, '2019-02-10', 200], [2, '2019-03-22', 30]]
units_sold = pd.DataFrame(data, columns=['product_id', 'purchase_date', 'units']).astype({'product_id':'Int64', 'purchase_date':'datetime64[ns]', 'units':'Int64'})
df = units_sold.merge(prices, on = 'product_id', how = 'right')
df = (df[(df['purchase_date'].between(df['start_date'], df['end_date'])) | (df['purchase_date'].isna())])
df.fillna(value=0,inplace=True)
df['Total_price'] = df['units']*df['price']
df = df.groupby('product_id').agg({'Total_price':'sum','units':'sum'}).reset_index()
df['average_price'] = df['Total_price'] / df['units']
df['average_price'] = np.where(df['units'] != 0, df['Total_price'] / df['units'], 0)
df = df[['product_id','average_price']].round(2)
print(df)