import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(graph, cx, cy):
    graph[cx][cy] = 0 # 방문하면 바다로
    # 주변탐색
    for i in range(8):
        fx = cx + dx[i]
        fy = cy + dy[i]
        if 0 <= fx < h and 0 <= fy < w and graph[fx][fy] == 1:
            dfs(graph, fx, fy)
    
    return 1 


#상 하 좌 우 왼쪽위 오른쪽 위, 왼쪽아래, 왼쪽아래
dx = [-1, 1, 0, 0, -1, -1, 1, 1] 
dy = [0, 0, -1, 1, -1, 1, -1, 1]

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break
    graph = []
    count = 0
    for _ in range(h):
        graph.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                count += dfs(graph, i, j)
    print(count)

       
    