import sys
sys.setrecursionlimit(10 ** 6)

from collections import deque

def getDistance(x, y, r, c):
    return abs(r - x) + abs(c - y)

def solution(n, m, x, y, r, c, k):
    DIRECTIONS = ['d', 'l', 'r', 'u']
    dx, dy = [1, 0, 0, -1], [0, -1, 1, 0]
    
    stack = deque([])
    stack.append([x, y, 0, ''])
    
    while stack:
        cx, cy, count, move = stack.pop()
        
        if cx == r and cy == c:
            if count == k:
                return move
            elif (k - count) % 2 == 1:
                return 'impossible'
        
        temp = []
        
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 < nx <= n and 0 < ny <= m and getDistance(nx, ny, r, c) + count + 1 <= k:
                temp.append([nx, ny, count + 1, move + DIRECTIONS[i]])
        
        temp.reverse()
        stack += temp
    
    return 'impossible'