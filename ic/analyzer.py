from .dictionary import Dictionary


def split_word(word: str) -> list:
    # 단어(word)를 가능한 모든 경웅의 수로 쪼개기
    # ex) f('민물고기') -> [('민','물고기'), ('민물','고기'), ('민물고','기')]
    if ' ' in word:
        # 문장일 때? -> 띄어쓰기 기준으로 생각
        word = word.split(' ')
        return [(' '.join(word[:i]), ' '.join(word[i:])) for i in range(1, len(word))]
    return [(word[:i], word[i:]) for i in range(1, len(word))]


def flatten(l: list) -> list:
    # flatten
    # ex) f([[1,2],3]) -> [1,2,3]
    r = []
    for i in l:
        if isinstance(i, list) or isinstance(i, tuple):
            r.extend(flatten(list(i)))
        else:
            r.append(i)
    return r


def filter_word(splited: list) -> list:
    # 사전에 등재돼 있지 않은 단어를 포함할 경우 -> 제거
    # ex) f([('뷁','체'), ('안녕','하세요')]) -> [('안녕','하세요')]
    r = []
    for i in splited:
        # i = ('안녕', '하세요')
        if sum([dic.find(word) for word in i]) == 2:
            # 둘 다 사전에 등재돼 있어야만
            r.append(i)
    return r


dic = Dictionary()
