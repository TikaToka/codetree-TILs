dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)
kx = (-1, 1, 1, -1)
ky = (1, 1, -1, -1)

def check(node):
    (x, y) = node
    return 0<= x < n and 0<= y < n

n, m, k, c = map(int, input().split())

board = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    board[i] = [x for x in map(int, input().split())]

kBoard = [[0 for _ in range(n)] for _ in range(n)]
killers = []


answer = 0
for yrs in range(m):
    # print(board)
    # grow +  baby
    grow = {}
    for i in range(n):
        for j in range(n):
            if board[i][j] > 0:
                cnt = 0
                tree = 0
                temp = []
                for d in range(4):
                    nx, ny = i + dx[d], j + dy[d]
                    if check((nx, ny)):
                        if board[nx][ny] == 0 and (nx, ny) not in killers:
                            cnt += 1
                            temp.append((nx, ny))
                        elif board[nx][ny] > 0:
                            tree += 1
                board[i][j] += tree
                if temp:
                    for (x, y) in temp:
                        if (x, y) not in grow.keys():
                            grow[(x, y)] = board[i][j] // cnt
                        else:
                            grow[(x, y)] += board[i][j] // cnt

    for (x, y) in grow.keys():
        board[x][y] += grow[(x, y)]

    # print(board)

    # killer
    maxcoord = (-1, -1)
    maxval = -1
    for i in range(n):
        for j in range(n):
            if board[i][j] <= 0:
                continue
            temp = board[i][j]
            for d in range(4):
                for l in range(1, k+1):
                    nx, ny = i + l * kx[d], j + l *ky[d]
                    if check((nx, ny)):
                        if board[nx][ny] > 0:
                            temp += board[nx][ny]
                        elif board[nx][ny] <=0: # 빈칸에서도
                            break
                    else: 
                        break
            # print(i, j, temp)
            if maxval < temp:
                maxval = temp
                maxcoord = (i, j)
            elif maxval == temp:
                if i < maxcoord[0]:
                    maxval = temp
                    maxcoord = (i, j)
                elif i == maxcoord:
                    if j < maxcoord[1]:
                        maxval = temp
                        maxcoord = (i, j)

    if maxval == -1:
        for i in range(n):
            for j in range(n):
                if board[i][j] == 0:
                    maxcoord = (i, j)
    # kill
    print(maxcoord)
    (x, y) = maxcoord
    if maxcoord not in killers:
        killers.append(maxcoord)
    kBoard[x][y] = c+1
    # if board[x][y] != 0:
    answer += board[x][y]
    board[x][y] = 0
    for i in range(4):
        for j in range(1, k+1):
            nx, ny = x + j * kx[i], y + j * ky[i]
            if check((nx, ny)):
                if board[nx][ny] > 0:
                    answer += board[nx][ny]
                    board[nx][ny] = 0
                    if (nx, ny) not in killers:
                        killers.append((nx, ny))
                    kBoard[nx][ny] = c+1
                elif board[nx][ny] <= 0:
                    break
            else:
                break
    # print(board)

    # decrease yr or remove
    for i in range(n):
        for j in range(n):
            if kBoard[i][j] > 0:
                kBoard[i][j] -= 1
                if kBoard[i][j] == 0:
                    killers.remove((i, j))
    # for (x, y) in killers:
    #     print(x, y)
    #     kBoard[x][y] -= 1
    #     if kBoard[x][y] == 0:
    #         print(x, y, 'killed')
    #         killers.remove((x, y))
    # print(board)
    # print(answer)

print(answer)