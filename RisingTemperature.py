import pandas as pd
data = [[1, '2015-01-01', 10], [2, '2015-01-02', 25], [3, '2015-01-03', 20], [4, '2015-01-04', 30]]
weather = pd.DataFrame(data, columns=['id', 'recordDate', 'temperature']).astype({'id':'Int64', 'recordDate':'datetime64[ns]', 'temperature':'Int64'})
weather.sort_values('recordDate', inplace=True)
print(weather[(weather.temperature.diff() > 0) & (weather.recordDate.diff().dt.days == 1)][['id']])