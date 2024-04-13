def solution(operations):
    answer = []
    arr = []
 
    for i in operations:
        cmd, num = map(str, i.split())
        if cmd == 'I':
            arr.append(int(num))
            arr.sort()

        elif cmd == 'D':
            if num == '1':
                if len(arr) != 0:
                    arr.pop(len(arr)-1)
                    arr.sort()
            else:
                if len(arr) != 0:
                    arr.pop(0)
                    arr.sort()
    if len(arr) != 0:
        answer.append(arr[len(answer)-1])
        answer.append(arr[0])
    else:
        answer.append(0)
        answer.append(0)
    return answer
