from gensim.models import Word2Vec

# 샘플 문장 데이터
sentences = [["I", "love", "deep", "learning"],
             ["I", "love", "NLP"],
             ["deep", "learning", "is", "fun"]]

# Word2Vec 모델 학습
model = Word2Vec(sentences, vector_size=10, window=2, min_count=1, workers=4)

# 단어 "love"와 가장 비슷한 단어들 찾기
similar_words = model.wv.most_similar("love", topn=3)

# 결과 출력
print(similar_words)


# 벡터의 의미:
# Word2Vec은 단어를 고정된 크기의 벡터로 매핑하는데, 이 경우 **vector_size=10**으로 설정되어 있어 각 단어는 10차원의 벡터로 표현됩니다.
# 각 숫자는 해당 차원의 값으로, 단어의 의미를 수학적으로 나타냅니다. 예를 들어:
# 벡터의 값이 양수이면 해당 차원에서 긍정적인 특성을, 음수이면 부정적인 특성을 나타낼 수 있습니다.
# 벡터 값들은 서로 비슷한 의미를 가지는 단어들끼리 비슷한 값들을 가지며, 비슷한 문맥에서 등장한 단어들은 벡터 공간에서 서로 가까운 위치에 있게 됩니다.