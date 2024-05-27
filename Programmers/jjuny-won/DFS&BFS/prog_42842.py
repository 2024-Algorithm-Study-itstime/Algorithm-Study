def solution(brown, yellow):
    # yello 의 약수를 구하자
    nums = []
    for n in range(1,yellow+1):
        if yellow % n == 0:
            m= yellow//n
            # print(n,m)
            if(n+m+2)*2 == brown:
                # print(n,m)
                if n>m:
                    ans = (n+2,m+2)
                else:
                    ans = (m+2,n+2)
                print(ans)
                return list(ans)
                
    
solution(24,24)
solution(10,2)
solution(8,1)
