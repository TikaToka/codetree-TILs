from collections import deque

dx = (0, 1, 0, -1, -1, 1, 1, -1)
dy = (1, 0, -1, 0, 1, 1, -1, -1)

def bfs(board, start, end):
    tovisit = deque()
    visited = []
    parent = {}
    tovisit.append(start)
    while tovisit:
        # print(tovisit)
        node = tovisit.popleft()
        visited.append(node)
        if node == end:
            path = [node]
            curr = end
            while curr != start:
                path.append(parent[curr])
                curr = parent[curr]
            return list(reversed(path))
        (x, y) = node
        for d in range(4): # 상하좌우
            nx, ny = x + dx[d], y + dy[d]
            nx = nx % N
            ny = ny % M
            if (nx, ny) not in visited and board[nx][ny] > 0 and (nx, ny) not in tovisit:
                tovisit.append((nx, ny))
                parent[(nx, ny)] = (x, y)

    return None

N, M, K = map(int, input().split())

board = [[] for _ in range(N)]

for i in range(N):
    board[i] = [int(x) for x in input().split()]

recent = [[-1 for _ in range(M)] for _ in range(N)]
# print(board)
for i in range(K):
    # select weak
    weak = (-1, -1)
    weakDmg = 5001
    for a in range(N):
        for b in range(M):
            if board[a][b] <= 0:
                continue
            if board[a][b] < weakDmg: #dmg
                weak = (a, b)
                weakDmg = board[a][b]
            elif board[a][b] == weakDmg:
                if recent[a][b] > recent[weak[0]][weak[1]]: #recent
                    weak = (a, b)
                    weakDmg = board[a][b]
                elif recent[a][b] == recent[weak[0]][weak[1]]:
                    if a + b > weak[0] + weak[1]: # r + c
                        weak = (a, b)
                        weakDmg = board[a][b]
                    elif a + b == weak[0] + weak[1]:
                        if b > weak[1]: # c
                            weak = (a, b)
                            weakDmg = board[a][b]
    recent[weak[0]][weak[1]] = i
    board[weak[0]][weak[1]] += N + M
    weakDmg += N + M
    # attack
    strong = (-1, -1)
    strDmg = -1
    for a in range(N):
        for b in range(M):
            if board[a][b] <= 0 or (a, b) == weak:
                continue
            if board[a][b] > strDmg: #dmg
                strong = (a, b)
                strDmg = board[a][b]
            elif board[a][b] == strDmg:
                if recent[a][b] < recent[strong[0]][strong[1]]: #recent
                    strong = (a, b)
                    strDmg = board[a][b]
                elif recent[a][b] == recent[strong[0]][strong[1]]:
                    if a + b < strong[0] + strong[1]: # r + c
                        strong = (a, b)
                        strDmg = board[a][b]
                    elif a + b == strong[0] + strong[1]:
                        if b < strong[1]: # c
                            strong = (a, b)
                            strDmg = board[a][b]
    # attack
    route = bfs(board, weak, strong)
    # print(route)
    #razer
    if route != None:
        for node in route:
            if node == weak:
                continue
            elif node != strong:
                board[node[0]][node[1]] -= weakDmg // 2
            else:
                board[node[0]][node[1]] -= weakDmg
        # repair
        for a in range(N):
            for b in range(M):
                if board[a][b] > 0:
                    if (a, b) not in route:
                        board[a][b] += 1
    else: # bomb
        attacked = set(weak)
        (x, y) = strong
        board[x][y] -= weakDmg
        attacked.add((x, y))
        for d in range(8):
            nx, ny = x + dx[d], y + dy[d]
            nx = nx % N
            ny = ny % M
            if board[nx][ny] > 0 and not((nx, ny) == weak):
                board[nx][ny] -= weakDmg // 2
                attacked.add((nx, ny))
        # repair
        for a in range(N):
            for b in range(M):
                if board[a][b] > 0 and (a, b) not in attacked:
                    board[a][b] += 1
    cnt = 0
    for a in range(N):
        for b in range(M):
            if board[a][b] > 0:
                    cnt += 1
    if cnt == 1:
        break
maxDmg = -9999999999999

for a in range(N):
    for b in range(M):
        if board[a][b] > maxDmg:
            maxDmg = board[a][b]
print(maxDmg)