import pandas as pd
data = [[13, 15, 30], [10, 20, 15]]
triangle = pd.DataFrame(data, columns=['x', 'y', 'z']).astype({'x':'Int64', 'y':'Int64', 'z':'Int64'})
def triangle_inequality(df):
    if((abs(df['x']+df['y']) > abs(df['z'])) & (abs(df['x']+df['z']) > abs(df['y'])) & (abs(df['y']+df['z']) > abs(df['x'])) ):
        return 'Yes'
    else: return 'No'
triangle['triangle'] = triangle.apply(triangle_inequality, axis = 1)
print(triangle)