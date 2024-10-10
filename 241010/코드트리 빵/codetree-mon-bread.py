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
            if check((nx, ny)) and (nx, ny) not in visited and (nx, ny) not in usedCamp and (nx, ny) not in usedConvei:
                tovisit.append((nx, ny))
                parent[(nx, ny)] = node
    return None


n, m = map(int, input().split())

human = []
done = [False for _ in range(m)]
convei = []
camp = []

usedCamp = set()
usedConvei = set()

for i in range(n):
    temp = input().split()
    for j in range(n):
        # board[i][j] = int(temp[j])
        if int(temp[j]) == 1:
            camp.append((i, j))
        
for i in range(m):
    x, y = map(int, input().split())
    convei.append((x-1, y-1))

t = 0
while len(usedConvei) < m:
# for l in range(5):
    fin = []
    for i in range(len(human)):
        # 1
        if not done[i]:
            route = bfs(human[i], convei[i])
            human[i] = route[1]
            # 2
            if human[i] == convei[i]:
                fin.append(i)
                
    # 2
    for i in fin:
        usedConvei.add(convei[i])
        done[i] = True
    # 3
    if 1 <= t <= m:
        mini = 3 * n
        target = ()
        x, y = convei[t-1]
        for (a, b) in camp:
            if (a, b) in usedCamp:
                continue
            dist = len(bfs((a, b), (x, y))) - 1
            if dist < mini:
                target = (a, b)
                mini = dist
            elif dist == mini:
                if a < target[0]:
                    target = (a, b)
                elif a == target[0]:
                    if b < target[0]:
                        target = (a, b)
            
        human.append(target)
        usedCamp.add(target)
        camp.remove(target)
    if len(usedConvei) < m:
        t += 1
    # print(human)
    # print(done)
    # print(usedCamp)
    # print(usedConvei)
    # print('.')
print(t)