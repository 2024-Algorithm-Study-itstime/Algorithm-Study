def solution(s):
    answer = []
    answer.append(-1)
    for i in range(1,len(s)):
        s_section=s[i-1::-1]
        word=s[i]
        num=s_section.find(word)
        if num==-1:
            answer.append(num)
        else:
            answer.append(num+1)     
    return answer