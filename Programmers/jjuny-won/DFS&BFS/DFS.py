def dfs(graph, v, visitied):
    visitied[v] = True
    print(v ,end = ' ')
    for i in graph[v]:
        if not visitied[i]:
            dfs(graph, i,visited)
    
graph = [[],[3,4,6]]
visited = [False] * 9
dfs(graph, 1, visitied)