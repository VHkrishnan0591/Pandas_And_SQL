import pandas as pd
data = [[1, 2, 3], [1, 2, 4], [1, 3, 3], [2, 1, 1], [2, 2, 1], [2, 3, 1], [2, 4, 1]]
teacher = pd.DataFrame(data, columns=['teacher_id', 'subject_id', 'dept_id']).astype({'teacher_id':'Int64', 'subject_id':'Int64', 'dept_id':'Int64'})

# This Coversts the series into a dataframe but the index is not a separate column in that dataframe still and index to the dataframe
# df = teacher.groupby('teacher_id')['subject_id'].nunique().to_frame(name='cnt')

# This Coversts the series into a dataframe but the index as a separate column in that dataframe 
df = teacher.groupby('teacher_id')['subject_id'].nunique().reset_index(name='cnt')
print(df)