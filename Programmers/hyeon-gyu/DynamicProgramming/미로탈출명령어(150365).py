import sys
sys.setrecursionlimit(10**5)
# bfs는 시간초과 -> 이동 경로를 전부 고려하는게 아니라 처음부터 가장 정확하고 사전순으로 빠른 경로 하나만을 탐색.
dirs = [["d", 1, 0], ["l", 0, -1], ["r", 0, 1], ["u", -1, 0]]
# dfs = 한방향으로 가능한 깊이 -> 가장 먼저 발견되는 유효한 경로가 사전순으로 빠른 경로
def solution(n, m, x, y, r, c, k):
    dist = abs(x - r) + abs(y - c)
    if dist > k:
        return "impossible"
    if dist % 2 != k % 2:
        return "impossible"

    def dfs(cy, cx, path, cnt):
        if cnt == k:
            if cy == r and cx == c:
                return path
        else:
            for prc in dirs:
                ny = cy + prc[1]
                nx = cx + prc[2]
                if 1 <= ny <= n and 1 <= nx <= m:
                    dist = abs(ny - r) + abs(nx - c)
                    # 다음 위치에서 목표 위치까지의 맨해튼 거리가 남은 이동 횟수보다 크면 그 방향으로 이동x
                    if dist > k - (cnt + 1):
                        continue 
                    rtn = dfs(ny, nx, path + prc[0], cnt + 1)
                    if rtn is not None:
                        return rtn

    answer = dfs(x, y, "", 0)
    if answer is None:
        return "impossible"
    return answer