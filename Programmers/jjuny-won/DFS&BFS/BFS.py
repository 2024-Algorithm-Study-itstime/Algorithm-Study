from collections import deque

def bfs(graph, start,visited):
    queue = deque([start])
    
    visited[start] = True
    #현재 노드 방문처리
    while queue:
        v = queue.popleft()
        print(v,end= ' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[v]:
                queue.append(i)
                visited[i] = True
   
   
graph = [[],[2,3,4]]             
visited = [False] *9
bfs(graph, 1, visited)