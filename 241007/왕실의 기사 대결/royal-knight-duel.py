from collections import deque


L, N, Q = map(int, input().split())

# def change(a, b)
#     for i in knight[idx]

def check(node):
    (x, y) = node
    return 0<= x < L and 0<= y < L

def move(i, d, knight):
    tovisit = deque()
    visited = set()
    tovisit.append(i)
    while tovisit:
        i = tovisit.popleft()
        visited.add(i)
        temp = []
        for k in range(len(knight[i])):
            knight[i][k] = (knight[i][k][0] + dx[d], knight[i][k][1] + dy[d])
        for idx in knight[i]:
            if not check(idx) or board[idx[0]][idx[1]] == 2: #못움직이니 롤백해야함
                return None, None
            for j in range(len(knight)):
                if idx in knight[j] and j not in visited and j not in tovisit:# 기사가 있고 다르면 걔도 추적
                    tovisit.append(j)
                    break
    return knight, visited

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

board = [[] for _ in range(L)]
for i in range(L):
    board[i] = [int(x) for x in input().split()]

# kBoard = [[-1 for _ in range(L)] for _ in range(L)]
knight = []
health = []
alive = []
dmg = [0 for _ in range(N)]

for i in range(N):
    r, c, h, w, k = map(int, input().split())
    temp = []
    for a in range(h):
        for b in range(w):
            # kBoard[r-1+a][c-1+b] = i
            temp.append((r-1+a, c-1+b))
    knight.append(temp)
    health.append(k)
    alive.append(1)

for q in range(Q):
    # move
    i, d = map(int, input().split())
    if alive[i-1] != 1:
        continue
    # print(knight)
    temp = [row[:] for row in knight]
    temp, visited = move(i-1, d, temp)

    if temp == None:
        continue
    knight = temp
    # else:
    #     knight = temp
    #     #board update
    #     kBoard = [[-1 for _ in range(L)] for _ in range(L)]
    #     for k in range(N):
    #         if alive[k] != 1:
    #             continue
    #         for l in knight[k]:
    #             kBoard[l[0]][l[1]] = k
    # calculate dmg
    for k in range(N):
        if alive[k] != 1 or k == i-1 or k not in visited:
            continue
        for j in knight[k]:
            if board[j[0]][j[1]] == 1:
                health[k] -= 1
                dmg[k] += 1
        if health[k] <= 0:
            alive[k] = 0
            knight[k] = []
        

answer = 0

for i in range(N):
    if alive[i] == 1:
        answer += dmg[i]              

print(answer)