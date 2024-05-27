def solution(board, skill):
    n = len(board)
    m = len(board[0])
    damage = [[0] * (m + 1) for _ in range(n + 1)] #damage에 배열 크기 설정

    #skill 배열을 순회하면서 각 공격/방어 정보를 damage 배열에 반영. 공격은 양수 값으로, 방어는 음수 값으로 표현
    for t, r1, c1, r2, c2, degree in skill:
        if t == 1:
            degree = -degree
        damage[r1][c1] += degree
        damage[r1][c2 + 1] -= degree
        damage[r2 + 1][c1] -= degree
        damage[r2 + 1][c2 + 1] += degree

    #각 행의 변화량을 누적합으로 계산
    for i in range(n):
        for j in range(m):
            damage[i][j + 1] += damage[i][j]

    for j in range(m):
        for i in range(n):
            damage[i + 1][j] += damage[i][j]

    #각 셀의 최종 값(원래 값 + 변화량)이 양수인 경우 intact_count를 증가
    intact_count = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] + damage[i][j] > 0:
                intact_count += 1

    return intact_count
