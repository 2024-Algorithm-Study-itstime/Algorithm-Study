def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        arr = []
        for j in range(len(arr2[0])):
            tmp = 0
            for k in range(len(arr1[0])):
                tmp += arr1[i][k] * arr2[k][j]
            arr.append(tmp)
        answer.append(arr)

    return answer