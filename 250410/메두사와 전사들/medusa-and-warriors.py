from collections import deque


def check(node):
    return 0<= node[0] < n and 0 <= node[1] < n


def bfs(board, start, end):
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    tovisit = deque([(start, [start])])
    visited = set(start)
    while tovisit:
        curr, path = tovisit.popleft()
        # visited.add(curr)
        if curr == (er, ec):
            return path
        (x, y) = curr
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if check((nx, ny)) and (nx, ny) not in visited and (board[nx][ny] == 0 or (nx, ny) == (er, ec)): # 
                tovisit.append(((nx, ny), path + [(nx, ny)]))
                visited.add((nx, ny))
    return []


def distance(n1, n2):
    return abs(n1[0] - n2[0]) + abs(n1[1] - n2[1])

def bfs_warrior1(board, start, end, area):
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    (x, y) = start
    cand = None
    dist = distance(start, end)
    for d in range(3, -1, -1):
        nx = x + dx[d]
        ny = y + dy[d]
        if check((nx, ny)) and area[nx][ny] != 1:
            if distance((nx, ny), end) <= dist:
                dist = distance((nx,ny), end)
                cand = (nx, ny)
    return cand


def bfs_warrior2(board, start, end, area):
    dx = (0, 0, -1, 1)
    dy = (-1, 1, 0, 0)
    (x, y) = start
    cand = None
    dist = distance(start, end)
    for d in range(3, -1, -1):
        nx = x + dx[d]
        ny = y + dy[d]
        if check((nx, ny)) and area[nx][ny] != 1:
            if distance((nx, ny), end) <= dist:
                dist = distance((nx,ny), end)
                cand = (nx, ny)
    return cand


def stone_area(start, warrior):
    stone = set()
    output = None
    N = n
    sight_map = [[0 for _ in range(N)] for _ in range(N)]

    x, y = start

    for i in range(x-1, -1, -1):
        left = max(0, y - (x - i))
        right = min(N-1, y + (x - i))
        for j in range(left, right + 1):
            sight_map[i][j] = 1

    thereis = False
    for i in range(x-1, -1, -1):
        if thereis:
            sight_map[i][y] = 0
        else:
            sight_map[i][y] = 1

        if (i, y) in warrior:
            thereis = True

    for i in range(x-1, 0, -1):
        left = max(0, y - (x - i))
        right = min(N-1, y + (x - i))
        for j in range(left, y):
            if not sight_map[i][j] or (i, j) in warrior:
                
                if j > 0:
                    sight_map[i-1][j-1] = 0
                
                sight_map[i-1][j] = 0

        for j in range(y+1, right):
            if not sight_map[i][j] or (i, j) in warrior:

                if j < n - 1:
                    sight_map[i-1][j+1] = 0

                sight_map[i-1][j] = 0

    coverage = set()
    for i in range(x - 1, -1, -1):
        left = max(0, y - (x - i))
        right = min(N - 1, y + (x - i))
        for j in range(left, right + 1):
            if sight_map[i][j]:
                for idx in range(len(warrior)):
                    if warrior[idx] == (i, j):
                        coverage.add(idx)

    if len(stone) < len(coverage):
        stone = coverage
        output = sight_map
###########################################
    sight_map = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(x+1, n):
        left = max(0, y - (i - x))
        right = min(N-1, y + (i - x))
        for j in range(left, right + 1):
            sight_map[i][j] = 1

    thereis = False
    for i in range(x+1, N):
        if thereis:
            sight_map[i][y] = 0
        else:
            sight_map[i][y] = 1

        if (i, y) in warrior:
            thereis = True

    for i in range(x+1, N-1):
        left = max(0, y - (i - x))
        right = min(N-1, y + (i - x))
        for j in range(left, y):
            if not sight_map[i][j] or (i, j) in warrior:
                
                if j > 0:
                    sight_map[i+1][j-1] = 0
                
                sight_map[i+1][j] = 0

        for j in range(y+1, right+1):
            if not sight_map[i][j] or (i, j) in warrior:

                if j < n - 1:
                    sight_map[i+1][j+1] = 0

                sight_map[i+1][j] = 0

    coverage = set()
    for i in range(x + 1, N):
        left = max(0, y - (i - x))
        right = min(N-1, y + (i - x))
        for j in range(left, right + 1):
            if sight_map[i][j]:
                for idx in range(len(warrior)):
                    if warrior[idx] == (i, j):
                        coverage.add(idx)

    if len(stone) < len(coverage):
        stone = coverage
        output = sight_map
    ########################
    sight_map = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(y-1, -1, -1):
        left = max(x - (y - i), 0)
        right = min(N-1, x + (y-i))
        for j in range(left, right + 1):
            sight_map[j][i] = 1

    thereis = False
    for i in range(y-1, -1, -1):
        if thereis:
            sight_map[x][i] = 0
        else:
            sight_map[x][i] = 1

        if (x, i) in warrior:
            thereis = True

    for i in range(y-1, 0, -1):
        left = max(x - (y - i), 0)
        right = min(N-1, x + (y-i))

        for j in range(left, x):
            if not sight_map[j][i] or (j, i) in warrior:
                
                if j > 0:
                    sight_map[j-1][i-1] = 0
                
                sight_map[j][i-1] = 0

        for j in range(x + 1, right + 1):
            if not sight_map[j][i] or (j, i) in warrior:

                if j < n - 1:
                    sight_map[j+1][i-1] = 0

                sight_map[j][i-1] = 0

    coverage = set()
    for i in range(y-1, -1, -1):
        left = max(0, x - (y - i))
        right = min(N - 1, x + (y - i))
        for j in range(left, right + 1):
            if sight_map[j][i]:
                for idx in range(len(warrior)):
                    if warrior[idx] == (j, i):
                        coverage.add(idx)

    if len(stone) < len(coverage):
        stone = coverage
        output = sight_map
    ########################
    sight_map = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(y+1, N):
        left = max(x - (i - y), 0)
        right = min(N-1, x + (i-y))
        for j in range(left, right + 1):
            sight_map[j][i] = 1

    thereis = False
    for i in range(y+1, N):
        if thereis:
            sight_map[x][i] = 0
        else:
            sight_map[x][i] = 1

        if (x, i) in warrior:
            thereis = True

    for i in range(y+1, N-1):
        left = max(x - (i - y), 0)
        right = min(N-1, x + (i-y))

        for j in range(left, x):
            if not sight_map[j][i] or (j, i) in warrior:
                
                if j > 0:
                    sight_map[j-1][i+1] = 0
                
                sight_map[j][i+1] = 0

        for j in range(x + 1, right + 1):
            if not sight_map[j][i] or (j, i) in warrior:

                if j < n - 1:
                    sight_map[j+1][i+1] = 0

                sight_map[j][i+1] = 0

    coverage = set()
    for i in range(y + 1, N):
        left = max(x - (i - y), 0)
        right = min(N-1, x + (i-y))
        for j in range(left, right + 1):
            if sight_map[j][i]:
                for idx in range(len(warrior)):
                    if warrior[idx] == (j, i):
                        coverage.add(idx)

    if len(stone) < len(coverage):
        stone = coverage
        output = sight_map

    return output, stone

# def stone_area(start, warrior, waypoint):
#     output_view = set()
#     max_stoned = set()
#     for d in range(len(waypoint)-1, -1, -1):
#         tovisit = deque([(start, -1)])
#         visited = set()
#         stoned = set()
#         nogo = set()
#         while tovisit:
#             curr, idv = tovisit.popleft()
#             # visited.add(curr)
#             nowarrior = True
#             for i in range(len(warrior)):
#                 if curr == warrior[i]:
#                     stoned.add(i)
#                     nowarrior = False
#             if nowarrior:
#                 if idv == -1:
#                     for idx, way in enumerate(waypoint[d]):
#                         nx = curr[0] + way[0]
#                         ny = curr[1] + way[1]
#                         if check((nx, ny)) and (nx, ny) not in tovisit:
#                             tovisit.append(((nx, ny), idx))
#                             visited.add((nx, ny))
#                 elif idv == 0:
#                     for idx, way in enumerate(waypoint[d][:2]):
#                         nx = curr[0] + way[0]
#                         ny = curr[1] + way[1]
#                         if check((nx, ny)) and (nx, ny) not in tovisit:
#                             tovisit.append(((nx, ny), idv))
#                             visited.add((nx, ny))
#                 elif idv == 1:
#                     for idx, way in enumerate([waypoint[d][1]]):
#                         nx = curr[0] + way[0]
#                         ny = curr[1] + way[1]
#                         if check((nx, ny)) and (nx, ny) not in tovisit:
#                             tovisit.append(((nx, ny), idv))
#                             visited.add((nx, ny))
#                 elif idv == 2:
#                     for idx, way in enumerate(waypoint[d][1:]):
#                         nx = curr[0] + way[0]
#                         ny = curr[1] + way[1]
#                         if check((nx, ny)) and (nx, ny) not in tovisit:
#                             tovisit.append(((nx, ny), idv))
#                             visited.add((nx, ny))
#             else:
#                 if idv == 0:
#                     output = killall(curr, waypoint[d][:2])
#                     nogo = nogo|output
#                 elif idv == 1:
#                     output = killall(curr, [waypoint[d][1]])
#                     nogo = nogo|output
#                 else:
#                     output = killall(curr, waypoint[d][1:])
#                     nogo = nogo|output

#         # visited.remove(start)
#         for i in range(len(warrior)):
#             if i in stoned and warrior[i] in nogo:
#                 stoned.remove(i)
#         visited -= nogo
#         if len(max_stoned) <= len(stoned):
#             output_view = visited
#             max_stoned = stoned
    
#     return output_view, max_stoned


def killall(start, waypoint):
    tovisit = deque([start])
    visited = set()
    while tovisit:
        curr = tovisit.popleft()
        visited.add(curr)
        for idx, way in enumerate(waypoint):
            nx = curr[0] + way[0]
            ny = curr[1] + way[1]
            if check((nx, ny)) and (nx, ny) not in visited:
                tovisit.append((nx, ny))
                visited.add((nx, ny))
    return visited

# setting
n, m = map(int, input().split())

sr, sc, er, ec = map(int, input().split())

warrior = []
temp = list(map(int, input().split()))
for i in range(m):
    warrior.append((temp[2*i], temp[2*i+1]))

status = [1 for _ in range(m)]

board = []
for i in range(n):
    board.append(list(map(int, input().split())))

# 공원 갈 수 있는 경로가 있는지 확인
route = bfs(board, (sr, sc), (er, ec))
cnt = 0
if len(route) == 0:
    print(-1)
else:
    while True:
        movement = 0
        stoned = 0
        attack = 0
        cnt += 1
        # 돌 된 애들 초기화
        
        # 메두사 이동 (메두사가 이동한 칸에 전사가 았으면 사라짐. 최단경로 상 하 좌 우, 경로가 없을수도)
        (sr, sc) = route[cnt]

        # 도착 확인
        if (sr, sc) == (er, ec):
            print(0)
            break

        for i in range(len(warrior)-1, -1, -1):
            if warrior[i] == (sr, sc):
                warrior.pop(i)
                status.pop(i)


        # 시선 (상하좌우, 90도 시야각)
        if len(warrior) > 0: 
            area, stone = stone_area((sr, sc), warrior)
            for idx in stone:
                status[idx] = 0
                stoned += 1

        # 전사들의 이동 상하좌우
        for i in range(len(warrior)-1, -1, -1):
            poped = False
            if status[i]:
                temp = bfs_warrior1(board, warrior[i], (sr, sc), area)
                if temp != None:
                    # 겹치면 공격 ㄱㄱ
                    if temp == (sr, sc):
                        attack += 1
                        warrior.pop(i)
                        status.pop(i)
                        poped =True
                    else:
                        warrior[i] = temp
                    movement += 1
            if not poped:
                if status[i]:
                    temp = bfs_warrior2(board, warrior[i], (sr, sc), area)
                    if temp != None:
                        # 겹치면 공격 ㄱㄱ
                        if temp == (sr, sc):
                            attack += 1
                            warrior.pop(i)
                            status.pop(i)
                        else:
                            warrior[i] = temp
                        movement += 1
        # # 전사들의 이동 좌우상하
        # for i in range(len(warrior)-1, -1, -1):
        #     if status[i]:
        #             temp = bfs_warrior2(board, warrior[i], (sr, sc), area)
        #             if temp != None:
        #                 # 겹치면 공격 ㄱㄱ
        #                 if temp == (sr, sc):
        #                     attack += 1
        #                     warrior.pop(i)
        #                     status.pop(i)
        #                 else:
        #                     warrior[i] = temp
        #                 movement += 1
        # # 전사들의 공격 (같은 칸에 메두사 있으면 공격 후 전사 사라짐)
        # for m in range(len(warrior)-1, -1, -1):
        #     if warrior[m] == (sr, sc):
        #         attack += 1
        #         warrior.pop(m)
        # print 전사이동합 돌이된 전사의 수 메두사를 공격한 전사의 수
        print(movement, stoned, attack)
        status = [1 for _ in range(len(warrior))]