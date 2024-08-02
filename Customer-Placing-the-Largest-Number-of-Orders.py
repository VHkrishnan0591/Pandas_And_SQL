import pandas as pd
data = [[1, 1], [2, 2], [3, 3], [4, 3]]
orders = pd.DataFrame(data, columns=['order_number', 'customer_number']).astype({'order_number':'Int64', 'customer_number':'Int64'})
df = orders.groupby(by = 'customer_number').count().reset_index().sort_values(by = "order_number", ascending = False).head(1)[['customer_number']]
print(df)