import sys
input = sys.stdin.readline
def dfs(v):
    visited[v]=1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)
            
N = int(input())
v = int(input())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)

for i in range(v):
    a,b = map(int,input().split())
    graph[a]+=[b]
    graph[b]+=[a]
    
dfs(1)
print(sum(visited)-1)