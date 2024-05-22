from itertools import combinations

def solution(number):
    answer = 0
    
    # 삼총사 조건 : -1 -2 3 도 되네 
    number.sort()
    for i in combinations(number,3):
        if sum(i) == 0:
            answer += 1
    
    return answer 