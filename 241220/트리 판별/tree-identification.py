m = int(input())

edges = [[] for _ in range(10001)]

for i in range(m):
    x, y = map(int, input().split())
    edges[x].append(y)
    edges[y].append(x)


parent = [0] * (10001)
visited = [False] * (10001)

def dfs(x):
    visited[x] = True
    for y in edges[x]:
        if not visited[y]:
            parent[y] = x
            dfs(y)

dfs(1)

edges = [[] for _ in range(10001)]

for i in range(1, len(parent)):
    edges[parent[i]].append(i)

visited = [False] * (10001)

def dfs(x):
    visited[x] = True
    tovisit = [x]
    while tovisit:
        x = tovisit.pop()
        for y in edges[x]:
            if visited[y]:
                return 0
            else:
                tovisit.append(y)
    return 1

print(dfs(1))