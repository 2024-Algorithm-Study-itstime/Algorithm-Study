def solution(seoul):
    answer = ''
    x=0;
    for i in range(len(seoul)):
        if seoul[i]=="Kim":
            x=i
    return ('김서방은 '+str(x)+'에 있다')