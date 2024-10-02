from collections import deque

def rotate(graph, middle):
    # graph는 5x5이고, middle은 3x3의 중심 좌표 (x, y)
    x, y = middle

    # 3x3 부분을 추출
    sub_grid = [row[y-1:y+2] for row in graph[x-1:x+2]]

    # 3x3 부분을 90도 시계 방향으로 회전
    rotated = [[sub_grid[2-b][a] for b in range(3)] for a in range(3)]

    # 회전된 3x3 부분을 원래 보드에 다시 삽입
    new_board = [row[:] for row in graph]
    for i in range(3):
        for j in range(3):
            new_board[x-1+i][y-1+j] = rotated[i][j]

    return new_board


def checkRange(x, y):
    return 0<= x < 5 and 0<= y <5


def dfs(graph):
    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)
    visits = []
    visited = set()
    for i in range(5):
        for j in range(5):
            tovisit = []
            if (i, j) not in visited:
                visit = set()
                tovisit.append((i, j))
                v = graph[i][j]
                while tovisit:
                    x, y = tovisit.pop()
                    visit.add((x, y))
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if checkRange(nx, ny) and (nx, ny) not in visit and (nx, ny) not in visited and graph[nx][ny]==v:
                            tovisit.append((nx, ny))
                visited = visited.union(visit)
                if len(visit) >= 3:
                    visits+=list(visit)
    return visits
    

k, m = map(int, input().split())

graph = [[] for _ in range(5)]
for i in range(5):
    line = [int(x) for x in input().split()]
    graph[i] = line

rep = deque([int(x) for x in input().split()])

answers = []
for i in range(k): # k
    answer = 0
    # center
    maxarr = []
    maxval = 0 # max
    maxrot = 4 # min
    maxq = 6 # min
    maxp = 6 # min
    maxgraph = []
    for p in range(1, 4):
        for q in range(1, 4):
            tempgraph = [row[:] for row in graph]
            # rotate
            for m in range(1, 4):
                tempgraph = rotate(tempgraph, (p, q))
                arr = dfs(tempgraph)
                if not arr:
                    continue
                if len(arr) > maxval: #value
                    maxval = len(arr)
                    maxrot = m
                    maxarr = arr
                    maxp = p
                    maxq = q
                    maxgraph = tempgraph
                elif len(arr) == maxval: #rotate
                    if maxrot > m:
                        maxrot = m
                        maxarr = arr
                        maxp = p
                        maxq = q
                        maxgraph = tempgraph
                    elif maxrot == m:
                        if maxq > q:
                            maxarr = arr
                            maxp = p
                            maxq = q
                            maxgraph = tempgraph
                        elif maxq == q:
                            if maxp > p:
                                maxarr = arr
                                maxp = p
                                maxgraph = tempgraph
    if maxval == 0:
        break
    answer += maxval
    if not maxarr:
        continue
    graph = maxgraph
    # print(graph)
    # print(maxp, maxq, maxrot)
    while True:
        # print(answer)
        # refill
        maxarr = sorted(maxarr, key=lambda x: (x[1], -x[0]))
        # print(maxarr)
        for x, y in maxarr:
            if rep:
                graph[x][y] = rep.popleft()
        # print(graph)
        # check
        arr = dfs(graph)
        if not arr:
            break
        else:
            maxarr = arr
            answer += len(arr)
    if answer != 0:
        answers.append(str(answer))

if answers:
    print(' '.join(answers))