from collections import deque
 
def solution(board):
    answer = int(1e9)
 
    MAX_VALUE = int(1e6)
 
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    size = len(board)
    co_board = [[MAX_VALUE] * size for _ in range(size)]
    # 각 위치에 도달하는 최소 비용을 저장하는 2차원 배열
    
    q = deque() 
    # 초기 위치인 (0,0)과 시작 방향(우측과 하단)으로 설정
    
    q.append((0,0,1,0))
    q.append((0,0,2,0))
 
    while q:
        cx, cy, c_dire, c_cost = q.popleft()
        
        if cx == size - 1 and cy == size -1:
            answer = min(answer, c_cost)
            continue
 
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            cost = 0
            #격자 벗어나거나,벽이 있는 경우
            if nx < 0 or ny < 0 or nx >= size or ny >= size or board[nx][ny] == 1:
                continue
            # # 뒤로 돌아가는 방향 제외
            # if c_dire + 2 == i or c_dire - 2 == i:
            #     continue
            # 현재 방향과 이동하려는 방향이 같으면
            if c_dire == i:
                cost = 100
            # 다른 방향으로 전환 하는 경우
            else:
                cost = 500 + 100
            # 최소 비용 갱신
            if co_board[nx][ny] >= c_cost + cost:
                co_board[nx][ny] = c_cost + cost
                q.append((nx, ny, i, c_cost + cost))
            
    print(answer)

    return answer