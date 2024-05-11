### 시간초과 코드
def solution(n, left, right):
    arr = [ [0] * n for _ in range(n)]

    for i in range(n):
        arr[i][i] = i + 1
        for j in range(i, -1, -1):
            arr[j][i] = i + 1
            arr[i][j] = i + 1
    res = []
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            res.append(arr[i][j])

    return res[left:right+1]



def solution(n, left, right):
    answer = []

    for i in range(left,right+1):
        if (i%n)>(i//n):
            answer.append((i%n)+1)
        else:
            answer.append((i//n)+1)
    return answer