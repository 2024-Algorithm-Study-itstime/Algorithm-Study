import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())
arr = ""
for _ in range(n):
    arr += input().strip()
    

left, right = 0, n-1
tmp = ""

while left <= right:
    if arr[left:right+1] < arr[left:right+1][::-1]:
        tmp += arr[left]
        left += 1
    else:
        tmp += arr[right]
        right -= 1
result = ""
for i in range(0,len(tmp),80):
    result += tmp[i:i+80] + '\n'
print(result)