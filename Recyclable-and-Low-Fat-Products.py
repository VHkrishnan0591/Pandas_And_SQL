import pandas as pd
data = [['0', 'Y', 'N'], ['1', 'Y', 'Y'], ['2', 'N', 'Y'], ['3', 'Y', 'Y'], ['4', 'N', 'N']]
products = pd.DataFrame(data, columns=['product_id', 'low_fats', 'recyclable']).astype({'product_id':'int64', 'low_fats':'category', 'recyclable':'category'})
df = products[(products['low_fats'] == 'Y' )& (products['recyclable'] == 'Y')][['product_id']]
print(df)
# Learning:
# # The previus code : products[products['low_fats'] == 'Y' & products['recyclable'] == 'Y'][['product_id']]
# The error you're getting is because you're trying to use the bitwise AND operator (&) on a string ('Y') and a Categorical type ('low_fats'). 
# Pandas categoricals are used to represent data that has limited categories, and they don't support bitwise operators