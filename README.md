## 직접 구성 성분 분석기 (Immediate constituent analyzer)


> 벽돌집 → **벽돌** + **집**<br>인생은 짧지만 예술은 길다 → **인생은 짧지만** + **예술은 길다**


`직접 구성 성분 분석`은 하나의 말을 두 부분으로 쪼개는 분석 방법입니다.

본 레포지토리는 [tf-hub](https://www.tensorflow.org/hub?hl=ko)를 활용하여 `직접 구성 성분 분석`을 구현한 레포지토리입니다.


## 사용법

시작하기 전 requirements.txt의 패키지를 모두 설치해 주세요.

```python3
from ic import IC
ic = IC()

ic('벽돌집')  # 벽돌 + 집
ic('안녕하세요 저는 조준희입니다.')  # 안녕하세요 + 저는 조준희입니다.
ic('집')  # 집
```

## 이런 곳에 사용될 수 있습니다

### 겹문장 분석

  규칙 기반에 비해 훨씬 효율적입니다.

  ```python3
  ic('나는 밥을 먹으러 식당에 간다')  # 나는 밥을 먹으러 + 식당에 간다
  ```
 
### 단어 분석

  [konlpy](https://konlpy.org/en/latest/)같은 일반적인 품사 tagger보다 세부적인 분석이 가능해집니다.
  ```python3
  # pos tagger
  from konlpy.tag import Kkma
  Kkma().tag('살얼음')  # 살얼음
  
  # IC 분섟
  ic('살얼음')  # 살 + 얼음
  ```

## 원리

분석 과정은 다음과 같습니다. '민물고기'라는 단어를 예로 들어 설명하겠습니다.

1. 모든 경우로 단어 분리하기
    > 민+물고기, 민물+고기, 민물고+기
  
2. 사전에 등재돼 있는 단어만 남기기
    > 민+물고기, 민물+고기
  
3. 원래 단어와 의미 비교 ([Universial Sentence Encoder](https://tfhub.dev/google/universal-sentence-encoder-multilingual/3)활용)
    > 민+물고기 (0.63), 민물+고기 (0.78)
  
4. 의미가 가장 비슷한 구조 채택
    > 민물고기 = 민물+고기
    
## Reference

[국립국어원 표준국어대사전 표제어 DB](https://github.com/korean-word-game/db)를 사용했습니다.
    
## 주의
시험 공부 중 아이디어 떠올라서 2시간 만에 만든 거라 성능은 보장할 수 없습니다 😂😂
