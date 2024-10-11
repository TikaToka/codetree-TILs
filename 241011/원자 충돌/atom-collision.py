dx = (-1, -1, 0, 1, 1, 1, 0, -1)
dy = (0, 1, 1, 1, 0, -1, -1, -1)

n, m, k = map(int, input().split())

board = [[[] for _ in range(n)] for _ in range(n)]

for i in range(m):
    x, y, m, s, d = map(int, input().split())
    board[x-1][y-1].append([m, s, d])



for time in range(k):
    nBoard = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(len(board[i][j])-1, -1, -1):
                temp = board[i][j][k]
                nx, ny = (i + dx[temp[2]] * temp[1])%4, (j + dy[temp[2]] * temp[1])%4
                nBoard[nx][ny].append(temp)
    board = [row[:] for row in nBoard]


    for i in range(n):
        for j in range(n):
            if len(board[i][j]) >= 2:
                a, b= 0, 0
                s = len(board[i][j])
                t0 = 0
                t1 = 0
                for k in range(len(board[i][j])):
                    a += board[i][j][k][0]
                    b += board[i][j][k][1]
                    if board[i][j][k][2] in [1, 3, 5, 7]:
                        t0 += 1
                    elif board[i][j][k][2] in [0, 2, 4, 6]:
                        t1 += 1
                if t0 == s or t1 == s:
                    c = 0
                else:
                    c = 1
                board[i][j] = []
                if a >= 5:
                    if c == 0:
                        for k in [0, 2, 4, 6]:
                            board[i][j].append([a//5, b//s, k])
                    else:
                        for k in [1, 3, 5, 7]:
                            board[i][j].append([a//5, b//s, k])

    print(board)

answer = 0
for i in range(n):
    for j in range(n):
        answer += len(board[i][j])
print(answer)