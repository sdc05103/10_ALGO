"""
BFS
* 큐 자료구조 이용 => deque 사용
"""

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])

    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end = " ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True   # 큐에 넣는 동시에 방문처리 
graph = [
    [], [2,3,8], [1,7], [1,4,5],[3,5], [3,4], [7], [2,6,8], [1,7]
]

visited = [False]* 9

bfs(graph, 1, visited)




