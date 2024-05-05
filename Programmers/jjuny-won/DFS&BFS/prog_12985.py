def num_divide (n):
    
    if n%2==0:
        n=n//2
    else:
        n= n//2+1
    return n


def solution(n,a,b):
    answer = 0

    for i in range(n):
        if a>b:
            tmp = a
            a =b
            b= tmp
    
        if b%2==0 and b == a+1:
            break
        if a == 1:
            a=1
        else:
            a = num_divide(a)
        
        if b == 1:
            b =1
        else:
            b = num_divide(b)
        answer +=1
        
        print(a,b,answer+1)
    return answer+1

    


n,a,b = map(int,input().split())
solution(n, a, b)