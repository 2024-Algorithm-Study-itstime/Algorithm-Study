import sys
input = sys.stdin.readline
N = int(input())
S, T = '', ''
for _ in range(N):
    s = input().rstrip()
    S += s
 
cnt = 0
i, j = 0, N-1
while i <= j:
    if S[i] < S[j]:
        T += S[i]
        i += 1
    elif S[i] > S[j]:
        T += S[j]
        j -= 1
    else:
        ii, jj = i, j
        diff = False
        while ii <= jj:
            if S[ii] < S[jj]:
                T += S[i]
                i += 1
                diff = True
                break
 
            elif S[ii] > S[jj]:
                T += S[j]
                j -= 1
                diff = True
                break
 
            else:
                ii += 1
                jj -= 1
            
        if not diff:
            T += S[i]
            i += 1
 
    cnt += 1
    if cnt % 80 == 0:
        T += '\n'
 
print(T)