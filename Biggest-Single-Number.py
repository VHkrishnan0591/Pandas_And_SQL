import pandas as pd
data = [[8], [8], [3], [3], [1], [3], [5], [5]]
my_numbers = pd.DataFrame(data, columns=['num']).astype({'num':'Int64'})
print(my_numbers.drop_duplicates(keep=False).max().to_frame(name='num'))
