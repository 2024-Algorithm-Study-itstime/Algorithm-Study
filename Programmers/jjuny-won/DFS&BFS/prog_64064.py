
from itertools import product

def check(str1, str2):
    if len(str1) != len(str2):
        return False
    for i in range(len(str1)):
        if str1[i] == "*":
            continue
        if str1[i] != str2[i]:
            return False

    return True

def solution(user_id, banned_id):
    answer = set()
    result = [[] for i in range(len(banned_id))]


    for i in  range(len(banned_id)):
        for j in user_id:
            if check(banned_id[i],j):
                result[i].append(j)
                
    result = list(product(*result)) #모든 리스트들의 가능한 모든 조합을 생성
    # print(result)
    for r in result:
        #set(r)은 중복을 제거 , len 이 같은지 확인
        if len(set(r)) == len(banned_id):
            answer.add("".join(sorted(set(r)))) #answer 이라는 set에 저장하기 위해 set (r)
            
    # print(answer)
    return len(answer)