import sys
input = sys.stdin.readline

def check2(ans,left,right):
    while left < right:
        if ans[left] == ans[right]:
            left += 1
            right -= 1
            continue
        else:
            return False
    return True

def check(ans, left, right):
    if ans == ans[::-1]:
        return 0
    while left < right:
        if ans[left] == ans[right]:
            left += 1
            right -= 1
            continue
        res1 = check2(ans, left+1, right)
        res2 = check2(ans, left, right-1)
        if res1 or res2:
            return 1
        else:
            return 2

t = int(input())

for _ in range(t):
    ans = list(input().rstrip())
    left, right = 0, len(ans)-1
    print(check(ans, left, right))

