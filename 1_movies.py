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

# 개봉연도 데이터 정제하기 (데이터 전처리, PreProcessing)
print(movies['title'].str.extract('(\(\d\d\d\d\))')) #연도 숫자4개 추출하기

movies['year'] = movies['title'].str.extract('(\(\d\d\d\d\))')

# 괄호를 제외한 날짜만 추출
movies['year'] = movies['year'].str.extract('(\d\d\d\d)')
print(movies)

# 중복된 값들 제외
print(movies['year'].unique())

# NAN 결측값 핸들링하기
print(movies[movies['year'].isnull()]) # 결측값 추출
movies['year'] = movies['year'].fillna('2050') # Nan을 2050으로 대체
print(movies['year'].unique())

# 데이터에 가장 많이 출현하는 개봉연도를 찾아주세요.
# print(movies['year'].value_counts()) # 데이터숫자의 내림차순으로 연도가 정리
import seaborn as sns
import matplotlib.pyplot as plt # seaborn figure 크기 조절을 위함.
plt.figure(figsize=(30, 5))
sns.countplot(data=movies, x='year')
plt.show()
