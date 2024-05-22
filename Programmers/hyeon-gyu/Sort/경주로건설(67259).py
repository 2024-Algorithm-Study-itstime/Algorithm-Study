from collections import deque

dx = [-1,1,0,0] #상하좌우
dy = [0,0,-1,1]
    # 오른쪽 인덱스 3, 아래 인덱스 1
def bfs(board,dir):
    n = len(board)
    costgraph = [ [1e9] * n for _ in range(n)] # 비용그래프
    
    queue = deque()
    queue.append((0,0,0,dir)) # 시작x, 시작y, 시작cost, 방향
    while queue:
        x,y,c,d = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            nd = i # 다음 방향
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                if d == nd:
                    nc = c + 100
                else:
                    nc = c + 600
                
                if costgraph[nx][ny] > nc:
                    costgraph[nx][ny] = nc
                    queue.append((nx, ny, nc, nd))
                    
    return costgraph[n-1][n-1]
# 다익스트라 + 비용 계산?
def solution(board):
    n = len(board)
    # 오른쪽으로 가는 방법 vs 아래로 가는 방법 둘다 실행해서 더 작은 값을 정답으로
    return min(bfs(board,3), bfs(board,1))