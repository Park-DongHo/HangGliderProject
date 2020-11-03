from aws.models import *    # db수정
from django.conf import settings
from .similarityVoca import SimilarytyWord

def matchingSign(Morpheme_path):    # 여기수정
    print('##Match Sign Start...')
    line = Morpheme_path
    
    results = []
    words = line[0]
    idx=0
    for word in words:
        idx+=1
        try:
            # 형태소가 숫자일 때,
            if word.isdigit():
                find_word = Number.objects.get(word=word)
                results.append(find_word.location)
                print(word)

            # 형태소가 DB 검색 시 1개 일 때,
            elif Basic.objects.filter(word=word).count() == 1:
                find_word = Basic.objects.get(word=word)
                results.append(find_word.location)
                print(word)

            # 형태소가 DB 검색 시 여러 개 일 때,
            elif Basic.objects.filter(word=word).count() > 1:
                find_word = Basic.objects.filter(word=word)
                print(word)

                # 참조단어 추가하는 코드
                


                # 명사 list, 왼쪽 오른쪽 명사거리, 명사, 참조단어 list, href list
                noun = []
                nounSub = []
                refList = []
                locationList = []

                # 품사 리스트
                parts = line[1]  # 품사

                for i in range(idx-2, -1, -1):
                    if(parts[i] == "명사"):
                        noun.append(words[i])
                        nounSub.append(idx - i -1)
                        break

                for i in range(idx, len(parts)):
                    if(parts[i] == "명사"):

                        noun.append(words[i])
                        nounSub.append(i-idx+1)
                        break

                if(nounSub[0]>nounSub[1]):
                    N = noun[1]
                else:
                    N = noun[0]

                # 같은 품사 갯수
                samePart = 0
                href = ''
                # 일차적으로 품사가 일치하는 단어로 반환
                for result in find_word:
                    if result.part == parts[idx-1]:
                        samePart += 1
                        print('일치하는 품사가 있다')
                        href = result.location
                    refList.append(result.ref_word)
                    locationList.append(result.location)
                    

                if(samePart == 1):
                    results.append(href)

                else:
                    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
                    print('단어 : ', word)
                    print("refList :        ",refList)
                    print('가장 가까운 명사 : ' , N)
                    sim = SimilarytyWord()
                    n = sim.calc_similarity(N, refList)
                    print('유사도 결과 단어 : ')
                    print(refList[n])
                    if(n == -1):
                        results.append(locationList[0])
                    else:
                        results.append(locationList[n])
            
        except:
            continue

    print(results)
    print('##Match Sign End')
    return results