from aws.models import *    # db수정
from django.conf import settings
from .similarityVoca import SimilarytyWord
from .nlp import NLP

def matchingSign(Morpheme_path):   
    print('##Match Sign Start...')
    line = Morpheme_path
    nlp = NLP()
    results = []
    words = line[0]
    print(words)
    idx=0

    for word in words:
        idx+=1
        try:
            # 형태소가 숫자일 때,
            if word.isdigit():
                find_word = Number.objects.get(word=word)
                results.append(find_word.location)
                print(find_word)

            # 형태소가 DB 검색 시 1개 일 때,
            elif Basic.objects.filter(word=word).count() == 1:
                find_word = Basic.objects.get(word=word)
                results.append(find_word.location)
                print(find_word)

            # 형태소가 DB 검색 시 2개 일 때,
            elif Basic.objects.filter(word=word).count() == 2:
                find_word = Basic.objects.filter(word=word)
                results.append(find_word[0].location)

            # 형태소가 DB 검색 시 여러 개 일 때,
            elif Basic.objects.filter(word=word).count() > 2:
                find_word = Basic.objects.filter(word=word)
                
                

    # ===============================================================================================
                # 명사 list, 왼쪽 오른쪽 명사거리, 명사, 참조단어 list, href list
                noun = []
                nounSub = []
                refList = []
                locationList = []
                mean_list=[]
                N=''
                # 품사 리스트
                parts = line[1]  # 품사

                # 해당 단어의 왼쪽 방향 가까운 명사 찾기.
                for i in range(idx-2, -1, -1):
                    if(parts[i] == "명사"):
                        noun.append(words[i])
                        nounSub.append(idx - i -1)
                        break
                

                # 해당 단어의 오른쪽 방향 가까운 명사 찾기
                for i in range(idx, len(parts)):
                    if(parts[i] == "명사"):

                        noun.append(words[i])
                        nounSub.append(i-idx+1)
                        break

                if len(nounSub) > 1 :
                    if(nounSub[0]>nounSub[1]):
                        N = noun[1]
                elif len(nounSub) == 1:
                    N = noun[0]
                elif N=='':
                    results.append(find_word[0].location)
                    continue

                # 같은 품사 갯수
                samePart = 0
                href = ''
                # 일차적으로 품사가 일치하는 단어로 반환
                for result in find_word:
                    part_list=[]
                    if result.mean in mean_list:
                        continue
                    if result.part == parts[idx-1]:
                        samePart += 1
                        print('일치하는 품사가 있다')
                        href = result.location
                    pre_text= nlp.relocateMorpheme(result.mean)
                    for i in range(len(pre_text[1])):
                        if pre_text[1][i] =='명사':
                            part_list.append(pre_text[0][i])
                    mean_list.append(result.mean)
                    refList.append(part_list[0])
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
            print('（￣。。￣）')
            continue
        

    print(results)
    print('##Match Sign End')
    return results