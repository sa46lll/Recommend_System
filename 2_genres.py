import pandas as pd

movies = pd.read_csv('Z:\RecommendationSystem\data\ml_latest_small/movies.csv', index_col='movieId')

# genres 분석
print(movies['genres'])

sample_genre = movies['genres'][1]
sample_genre.split("|") #장르 쪼개기
# print(sample_genre)

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

#장르 데이터 숫자형으로 변환하기
message = 'Hello'
print('H' in message) #True
print('Adventure' in sample_genre) #True
print(movies['genres'].apply(lambda x: 'Adventure' in x))

# if Avdenture -> True else False
movies['Adventure'] = movies['genres'].apply(lambda x: 'Adventure' in x)
movies['Comedy'] = movies['genres'].apply(lambda x: 'Comedy' in x)

# 모든 영화에 대한 장르에 따른 0,1 변환 -> pandas 제공
print(movies['genres'].str.get_dummies(sep='|'))
genres_dummies = movies['genres'].str.get_dummies(sep='|')

# genres_dummies 저장 (pickle는 인덱스까지 저장하므로 유용함.)
# genres_dummies.to_pickle('Z:\RecommendationSystem\data\ml_latest_small/genres.p')

# 두 장르의 관계가 1에 가깝다는 것은 : 두 장르가 자주 같이 출현
# 두 장르의 관계가 -1에 가깝다는 것은 : 두 장르가 아주 드물게 출현, 겹치는 영역이 없음.
import seaborn as sns
import matplotlib.pyplot as plt # seaborn figure 크기 조절을 위함.

plt.figure(figsize=(30,15))
sns.heatmap(genres_dummies.corr(), annot=True) #seaborn의 heatmap 이용
plt.show()
