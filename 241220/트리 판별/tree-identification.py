m = int(input())

edges = [[] for _ in range(10001)]

for i in range(m):
    x, y = map(int, input().split())
    edges[x].append(y)


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


if dfs(1):
    if cnt == m+1:
        print(1)
    else:
        print(0)
else:
    print(0)