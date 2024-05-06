def solution(brown, yellow):
    answer = []
    arr1 = []
    arr2 = []
    tot = brown + yellow
    # 가로 세로는 무조건 3이상.
    # 가로는 세로보다 길다
    # brown + yellow로 조건에 부합하는 가로세로 경우의 수를 찾기 12 -> 4*3 / 48 -> 16*3, 12*4, 8*6
    
    # yellow 가로세로 경우의 수 
    j = 1
    while(1):
        if yellow == 1:
            arr2.append([1,1])
            break
        if j == yellow:
            break
        if yellow % j == 0:
            arr2.append([yellow//j, j])
        j = j + 1
    
    # 전체 배열의 가로세로 경우의 수
    i = 2
    while(1):
        if i >= tot / 2:
            break
        if tot % i == 0 and tot//i >= i and i >= 3 and tot//i >= 3:
            arr1.append([tot//i,i])
        i = i + 1
    
    for arr in arr1:
        for y in arr2:
            if arr[0] - y[0] >= 2 and arr[1] - y[1] >= 2 and (arr[0]-2)*(arr[1]-2)== yellow:
                answer.append(arr[0])
                answer.append(arr[1])
                break
    return answer



''' 다른 사람 풀이
def solution(brown, red):
    nm = brown + red
    for n in range(1, nm+1):
        if nm%n != 0:
            continue
        m = nm//n
        if (n-2)*(m-2) == red:
            return sorted([n, m], reverse = True)
            
'''