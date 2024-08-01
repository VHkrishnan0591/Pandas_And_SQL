import pandas as pd
data = [[1, 'Joe'], [2, 'Henry'], [3, 'Sam'], [4, 'Max']]
customers = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})
data = [[1, 3], [2, 1]]
orders = pd.DataFrame(data, columns=['id', 'customerId']).astype({'id':'Int64', 'customerId':'Int64'})
df =  pd.merge(customers,orders, left_on = 'id', right_on = 'customerId' , how = 'left').rename(columns = {'name':'Customers'})
print(df[df['id_y'].isna()][['Customers']])