
def solution(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            # 첫 번째 불일치가 발생했을 때, 한 쪽 문자를 제거하고 회문 검사
            if s[left + 1: right + 1] == s[left + 1: right + 1][::-1] or s[left: right] == s[left: right][::-1]:
                return 1  # 유사 회문
            
            else:
                return 2  # 일반 문자열
        left += 1
        right -= 1

    return 0  # 회문

 
n = int(input())
sen = []
for i in range(n):
    sen.append(input())
    
ans =[]
for i in sen:
    ans.append(solution(i))

for res in ans:
    print(res)