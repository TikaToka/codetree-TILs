def check(node):
    return 0<= node[0] < n and 0<= node[1]<n

def countit(node, friends):
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)
    a = 0
    b = 0
    for d in range(4):
        nx, ny = node[0] + dx[d], node[1] + dy[d]
        if check((nx, ny)):
            if board[nx][ny] == 0:
                a += 1
            elif board[nx][ny] in friends:
                b += 1
    return b, a

n = int(input())

board = [[0 for _ in range(n)] for _ in range(n)]

info = {}
for i in range(n*n):
    temp = input().split()
    idx, k = int(temp[0]), set(int(x) for x in temp[1:])
    info[idx] = k

answer = 0

for k, v in info.items():
    best =(-1, -1)
    fcnt = -1
    cnt = -1
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                continue
            tfcnt, tcnt = countit((i, j), v)
            if fcnt < tfcnt:
                best = (i, j)
                fcnt = tfcnt
                cnt = tcnt
            elif fcnt == tfcnt:
                if tcnt > cnt:
                    best = (i, j)
                    cnt = tcnt
                elif tcnt == cnt:
                    if i < best[0]:
                        best = (i, j)
                    elif i == best[0]:
                        if j < best[1]:
                            best = (i, j)
    board[best[0]][best[1]] = k


for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            fcnt, cnt = countit((i, j), info[board[i][j]])
            if fcnt > 0:
                answer += 10 ** (fcnt-1)

print(answer)