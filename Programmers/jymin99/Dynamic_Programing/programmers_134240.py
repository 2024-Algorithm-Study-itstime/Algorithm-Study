def solution(food):
    answer = ''
    player1=''
    for i in range(1,len(food)):
        for j in range (food[i]//2):
            player1+=str(i)
    player2=player1[::-1]
    answer=player1+'0'+player2
    return answer