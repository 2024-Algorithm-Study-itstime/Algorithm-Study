def solution(N, stages):
    answer = []
    stage ={}
    for i in range(1,N+1):
        total =0
        fail=0
        for j in stages:
            if j >=i:
                total +=1
            if j==i:
                fail +=1
        if total == 0:
            stage[i] =0
        else:
            stage[i] = fail/total

    sorted_stage = sorted(stage.items(), key = lambda item:item[1] ,reverse=True)  
    for i in sorted_stage:
        answer.append(i[0])
        
    
    return answer