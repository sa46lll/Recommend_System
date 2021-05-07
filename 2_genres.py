import pandas as pd

movies = pd.read_csv('Z:\RecommendationSystem\data\ml_latest_small/movies.csv', index_col='movieId')

# genres 분석
print(movies['genres'])

sample_genre = movies['genres'][1]
sample_genre.split("|") #장르 쪼개기

# 장르 모두 split 적용
genres_list = list(movies['genres'].apply(lambda x:x.split("|")))
print(genres_list[:3]) #3개 까지 출력

# 장르 개수 확인(리스트를 모두 몰아 넣기)
flat_list = []
for sublist in genres_list:
    for item in sublist:
        flat_list.append(item)
genres_unique = list(set(flat_list)) #중복값 삭제
print(len(genres_unique)-1) # No genre_list 제외.
