import pandas as pd
import itertools
data = [[1, 'Alice'], [2, 'Bob'], [13, 'John'], [6, 'Alex']]
students = pd.DataFrame(data, columns=['student_id', 'student_name']).astype({'student_id':'Int64', 'student_name':'object'})
data = [['Math'], ['Physics'], ['Programming']]
subjects = pd.DataFrame(data, columns=['subject_name']).astype({'subject_name':'object'})
data = [[1, 'Math'], [1, 'Physics'], [1, 'Programming'], [2, 'Programming'], [1, 'Physics'], [1, 'Math'], [13, 'Math'], [13, 'Programming'], [13, 'Physics'], [2, 'Math'], [1, 'Math']]
examinations = pd.DataFrame(data, columns=['student_id', 'subject_name']).astype({'student_id':'Int64', 'subject_name':'object'})
examinations['attended_exams']= examinations.groupby(['student_id', 'subject_name'])[['student_id']].transform('count')
df = students.assign(key=1).merge(subjects.assign(key=1), on='key').drop('key', axis=1)
# Create a list of tuples containing combinations of student_id and subject_name
# combinations = list(itertools.product(students['student_id'], subjects['subject_name']))
# Create a new DataFrame from the combinations
# result = pd.DataFrame(combinations, columns=['student_id', 'subject_name'])
df = (df.merge(examinations, on=['student_id', 'subject_name'], how = 'left').drop_duplicates().sort_values(['student_id', 'subject_name']))
df['attended_exams'].fillna(0, inplace=True)
print(df)