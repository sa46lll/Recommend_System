# 기초통계
import pandas as pd

ratings = pd.read_csv('Z:\RecommendationSystem\data\ml_latest_small/ratings.csv')

print(ratings.sample())
print(ratings.shape) # data, col 개수
print(len(ratings['userId'].unique())) # 610명의 유저 데이터
print(len(ratings['movieId'].unique())) # 9724개의 영화 데이터

print(ratings['rating'].describe()) # max, min 등 판다스 제공
print(ratings['rating'].hist()) #pandas에서 제공하는 시각화
