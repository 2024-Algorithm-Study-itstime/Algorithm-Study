cnt = 0
def dfs(numbers, target, idx, tot):
    global cnt
    if idx == len(numbers):
        if tot == target:
            cnt += 1
        return
    
    dfs(numbers, target, idx+1, tot+numbers[idx])
    dfs(numbers, target, idx+1, tot-numbers[idx])
    
def solution(numbers, target):

    dfs(numbers, target, 0, 0)
    return cnt