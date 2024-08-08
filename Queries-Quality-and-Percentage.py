import pandas as pd
data = [['Dog', 'Golden Retriever', 1, 5], ['Dog', 'German Shepherd', 2, 5], ['Dog', 'Mule', 200, 1], ['Cat', 'Shirazi', 5, 2], ['Cat', 'Siamese', 3, 3], ['Cat', 'Sphynx', 7, 4]]
queries = pd.DataFrame(data, columns=['query_name', 'result', 'position', 'rating']).astype({'query_name':'object', 'result':'object', 'position':'Int64', 'rating':'Int64'})
queries['quality'] = queries['rating']/queries['position'] 
queries['poor_query_percentage'] = (queries['rating']<3)*100
print((queries.groupby('query_name')[['quality','poor_query_percentage']].mean()).round({'quality':2,'poor_query_percentage':2}).reset_index())