import pandas as pd
data = [[1, 'War', 'great 3D', 8.9], [2, 'Science', 'fiction', 8.5], [3, 'irish', 'boring', 6.2], [4, 'Ice song', 'Fantasy', 8.6], [5, 'House card', 'Interesting', 9.1]]
not_so_boring_movies = pd.DataFrame(data, columns=['id', 'movie', 'description', 'rating'])
df = not_so_boring_movies[(not_so_boring_movies['id'] %2 !=0) & (not_so_boring_movies['description'] != 'boring')].sort_values("rating",ascending = False)
print(df)