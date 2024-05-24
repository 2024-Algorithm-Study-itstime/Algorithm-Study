def solution(s):
    answer = []
    for i in range(len(s)):
        if s[i] in s[:i]:
            first = s[:i].rfind(s[i])
            # first = s[:i].rindex(s[i])
            answer.append(i -first)
        else:
            answer.append(-1)
    return answer