n = int(input())

edges = [[] for _ in range(n+1)]

visited = [False for _ in range(n+1)]

parent = [0 for _ in range(n+1)]

for i in range(n-1):
    x, y = map(int, input().split())
    edges[x].append(y)
    edges[y].append(x)

def traversal(x):
    for y in edges[x]:
        if not visited[y]:
            visited[y] = True
            parent[y] = x

            traversal(y)

traversal(1)

for i in range(2, n+1):
    print(parent[i])