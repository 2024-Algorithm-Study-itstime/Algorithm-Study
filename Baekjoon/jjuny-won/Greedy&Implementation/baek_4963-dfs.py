import sys
input = sys.stdin.readline
from collections import deque
# 시계 방향
dx = [-1,0,1,1,1,0,-1,-1]
dy = [-1,-1,-1,0,1,1,1,0]
answer =[] 

def dfs(x,y):

    graph[y][x]=0
    for i in range(8):
        nx = x+dx[i]
        ny = y+dy[i]
            
        if 0 <= nx < w and 0 <= ny <h and graph[ny][nx] ==1:
                dfs(nx,ny)


while (True):

    graph= []
    w,h =  map(int,input().split())
    
    if (w== 0 and h ==0):
        break
    
    cnt =0
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    
    
    for y in range(h):
        for x in range(w):
            if graph[y][x]==1:
                # print(graph)
                dfs(x,y)
                cnt +=1 
    
    answer.append(cnt)


for i in answer:
    print(i)
