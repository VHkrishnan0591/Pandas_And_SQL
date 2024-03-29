import pandas as pd
data = [[1, 'A', 'm', 2500], [2, 'B', 'f', 1500], [3, 'C', 'm', 5500], [4, 'D', 'f', 500]]
salary = pd.DataFrame(data, columns=['id', 'name', 'sex', 'salary']).astype({'id':'Int64', 'name':'object', 'sex':'object', 'salary':'Int64'})
salary['sex'] = salary['sex'].replace(['f','m'],['m','f'])
print(salary)