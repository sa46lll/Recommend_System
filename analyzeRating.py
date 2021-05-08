# 기초통계
import pandas as pd

ratings = pd.read_csv('Z:\RecommendationSystem\data\ml_latest_small/ratings.csv')

print(ratings.sample())
print(ratings.shape) # data, col 개수
print(len(ratings['userId'].unique())) # 610명의 유저 데이터
print(len(ratings['movieId'].unique())) # 9724개의 영화 데이터

print(ratings['rating'].describe()) # max, min 등 판다스 제공
print(ratings['rating'].hist()) #pandas에서 제공하는 시각화


# 사람들은 평균적으로 몇 개의 영화에 대해서 rating을 남겼는가?
users = ratings.groupby('userId')['movieId'].count() # user별 movie 개수
print(users[:5])

print(users.describe())

# power law distribution, 멱함수 분포
import seaborn as sns
import matplotlib.pyplot as plt # seaborn figure 크기 조절을 위함.

sns.displot(users.values) #어떤 사람이 몇개의 영화를 봤는지

# 사람들이 많이 보는 영화는?
films = ratings.groupby('movieId')['userId'].count()
print(films[:5])
print(films.describe())
sns.displot(films.values)
plt.show()
