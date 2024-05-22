def solution(operations):
    answer = []
    queue =[]
    for i in operations:
        if i[0]=="I":
            queue.append(int(i[2:]))
        else:
            if queue ==[]:
                pass
            else:
                if i == "D 1":
                    queue.remove(max(queue))
                if i == "D -1":
                    queue.remove(min(queue))
    if queue ==[]:
        answer=[0,0]
    else:
        answer = [max(queue),min(queue)]
    return answer

