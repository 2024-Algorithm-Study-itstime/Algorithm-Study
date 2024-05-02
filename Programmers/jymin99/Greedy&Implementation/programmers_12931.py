def solution(n):
    answer = 0
    
    for i in range(9,0,-1):
        answer=answer+(n%(10**i))//(10**(i-1))
        

    return answer