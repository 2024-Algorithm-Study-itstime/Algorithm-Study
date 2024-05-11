def solution(left, right):
    answer = 0
    
    while left <= right:
        count = 0
        for i in range(1, left+1//2+1):
            if left % i == 0:
                count += 1
        if count % 2 == 0:
            answer += left
        else:
            answer -= left
        left += 1
    return answer