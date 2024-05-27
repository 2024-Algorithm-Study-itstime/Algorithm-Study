import sys
input = sys.stdin.readline
N = int(input().strip())
arr = []
for i in range(N):
    arr.append(tuple(map(int,(input().split()))))
arr.sort(key = lambda x : (x[1], x[0]))

count = 0
prev_time = 0
for (x, y) in arr:
    if x >= prev_time:
        prev_time = y
        count += 1    
print(count)