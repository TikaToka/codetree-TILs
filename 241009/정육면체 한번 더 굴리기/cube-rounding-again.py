dice = {4: {5, 1, 2, 6},
        2: {4, 1, 3, 6},
        5: {3, 1, 4, 6},
        1, }
arrow = [0, 0, 3, 1, 2, 1]
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
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if check((nx, ny)) and (nx, ny) not in visited, and (nx, ny) not in tovisit and board[nx][ny] == value:
                tovisit.append((nx, ny))

    return visited
n, m = map(int, input().split())

board = [[0 for _ in range(n)] for _ in range(n)]

x, y = 0, 0

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

way = 0

value = 3

answer = 
for turn in range(m):
    x, y = x + dx[way], y + dy[way]
    for i in range(n):
        board[i] = [x for x in map(int, input().split())]
    # select d
    if turn != 0:

    count = dfs(board, (x, y))
    answer += board[x][y] * count

    # change d
    if board[x][y] < value:
        way = (way + 1) % 4
    elif board[x][y] > value:
        way = (way - 1) % 4

    nx, ny = x + dx[way], y + dy[way]
    if not check((nx, ny)):
        way = (way + 2) % 4