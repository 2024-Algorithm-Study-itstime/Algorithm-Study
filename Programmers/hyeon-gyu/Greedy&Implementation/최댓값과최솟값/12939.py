
def solution(s):
    answer = ''
    s = list(map(int, s.split()))

    a = max(s)
    b = min(s)
    
    answer = str(b) + ' ' + str(a)
    return answer
