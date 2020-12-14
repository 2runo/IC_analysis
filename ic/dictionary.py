class Dictionary:
    def __init__(self, path: str = "./ic/assets/"):
        self.affix = []
        self.nouns = []
        self.load_dict(path)

    def load_dict(self, path: str) -> None:
        # 사전 불러오기
        if path[-1] != '/':
            path += '/'

        fn = path + 'affix.txt'
        with open(fn, 'r', encoding='utf8') as f:
            data = f.read()
        self.affix: list = list(set(data.split('\n')))

        fn = path + 'nouns.txt'
        with open(fn, 'r', encoding='utf8') as f:
            data = f.read()
        self.nouns: list = list(set(data.split('\n')))

    def find(self, word: str, affix: bool = True) -> bool:
        # 해당 단어가 사전에 있는가?
        # affix: 합성어 검사하나?
        for w in self.nouns:  # 일반 명사
            if w == word:
                return True
        if affix:
            for a in self.affix:  # 합성어
                if word.endswith(a):
                    if self.find(word[:-len(a)], affix=False):
                        return True
        return False
