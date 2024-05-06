def solution(seoul):
    
    for i in seoul:
        if i == "Kim":
            idx = seoul.index(i)
    
    answer = "김서방은 "+str(idx) +"에 있다" 
    return answer