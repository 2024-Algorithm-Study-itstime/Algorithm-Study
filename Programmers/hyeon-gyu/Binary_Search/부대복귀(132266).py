# from collections import deque

# def bfs(graph, start, destination):
#     visited = [-1] * (len(graph))
#     queue = deque([])  # (현재 노드, 거리)
    
#     while queue:
#         current, dist = queue.popleft()
        
#         if current == destination:
#             return dist
        
#         if not visited[current]:
#             visited[current] = 1
#             for neighbor in graph[current]:
#                 if not visited[neighbor]:
#                     queue.append((neighbor, dist + 1))
    
#     return -1

# def solution(n, roads, sources, destination):
#     answer = []
#     graph = [[] for _ in range(n + 1)]
    
#     for road in roads:
#         graph[road[0]].append(road[1])
#         graph[road[1]].append(road[0])
    
#     for source in sources:
#         res = bfs(graph, source, destination)
#         answer.append(res)
    
#     return answer


from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    graph = [ [] for _ in range(n+1)]
    visited = [ -1 for _ in range(n+1)] # 방문 노드 체크 & 거리 값 저장
    visited[destination] = 0 #목적지에서부터 출발
    queue = deque([destination])
    for n1, n2 in roads:
        graph[n1].append(n2)
        graph[n2].append(n1)
    while queue:
        n = queue.popleft()
        for i in graph[n]:
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[n] + 1
    for s in sources:
        answer.append(visited[s])
    return answer