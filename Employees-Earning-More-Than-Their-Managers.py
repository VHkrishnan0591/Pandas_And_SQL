import pandas as pd
data = [[1, 'Joe', 70000, 3], [2, 'Henry', 80000, 4], [3, 'Sam', 60000, None], [4, 'Max', 90000, None]]
employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'managerId']).astype({'id':'Int64', 'name':'object', 'salary':'Int64', 'managerId':'Int64'})
df = employee.merge(employee, left_on = 'id', right_on = 'managerId' , how = 'inner')
print(df[df['salary_x'] < df['salary_y']][['name_y']].rename(columns = {'name_y':'Employee'}))