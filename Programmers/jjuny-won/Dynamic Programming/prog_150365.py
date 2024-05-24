
def solution(n, m, x, y, r, c, k):
    d = {'u': (0,1), 'd': (0, -1), 'r': (1, 0), 'l': (-1, 0)}
    diff = abs(x-r)+abs(y-c)
    print(diff)  
    # 최소 거리와 k 비교
    if diff%2!=k%2 or diff>k:
        return 'impossible'

    answer = ''

    rest = k-diff
    lcount ,rcount ,dcount ,ucount = 0
    if x<r : #내려가야함
        dcount = r-x
    else:
        ucount = x-r
    if y<c :
        rcount = c-y
    else:
        lcount = y-c

    dplus = min( n-max(x,r), rest//2)
    rest -= dplus*2

    lplus = min( min(y,c)-1, rest//2)
    rest -= lplus*2

    answer = 'd'*(dcount+dplus)+'l'*(lcount+lplus)+'rl'*(rest//2)+'r'*(rcount+lplus)+'u'*(dplus+ucount)
    # print(lcount,lplus,rcount,rest)
    print(answer)
    return answer

solution(3,4,2,3,3,1,5)