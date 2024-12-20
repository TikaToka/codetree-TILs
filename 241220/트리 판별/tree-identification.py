m = int(input())

edges = [[] for _ in range(10001)]

nodes = set()

for i in range(m):
    x, y = map(int, input().split())
    edges[x].append(y)
    nodes.add(x)
    nodes.add(y)

parent = [0] * (10001)
visited = [False] * (10001)

def dfs(x):
    visited[x] = True
    for y in edges[x]:
        if not visited[y]:
            parent[y] = x
            dfs(y)

dfs(1)

start = 0

for i in range(1, len(parent)):
    if i in nodes and parent[i] == 0:
        start = i

if start == 0:
    print(0)
else:
    edges = [[] for _ in range(10001)]

    for i in range(1, len(parent)):
        if parent[i] != 0:
            edges[parent[i]].append(i)


    visited = [False] * (10001)

    cnt = 0
    def dfs(x):
        global cnt
        tovisit = [(x, 0)]
        while tovisit:
            cnt += 1
            x, p = tovisit.pop()
            visited[x] = True
            for y in edges[x]:
                if y == p:
                    continue
                if visited[y]:
                    return 0
                else:
                    tovisit.append((y, x))
        return 1


    if dfs(start):
        if cnt == m+1:
            print(1)
        else:
            print(0)
    else:
        print(0)