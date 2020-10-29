# constant

class Morph:
    MORPH = {   # 명사
                'NNG': '명사', 'NNP': '명사', 'NNB': '명사','NF': '명사', 'NP': '명사',
                # 용언
                'VV': '용언', 'VA': '용언', 'VX': '용언', 'VCP': '용언','VCN': '용언', 'NV': '용언', 'XSV': '용언',
                # 관형사
                'MM': '관형사',
                # 부사
                'MAG': '부사', 'MAJ': '부사',
                # 감탄사
                'IC': '감탄사',
                # 조사
                'JKS': '조사','JKC': '조사', 'JKG': '조사', 'JKO': '조사', 'JKB': '조사', 'JKV': '조사',
                'JKQ': '조사', 'JX': '조사', 'JC': '조사',
                # 어미
                'EP': '어미','EF': '어미','EC': '어미','ETN': '어미','ETM': '어미',
                # 접사
                'XPN': '접사','XSN': '접사','XSA': '접사', 'XR': '접사',
                # 부호
                'SF': '기호','SP': '기호','SS': '기호','SE': '기호','SO': '기호','SW': '기호',
                # 숫자, 수사
                'SN': '숫자', 'NR': '수사',
                # 영어
                'SL': '영어',
                # 한자 제외
                'SH': '없음',
                # 분석 불능 범주 제외
                'NA': '없음'
    }

    # 사용하는 관형사
    USE_DETER = ['저', '맨', '별', '무슨', '헌', '온', '온갖', '그', '동', '오랜', '모든', '그런', '양', '딴', '각', '어떤', '이런',
                 '몹쓸', '약', '옛', '어느', '한', '이러한']

    # 사용하는 조사
    USE_POST = ['랑', '에서', '서', '더러', '보다', '에게', '의', '로', '이라고', '에', '처럼', '께', '으로', '한테', '라고',  '게', '로서', # 격조사
                 '로써', '으로서', '으로써', '만치', '만큼', '보고', '보다', '서부터', '에서부터', '시여', '이시여', '아',# 격조사
                '이나', '든지', '부터', '도', '커녕', '마다', '밖에', '뿐', '만', '까지', '라도', '이라도', '라든지', '거나', '나', '나마', # 보조사
                '이나마', '는', '다가', '대로', '든가', '들', '따라', '라야', '란', '이란','로부터', '마는', '마저', '밖에', '부터', '뿐', # 보조사
                '야말로', '이야말로', '에는', '에다', '에다가', '은',  '이라야', '이야', '조차',# 보조사
                '과', '와', '이랑', '고', '이고', '며', '이며',# 접속조사
                '이니까', '이다', '야'  # 서술격 조사
                ]

    # 사용하는 어미
    USE_END = ['았', '었', 'ㅂ시다', '면서', '자', '지만', '던', '면', '러', '다오', 'ㅂ니까', '다가', '아라', '자',
               '고자', '예요', '고', '을까', '구나', '다면', '으면', '라고', '와', '느라고']

    # 수어사전에 없는 명사 있는 명사로 대체
    SPECIAL_NOUN = {'꺼': '것', '거': '것', '니': '너', '내': '나'}

    # 불규칙 어미
    SPECIAL_END = {'았': '끝', '었': '끝', '으면': '면', '다면': '면', '예요': '이다', '을까': 'ㅂ니까', '다면': '면'}

    # 서술격 조사 '이다'로 변경
    SPECIAL_POST = {'이': '이다'}

    # 불규칙 접사
    SPECIAL_AFFIX = {'스럽': '스럽다', '하': '하다', '어떠한': '어떤', '이러한': '이런', '그러한': '그런'}

    # 수어사전에 없는 부사 있는 부사로 대체
    SPECIAL_ADVERB = {'근데': '그런데', '각각': '각'}

    # 기호
    SPECIAL_MARK = {'?': 'ㅂ니까'}
pass
