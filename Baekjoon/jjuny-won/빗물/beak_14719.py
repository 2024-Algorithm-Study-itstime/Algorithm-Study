h,w = map(int,input().split())
arr = list(map(int,input().split()))

#가장 큰 수를 기준으로 나눈다

result=0

for i in range(1,w-1):
    left = max(arr[:i])
    right = max(arr[i+1:])
    m = min(left,right)
    if(m>arr[i]):
        result += m-arr[i]
print(result)