#-*- coding: utf-8 -*-

from PyKomoran import *
from .stopword import StopWord


# 자막파일을 입력받아 수어에 사용되는 형태소를 재배치하는 함수를 가진 객체
class NLP:
    def __init__(self):
        self.komoran = Komoran(DEFAULT_MODEL['FULL'])
        self.komoran.set_user_dic("C:/Users/tpqls/OneDrive/바탕 화면/2019-cap1-2019_7-master/src/NLP/txt/dic.user")
        self.pr = StopWord()
        pass

    def splitLine(self, line):
        for i in range(len(line)):
            s = str(line[i])
            s = s.split('/')
            line[i] = s
        return line

    # 수어에 사용되는 형태소를 재배치하는 함수
    def relocateMorpheme(self, subtitle_path):
        result=[]
        line = self.komoran.get_list(subtitle_path)
        line = self.splitLine(line)    # ex) [['식사', 'NNG'],~~~]
        print(line)
        for w, m in line:
            r, word, morph = self.pr.process_morph(m, w)
            if r == 1:
                if (word == 'ㅂ니까') or (word == '하다') or (word == '끝'):
                    if len(result) == 0:
                        result.append([word,morph])
                    elif result[len(result) - 1][0] != word:
                        result.append([word,morph])
                else:
                    result.append([word,morph])
         

        return result