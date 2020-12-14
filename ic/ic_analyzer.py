import tensorflow_hub as hub
import tensorflow_text  # 임포트하지 않으면 오류 발생
import numpy as np
from .utils.sim import cos_sim
from .analyzer import split_word, flatten, filter_word


class IC:
    def __init__(self):
        self.model = self.load_model()
        self.criterion = cos_sim  # 유사도 판단 함수

    @staticmethod
    def load_model():
        return hub.load("https://tfhub.dev/google/universal-sentence-encoder-multilingual/3")

    def compare(self, org: str, words: list) -> list:
        # 원래 단어(org)를 words와 비교하여 각각의 유사도를 구하고 두 개씩 묶어서 평균 반환
        # ex) f('민물고기', ['민', '물고기', '민물', '고기']) -> [0.698, 0.701]
        embed = self.model([org] + words)  # 임베딩
        org_v, words_v = embed[0], embed[1:]

        # 유사도 구하기
        r = []
        for idx, v in enumerate(words_v):
            r.append(self.criterion(org_v, v))
        r = np.average(np.reshape(r, (-1, 2)), axis=1)  # 평균 유사도
        return r

    def analyze(self, word: str) -> tuple:
        # word : 직접 구성 성분 분석 대상
        # ex) f('민물고기') -> ('민물', '고기')
        splited = split_word(word)  # 가능한 구성성분 조합 모두 추출 ex) 민+물고기, 민물+고기, 민물고+기
        if not ' ' in word:
            splited = filter_word(splited)  # 사전에 등록되지 않은 구성성분? -> 거르기
        if len(splited) == 0:
            # 비교 대상이 없으면?
            return (word,)
        if len(splited) == 1:
            # 비교 대상이 하나밖에 없으면?
            return splited[0]

        # 유사도 비교
        sim = self.compare(word, flatten(splited))
        return splited[np.argmax(sim)]

    def __call__(self, word: str) -> tuple:
        return self.analyze(word)
