dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

def dfs(board, start):
    tovisit = []
    visited = []
    tovisit.append(start)
    value = board[start[0]][start[1]]
    while tovisit:
        node = tovisit.pop()
        visited.append(node)
        for d in range(4):
            nx, ny = node[0] + dx[d], node[1] + dy[d]
            if check((nx, ny)) and board[nx][ny] == value and (nx, ny) not in visited and (nx, ny) not in tovisit:
                tovisit.append((nx, ny))
    return visited, value

def check(node):
    (x, y) = node
    return 0<= x < n and 0<= y < n

def distance(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1-x2) + abs(y1-y2)

def rotateL(board, n):
    nBoard =[row[:] for row in board]
    for i in range(n):
        for j in range(n):
            if i == n//2 or j == n//2:
                nBoard[i][j] = board[j][n-1-i]
    return nBoard

def rotateR(board, n):
    nBoard =[row[:] for row in board]
    for i in range(n):
        for j in range(n):
            nBoard[i][j] = board[n-1-j][i]
    return nBoard

def getScore(board):
    def score(a, b):
        return (len(groups[a]) + len(groups[b])) * values[a] * values[b] * meet[a][b]
    groups = []
    groupset = set()
    values = []

    for i in range(n):
        for j in range(n):
            if (i, j) not in groupset:
                group, value = dfs(board, (i, j))
                groupset.update(group)
                groups.append(group)
                values.append(value)

    meet = [[0 for _ in range(len(groups))] for _ in range(len(groups))]

    for i in range(len(groups)):
        for j in range(i+1, len(groups)):
            for k in groups[i]:
                for l in groups[j]:
                    if distance(k, l) == 1:
                        meet[i][j] += 1

    init_score = 0
    for i in range(len(meet)):
        for j in range(i+1, len(meet)):
            if meet[i][j] > 0:
                init_score += score(i, j)

    return init_score

answer = []

n = int(input())

board = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    board[i] = [int(x) for x in input().split()]

answer.append(getScore(board))


for t in range(3):
    nBoard = [row[:] for row in board]
    board = rotateL(nBoard, n)

    for (x, y) in [(0, 0), (n//2+1, 0), (0, n//2+1), (n//2+1, n//2+1)]:
        nBoard = [row[y:y+n//2] for row in board[x:x+n//2]]
        rotated = rotateR(nBoard, n//2)
        for i in range(x, x+n//2):
            for j in range(y, y+n//2):
                board[i][j] = rotated[i-x][j-y]
    answer.append(getScore(board))


print(sum(answer))