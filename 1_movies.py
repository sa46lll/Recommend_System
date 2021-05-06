import pandas as pd

print(pd.__version__)

# index = movieId
# 데이터 불러오기, index = movieId
print(pd.read_csv('Z:\RecommendationSystem\data\ml_latest_small/movies.csv', index_col='movieId'))

movies = pd.read_csv('Z:\RecommendationSystem\data\ml_latest_small/movies.csv', index_col='movieId')

# 데이터의 개수, col 개수
print(movies.shape)

# 상위 데이터 추출
print(movies.head()) # 상위 5개
print(movies.head(10))
print(movies.tail()) # 하위 5개
print(movies.sample()) # 랜덤 5개

print(movies.columns)

# 데이터 저장
# movies.to_csv('Z:\RecommendationSystem\data\ml_latest_small/save_testData.csv')
