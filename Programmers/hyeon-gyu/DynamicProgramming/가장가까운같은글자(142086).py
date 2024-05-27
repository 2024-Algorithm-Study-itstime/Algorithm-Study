def solution(s):
    answer = []
    dic = {} # 단어 : 최근에 기록한 위치 인덱스
    for i in range(len(s)):
        res = dic.get(s[i],-1)  # 두번째 인자에 -1 넣으면 에러 대신 -1을 리턴  
        if res != -1:
            answer.append(i - dic[s[i]]) # dictionary에 존재한다면 현재 인덱스에서 최근 기록한 인덱스 차이값 기록
            dic[s[i]] = i
        else:
            answer.append(-1)
            dic[s[i]] = i 
    return answer