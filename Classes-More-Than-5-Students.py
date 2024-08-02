import pandas as pd
data = [['A', 'Math'], ['B', 'English'], ['C', 'Math'], ['D', 'Biology'], ['E', 'Math'], ['F', 'Computer'], ['G', 'Math'], ['H', 'Math'], ['I', 'Math']]
courses = pd.DataFrame(data, columns=['student', 'class']).astype({'student':'object', 'class':'object'})
df = courses.groupby('class').count().reset_index().rename(columns = {'student':'Count', 'class':'Class'})
print(df[df['Count']>=5][['Class']])