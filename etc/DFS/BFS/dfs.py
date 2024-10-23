"""
DFS
* 스택 자료구조에 기초 => BUT, 구현에는 사용x
* 재귀 함수를 이용
* 깊이 우선 탐색
"""

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


graph = [
    [], [2,3,8], [1,7], [1,4,5],[3,5], [3,4], [7], [2,6,8], [1,7]
]

visited = [False]* 9

dfs(graph, 1, visited)


