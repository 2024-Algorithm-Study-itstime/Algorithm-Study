# 최댓값과 최솟값


def solution(s):
    answer = ''
    strs = s.split(' ')
    nums = []
    for i in strs:
        nums.append(int(i))
    answer = f"{min(nums)} {max(nums)}"
         
    return answer