import sys
input = sys.stdin.readline
from collections import deque
# 시계 방향
dx = [-1,0,1,1,1,0,-1,-1]
dy = [-1,-1,-1,0,1,1,1,0]
answer =[] 

def BFS(x,y):
    queue = deque()
    queue.append([x,y])
    graph[y][x]=0
    
    while queue:
        x,y = queue.popleft()
        for i in range(8):
            next_x = x+dx[i]
            next_y = y+dy[i]
            
            if 0 <= next_x < w and 0<=next_y<h:
                if graph[next_y][next_x] ==1:
                    queue.append([next_x,next_y])
                    graph[next_y][next_x] =0


while (True):

    graph= []
    w,h =  map(int,input().split())
    
    if (w== 0 and h ==0):
        break
    
    cnt =0
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    
    
    for i in range(h):
        for j in range(w):
            if graph[i][j]==1:
                # print(graph)
                BFS(j,i)
                cnt +=1 
    
    answer.append(cnt)


for i in answer:
    print(i)
