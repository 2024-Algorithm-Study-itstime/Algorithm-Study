def solution(board, skill):
    n, m = len(board), len(board[0])
    tmp = [[0] * (m + 1) for _ in range(n + 1)]  # 누적합 기록을 위한 배열
    
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            degree = -degree
        tmp[r1][c1] += degree
        tmp[r1][c2 + 1] -= degree
        tmp[r2 + 1][c1] -= degree
        tmp[r2 + 1][c2 + 1] += degree

    # 행 기준 누적합
    for i in range(n):
        for j in range(m):
            tmp[i][j + 1] += tmp[i][j]

    # 열 기준 누적합
    for j in range(m):
        for i in range(n):
            tmp[i + 1][j] += tmp[i][j]

    # 기존 배열과 합함
    answer = 0
    for i in range(n):
        for j in range(m):
            board[i][j] += tmp[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer

