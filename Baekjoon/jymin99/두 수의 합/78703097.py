import sys
input = sys.stdin.readline

n = int(input())
numbers= sorted(list(map(int, input().split())))
x = int(input())
cnt = 0
left=0
right=n-1

while left<right:
    total=numbers[left]+numbers[right]
    if total==x:
        cnt+=1
        left+=1
        right-=1
    elif total<x:
        left+=1
    else:
        right-=1
print(cnt)
        

#일일이 더하는 코드
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
x = int(input())

count = 0
for i in range(n):
    for j in range(i+1, n):
        if nums[i] + nums[j] == x:
            count += 1

print(count)
