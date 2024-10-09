def check(node):
    (x, y) = node
    return 0<=x<n and 0<=y<n

def bfs(board, start):
    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)
    tovisit = []
    visited = set()
    tovisit.append(start)
    value = board[start[0]][start[1]]
    while tovisit:
        (x, y) = tovisit.pop(0)
        visited.add((x, y))
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if check((nx, ny)) and (nx, ny) not in visited and (nx, ny) not in tovisit and board[nx][ny] == value:
                tovisit.append((nx, ny))

    return len(visited)


def rotate(dice, d):
    nDice = [row[:] for row in dice]
    if d == 0:
        for i in range(4):
            if i == 3:
                nDice[i][1] = dice[0][1]
            else:
                nDice[i][1] = dice[i+1][1]
    elif d == 2:
        for i in range(4):
            if i == 0:
                nDice[i][1] = dice[3][1]
            else:
                nDice[i][1] = dice[i-1][1]
    elif d == 1:
        nDice[1][0] = dice[1][1] 
        nDice[3][1] = dice[1][0]
        nDice[1][2] = dice[3][1]
        nDice[1][1] = dice[1][2]
    elif d == 3:
        nDice[1][0] = dice[3][1] 
        nDice[3][1] = dice[1][2]
        nDice[1][2] = dice[1][1]
        nDice[1][1] = dice[1][0]
    
    return nDice

n, m = map(int, input().split())

board = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    board[i] = [x for x in map(int, input().split())]

x, y = 0, 0

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

way = 1
answer = 0

dice = [[0 for _ in range(3)] for _ in range(4)]

dice[0][1] = 5
dice[1][0] = 4
dice[1][1] = 6
dice[1][2] = 3
dice[2][1] = 2
dice[3][1] = 1


for turn in range(m):

    x, y = x + dx[way], y + dy[way]
    
    dice = rotate(dice, way)

    count = bfs(board, (x, y))
    answer += board[x][y] * count

    value = dice[1][1]

    # change d
    if board[x][y] < value:
        way = (way + 1) % 4
    elif board[x][y] > value:
        way = (way - 1) % 4

    nx, ny = x + dx[way], y + dy[way]
    if not check((nx, ny)):
        way = (way + 2) % 4

print(answer)