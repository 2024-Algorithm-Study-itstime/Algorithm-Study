from collections import deque

def solution(food):
    answer = ""
    queue = deque([0])
    for i in range(len(food)-1, -1, -1):
        k = food[i] // 2
        for _ in range(k):
            queue.appendleft(i) 
            queue.append(i)
    
    for i in queue:
        answer += str(i)
    return answer