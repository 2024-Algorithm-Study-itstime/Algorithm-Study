def solution(food):
    answer = ''
    for i in range(len(food)):
        if i ==0:
            continue
        answer += str(i )*(food[i]//2)
    final_answer = answer + "0" + answer[::-1]
    return answer
input_arr = list(map(int,input().split()))
solution(input_arr)