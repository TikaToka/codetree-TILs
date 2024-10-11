n, m, k = map(int, input().split())

board = [[0 for _ in range(n)] for _ in range(n)]

point = []
info = []

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

def check(node):
    return 0<=node[0]<n and 0<=node[1]<n


def dfs(board, start):
    tovisit = []
    visited = []
    tovisit.append(start)
    while tovisit:
        node = tovisit.pop()
        visited.append(node)
        (x, y) = node
        if board[x][y] == 3:
            return visited
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if board[x][y] == 1:
                if check((nx, ny)) and board[nx][ny] == 2 and (nx, ny) not in visited and (nx, ny) not in tovisit:
                    tovisit.append((nx, ny))
            elif board[x][y] == 2:
                if check((nx, ny)) and board[nx][ny] in [2, 3] and (nx, ny) not in visited and (nx, ny) not in tovisit:
                    tovisit.append((nx, ny))
    return None


for i in range(n):
    temp = input().split()
    for j in range(n):
        board[i][j] = int(temp[j])

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            temp = dfs(board, (i, j))
            info.append(temp)
            point.append(0)

    
for turn in range(k):
    # 공 방향
    t = turn % (4*n)
    if t // n == 0:
        ball = (t, 0)
        bx, by = (0, 1)
    elif t // n == 1:
        ball = (n-1, t-n)
        bx, by = (-1, 0)
    elif t // n == 2:
        ball = (3*n - 1 - t , n-1)
        bx, by = (0, -1)
    else:
        ball = (0, 4*n-t - 1)
        bx, by = (1, 0)

    # people move
    for i in range(len(info)):
        # 처음 갈사람은 고려가 필요함
        cand = {}
        first = info[i][0]
        for d in range(4):
            nx, ny = first[0] + dx[d], first[1] + dy[d]
            if check((nx, ny)):
                if board[nx][ny] in [3,4]:
                    cand[board[nx][ny]] = (nx, ny)

        nInfo = info[i][:]

        for j in range(1, len(nInfo)):
            nInfo[j] = info[i][j-1]

        if 3 in cand.keys():
            nInfo[0] = cand[3]
        else:
            nInfo[0] = cand[4]

        board[info[i][-1][0]][info[i][-1][1]] = 4
        board[info[i][0][0]][info[i][0][1]] = 2

        board[nInfo[-1][0]][nInfo[-1][1]] = 3
        board[nInfo[0][0]][nInfo[0][1]] = 1


        info[i] = nInfo[:]

    # print(info)

    # 공 주고 점수
    while check(ball):
        find = False
        team_idx = -1
        for i in range(len(info)):
            for j in range(len(info[i])):
                if ball == info[i][j]:
                    point[i] += (j+1) ** 2
                    team_idx = i
                    find = True
                    break
            if find:
                break
        # ball move
        if not find:
            ball = (ball[0] + bx, ball[1] + by) 
        # change order
        else:
            info[team_idx] = info[team_idx][::-1]
            board[info[team_idx][0][0]][info[team_idx][0][1]] = 1
            board[info[team_idx][-1][0]][info[team_idx][-1][1]] = 3
            break

        

print(sum(point))