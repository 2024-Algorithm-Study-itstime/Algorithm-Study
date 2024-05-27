from collections import deque
def solution(maps):
    n,m=len(maps), len(maps[0])
    #상하좌우
    dx, dy=[-1,1,0,0],[0,0,-1,1]
    route=deque()
    route.append([0,0])
    while route:
        x,y=route.popleft()
        #상하좌우 길 탐색
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            #범위 설정(맵 내부이면서,벽이 없는것 확인)
            if 0<=nx<n and 0<=ny<m and maps[nx][ny]==1:
                maps[nx][ny]=maps[x][y]+1
                route.append((nx,ny))
    #리스트 마지막 원소 출력
    return maps[-1][-1] if maps[-1][-1]>1 else -1