dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

def rotate(board, n):
    nBoard = [row[:] for row in board]
    for i in range(n):
        for j in range(n):
            nBoard[i][j] = board[n-1-j][i] - 1 if board[n-1-j][i]>0 else board[n-1-j][i] # [row[b:3] for row in board[a:a+3])]
    return nBoard

def Hrotate(board, n):
    nBoard = [row[:] for row in board]
    for i in range(n):
        for j in range(n):
            nBoard[i][j] = board[n-1-j][i] # [row[b:3] for row in board[a:a+3])]
    return nBoard


def distance(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1-x2) + abs(y1-y2)

def check(node):
    (x, y) = node
    return 1<=x<N+1 and 1<=y<N+1

N, M, K = map(int, input().split())

human = []


board = [[0 for _ in range(N+1)] for _ in range(N+1)]
hBoard = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, N+1):
    temp = input().split()
    for j in range(1, N+1):
        board[i][j] = int(temp[j-1])

for i in range(M):
    x, y = input().split()
    human.append((int(x), int(y)))
    hBoard[int(x)][int(y)] = 1

ex, ey = map(int, input().split())
hBoard[ex][ey] = -1
movement = 0

for i in range(K):
    # print(i)
    # print("time", i)
    human = sorted(human, key=(lambda x: distance(x, (ex, ey))), reverse=True)
    # print(human)
    # print(ex, ey)
    # print(hBoard)
    # move
    for h in range(len(human)-1, -1, -1):
        # if human[h] == None:
        #     continue
        x, y = human[h][0], human[h][1]
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if check((nx, ny)) and board[nx][ny] ==0 and distance((x, y), (ex, ey)) > distance((nx, ny), (ex, ey)):
                if (nx, ny) == (ex, ey):
                    hBoard[x][y] -= 1
                    human.pop(h)
                    
                else:
                    hBoard[x][y]=0
                    human[h] = (nx, ny)
                    hBoard[nx][ny] += 1
                movement += 1
                break

    if not human:
        break

    found = False
    # find box
    for j in range(2, N):
        for k in range(1, N-j+1+1):
            for l in range(1, N-j+1+1):
                if not (k <= ex < k+j and l <= ey < l+j): # 출구 유무
                    continue
                # 사람유무
                for h in range(len(human)):
                    # if human[h] == (-1 * N, -1 * N):
                    #     continue
                    (hx, hy) = human[h]
                    if (k <= hx < k+j and l <= hy < l+j):
                        # print(j, k, l)
                        temp = [row[l:l+j] for row in board[k:k+j]]
                        rotated = rotate(temp, j)
                        for p in range(k, k+j):
                            for q in range(l, l+j):
                                board[p][q] = rotated[p-k][q-l]
                        temp = [row[l:l+j] for row in hBoard[k:k+j]]
                        rotated = Hrotate(temp, j)
                        for p in range(k, k+j):
                            for q in range(l, l+j):
                                hBoard[p][q] = rotated[p-k][q-l]
                        human = []
                        for p in range(1, N+1):
                            for q in range(1, N+1):
                                if hBoard[p][q] == -1:
                                    ex, ey = p, q
                                elif hBoard[p][q] > 0:
                                    for i in range(hBoard[p][q]):
                                        human.append((p, q))
                        found = True
                        break
                if found:
                    break
            if found:
                break
        if found:
            break

    hBoard = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for h in human:
        (x, y) = h
        hBoard[x][y] += 1
        hBoard[ex][ey] = -1

    # for j in board[1:]:
    #     print(j[1:])
    # print('.')
    
    # print(human)
    # print(ex, ey)
    # print(movement)

print(movement)
print(ex, ey)