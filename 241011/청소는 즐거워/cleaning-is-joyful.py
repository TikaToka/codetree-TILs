import  math

def check(node):
    return 0<= node[0] < n and 0 <= node[1] < n

def update(board, score, node, prev):
    ux = (1, 0, -1, 0)
    uy = (0, 1, 0, -1)
    tx = (-1, 1, 1, -1)
    ty = (-1, -1, 1, 1)

    (x, y) = node
    sums = 0
    dust = []
    final = (-1, -1)
    for d in range(4):
        nx, ny = x, y
        where = (2, 2)
        for k in range(2):
            nx, ny = nx + ux[d], ny + uy[d]
            where = where[0] + ux[d], where[1] + uy[d]
            if score[where[0]][where[1]] != 0:
                if check((nx, ny)):
                    if (nx, ny) == prev:
                        break
                    elif score[where[0]][where[1]] == -1:
                        final = (nx, ny)
                    else:
                        board[nx][ny] += math.floor(board[x][y] * score[where[0]][where[1]])
                else:
                    if score[where[0]][where[1]] == -1:
                        final = (nx, ny)
                    else:
                        dust.append(math.floor(board[x][y] * score[where[0]][where[1]]))
                if score[where[0]][where[1]] > 0:
                    sums += math.floor(board[x][y] * score[where[0]][where[1]])
    
    for d in range(4):
        where = (2, 2)
        nx, ny = x + tx[d], y + ty[d]
        where = where[0] + tx[d], where[1] + ty[d]
        if score[where[0]][where[1]] != 0:
            if check((nx, ny)):
                board[nx][ny] += math.floor(board[x][y] * score[where[0]][where[1]])
            else:
                dust.append(math.floor(board[x][y] * score[where[0]][where[1]]))
            sums += math.floor(board[x][y] * score[where[0]][where[1]])

    if check(final):
        board[final[0]][final[1]] += board[x][y] - sums
    else:
        dust.append(board[x][y] - sums)

    board[x][y] = 0

    # print(dust)

    return board, sum(dust)

def rotateL(b):
    nB = [row[:] for row in b]
    for i in range(5):
        for j in range(5):
            nB[i][j] = b[j][5-1-i]

    return nB

        
def snail(board):
    x = n // 2
    y = n // 2

    dx = (0, 1, 0, -1)
    dy = (-1, 0, 1, 0)

    score = [[0 for _ in range(5)] for _ in range(5)]
    score[0][2] = 0.02
    score[1][1] = 0.1
    score[1][2] = 0.07
    score[1][3] = 0.01
    score[2][0] = 0.05
    score[2][1] = -1
    score[3][1] = 0.1
    score[3][2] = 0.07
    score[3][3] = 0.01
    score[4][2] = 0.02

    answer = 0

    step = 1
    cnt = 0
    d = 0
    while check((x, y)):
        for i in range(step):
            prev = (x, y)
            x, y = x + dx[d], y + dy[d]
            if not check((x, y)):
                break
            if board[x][y] == 0:
                continue
            # print('start', (x ,y))
            # print(score)
            board, dust = update(board, score, (x, y), prev)
            # print(board)
            # print(dust)
            # print(dust)
            answer += dust
            # print(board)
        cnt += 1
        score = rotateL(score)[:]

        d = (d+1)%4
        
        if cnt == 2:
            cnt = 0
            step += 1
        # print(board)


    return answer
        
n = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    board[i] = [x for x in map(int, input().split())]

answer = snail(board)

# print(board)

print(answer)