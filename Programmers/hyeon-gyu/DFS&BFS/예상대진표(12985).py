''' def solution(n,a,b):

        88.2점 -> 테스트코드 3개 실패

    answer = 0
    while abs(a-b) != 1:
        if a % 2 != 0:
            a += 1
        if b % 2 != 0:
            b += 1
        a //= 2
        b //= 2
        answer += 1
    return answer
'''

def solution(n,a,b):
    ''' 1번2번은 1번
        3번4번은 2번
        5번6번은 3번
        7번8번은 4번
        홀수는 +1해서 나누기2
        짝수는 나누기2
    '''
    
    answer = 0
    while a != b:
        a = (a+1)//2
        b = (b+1)//2
        answer = answer+1
    return answer