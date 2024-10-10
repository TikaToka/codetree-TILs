from collections import deque

dx = (-1, 0, 0, 1)
dy = (0, -1, 1, 0)

def check(n1):
    return 0<=n1[0]<n and 0<=n1[1]<n

def bfs(start, end):
    tovisit = deque()
    visited = set()
    tovisit.append(start)
    parent = {}
    parent[start] = None
    while tovisit:
        node = tovisit.popleft()
        visited.add(node)
        if node == end:
            output = [node]
            while parent[node] != None:
                output.append(parent[node])
                node = parent[node]
            return list(reversed(output))
        for d in range(4):
            nx, ny = node[0] + dx[d], node[1] + dy[d]
            if check((nx, ny)) and (nx, ny) not in visited and (nx, ny) not in tovisit and (nx, ny) not in usedCamp and (nx, ny) not in usedConvei:
                tovisit.append((nx, ny))
                parent[(nx, ny)] = node
    return None


n, m = map(int, input().split())

human = []
done = [False for _ in range(m)]
convei = []
camp = set()

usedCamp = set()
usedConvei = set()

for i in range(n):
    temp = input().split()
    for j in range(n):
        if int(temp[j]) == 1:
            camp.add((i, j))
        
for i in range(m):
    x, y = map(int, input().split())
    convei.append((x-1, y-1))

routes = []
t = 0
while len(usedConvei) < m:
    fin = []
    for i in range(len(human)):
    # 1
        if not done[i]:
            # for j in range(1, len(routes[i])):
            #     if routes[i][j] in usedCamp or routes[i][j] in usedConvei:
            #         routes[i] = bfs(human[i], convei[i])
            #         break
            if routes[i][1] in usedCamp or routes[i][1] in usedConvei:
                routes[i] = bfs(human[i], convei[i])
            human[i] = routes[i][1]
            routes[i].pop(0)
    # 2
            if human[i] == convei[i]:
                fin.append(i)
    for i in fin:
        usedConvei.add(convei[i])
        done[i] = True
    # 3
    if 1 <= t <= m:
        mini = 3 * n
        target = ()
        x, y = convei[t-1]
        opt = []
        for (a, b) in camp:
            if (a, b) in usedCamp:
                continue
            temp = bfs((a, b), (x, y))
            if temp == None:
                continue
            dist = len(temp) - 1
            if dist < mini:
                target = (a, b)
                mini = dist
                opt = temp
            elif dist == mini:
                if a < target[0]:
                    target = (a, b)
                    opt = temp
                elif a == target[0]:
                    if b < target[0]:
                        target = (a, b)
                        opt = temp
            
        human.append(target)
        usedCamp.add(target)
        routes.append(opt)

    if len(usedConvei) < m:
        t += 1
print(t)