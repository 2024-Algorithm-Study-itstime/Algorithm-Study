import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

data_sorted = sorted(arr, key=lambda x:(x[1], x[0]))
#[[2, 2], [3, 3], [2, 3], [1, 3]]
#[[2, 2], [1, 3], [2, 3], [3, 3]]

cnt  =0 
end_time =0
for a in data_sorted:
    if a[0] >= end_time:
        cnt +=1
        end_time = a[1]
print(cnt)       
