import sys
n = int(input())
arr = sorted(list(map(int, sys.stdin.readline().split())))
x = int(input())
count = 0
left, right = 0, n-1
while left < right:
    sum = arr[left]+arr[right]
    if sum == x:
        count += 1
        left += 1
        continue
    elif sum < x:
        left += 1
    else:
        right -= 1

print(count)