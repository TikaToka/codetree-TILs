n = int(input())

board = [[x for x in map(int, input().split())] for _ in range(n)]

def check(node):
    return 0<= node[0] < n and 0 <= node[1] < n

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

def dfs(start, cnt):
    tovisit = []
    # visited = set()
    cnts = []
    tovisit.append([start, cnt])
    while tovisit:
        node, cnt= tovisit.pop()
        # visited.add(node)
        still = False
        for d in range(4):
            nx = node[0] + dx[d]
            ny = node[1] + dy[d]
            if check((nx, ny)) and board[nx][ny] > board[node[0]][node[1]] and (nx, ny) not in tovisit:
                tovisit.append([(nx, ny), cnt+1])
                still = True
        if not still:
            cnts.append(cnt)
    return cnts

answer = 0

for i in range(n):
    for j in range(n):
        temp = dfs((i, j), 1)
        answer = max(answer, max(temp))

print(answer)