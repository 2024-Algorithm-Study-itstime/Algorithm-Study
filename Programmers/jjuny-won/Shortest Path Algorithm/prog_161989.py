def solution(n, m, section):
    answer = 1
    prev = section[0]
    for i in section:
        if i - prev >= m:
            prev = i
            answer+=1
    return answer

