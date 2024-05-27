def solution(dirs):
    answer = 0
    dic = {"U" : (-1,0), "L" : (0,-1), "R" : (0,1), "D" : (1,0)}
    visited = []
    cx, cy = 0, 0
    for i in dirs:
        # 방문 여부 확인법 : [기존x,기존y,도착x,도착y] 기록
        nx, ny = cx + dic[i][0], cy + dic[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            if (cx, cy, nx, ny) not in visited and (nx, ny, cx, cy) not in visited:
                visited.append((cx, cy, nx, ny)) 
                visited.append((nx, ny, cx, cy)) # 왕복 둘다 적용해야함
                answer += 1
            cx, cy = nx, ny
    return answer
