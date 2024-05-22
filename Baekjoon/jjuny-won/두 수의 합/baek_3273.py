
from itertools import combinations
import sys

n = int(input())
arr = list(map(int,sys.stdin.readline().split()))
x = int(input())
cnt =0 

arr.sort()
left, right = 0, n - 1

while left < right:
    current_sum = arr[left] + arr[right]
    if current_sum == x:
            cnt += 1
            left += 1
            right -= 1
    elif current_sum < x:
            left += 1
    else:
            right -= 1

print(cnt)