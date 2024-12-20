n = int(input())

edges = [[] for _ in range(n+1)]

visited = [False] * (n+1)

parent = [()] * (n+1)

for i in range(n-1):
    x, y, w = map(int, input().split())
    edges[x].append((y, w))
    edges[y].append((x, w))


# def traversal(x):
#     for y, w in edges[x]:
#         if not visited[y]:
#             visited[y] = True
#             parent[y] = (x, w)

#             traversal(y)

# traversal(1)

def dfs(start):
    maxval = 0
    maxidx = start
    visited = [False] * (n+1)
    tovisit = [(start, 0)]
    while tovisit:
        (node, w) = tovisit.pop()
        visited[node] = True
        if w > maxval:
            maxval = w
            maxidx = node
        # if parent[node] != ():
        #     i = parent[node]
        #     if not visited[i[0]] and i[0] not in tovisit:
        #         tovisit.append((i[0], w+i[1]))
        for i in edges[node]:
            if not visited[i[0]] and i[0] not in tovisit:
                tovisit.append((i[0], w+i[1]))

    return maxidx, maxval

idx, val = dfs(1)

idx, val = dfs(idx)

print(val)
    