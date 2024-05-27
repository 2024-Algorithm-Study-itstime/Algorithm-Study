from collections import deque

def solution(maps):
    n = len(maps)  # 맵의 행 크기
    m = len(maps[0])  # 맵의 열 크기
    
    visited = [[-1 for _ in range(m)] for _ in range(n)]  # value에 이동비용 저장
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 1
    
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            tx = cx + dx[i]
            ty = cy + dy[i]
            if 0 <= tx < n and 0 <= ty < m and maps[tx][ty] == 1:
                if visited[tx][ty] == -1:
                    queue.append((tx, ty))
                    visited[tx][ty] = visited[cx][cy] + 1
                    if tx == n - 1 and ty == m - 1:
                        return visited[tx][ty]
    return -1
