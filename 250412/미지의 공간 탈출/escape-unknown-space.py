from collections import deque

dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)


def check(node, t):
    return 0<=node[0]<t and 0<=node[1]<t

def bfs3d(s, fin):
    tovisit = deque([s])
    visited = {s: None}
    while tovisit:
        curr = tovisit.popleft()
        if curr == fin:
            path = [curr]
            node = curr
            while node:
                path.append(visited[node])
                node = visited[node]
            return path[::-1][1:]
        for d in range(4):
            nx = curr[0] + dx[d]
            ny = curr[1] + dy[d]
            if check((nx, ny), 3 * m):
                # 북 동 / 동 북
                if 0<= nx < m and 2*m <= ny < 3*m:
                    nx, ny = (3* m - 1) - curr[1], (3*m -1) - curr[0]
                    if board3d[nx][ny] != 1 and (nx, ny) not in visited:
                        tovisit.append((nx, ny))
                        visited[(nx, ny)] = curr
                # 서 남 / 남 서
                elif 2 * m <= nx < 3 * m and 0 <= ny < m:
                    nx, ny = (3* m  - 1) - curr[1], (3*m -1) - curr[0]
                    if board3d[nx][ny] != 1 and (nx, ny) not in visited:
                        tovisit.append((nx, ny))
                        visited[(nx, ny)] = curr
                # 북 서 / 서 북
                elif 0 <= nx < m and 0 <= ny < m:
                    nx, ny = curr[1], curr[0]
                    if board3d[nx][ny] != 1 and (nx, ny) not in visited:
                        tovisit.append((nx, ny))
                        visited[(nx, ny)] = curr
                # 남 동 / 동 남
                elif 2*m <= nx < 3*m and 2*m <= ny < 3 * m:
                    nx, ny = curr[1], curr[0]
                    if board3d[nx][ny] != 1 and (nx, ny) not in visited:
                        tovisit.append((nx, ny))
                        visited[(nx, ny)] = curr
                #연결된 부분
                else:
                    if board3d[nx][ny] != 1 and (nx, ny) not in visited:
                        tovisit.append((nx, ny))
                        visited[(nx, ny)] = curr


def bfs2d(s, e):
    tovisit = deque([s])
    visited = {s: None}
    while tovisit:
        curr = tovisit.popleft()
        if curr == e:
            path = [curr]
            node = curr
            while node:
                path.append(visited[node])
                node = visited[node]
            return path[::-1][1:]
        for d in range(4):
            nx = curr[0] + dx[d]
            ny = curr[1] + dy[d]
            if check((nx, ny), n) and board2d[nx][ny] in [0, 4] and (nx, ny) not in visited:
                tovisit.append((nx, ny))
                visited[(nx, ny)] = curr
    return []

def find2dexit():
    for i in range(n):
        for j in range(n):
            if board2d[i][j] == 3:
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dx[d]
                    if check((nx, ny), n) and board2d[nx][ny] == 0:
                        return (nx, ny)

def exitto3d(exit2d):
    for d in range(4):
        nx = exit2d[0] + dx[d]
        ny = exit2d[1] + dy[d]
        if check((nx, ny), n) and board2d[nx][ny] == 3:
            if d == 0: # 서쪽 출구
                return (m + nx - edge[0], 0)
            elif d==1: # 동쪽 출구
                return(m + nx - edge[0] , 3*m-1)
            elif d==2: # 북쪽 출구
                return(0, m + ny - edge[1])
            else: # 남쪽출구
                return (3*m-1, m + ny - edge[1])

# 인풋 정리
n, m, f = map(int, input().split())
start = ()
goal = ()
edge = ()
answer = 0

board2d = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        board2d[i][j] = temp[j]
        if temp[j] == 4:
            goal = (i, j)
        elif temp[j] == 3:
            if edge == ():
                edge = (i, j)

(ex2d, ey2d)= find2dexit()
(ex3d, ey3d) = exitto3d((ex2d, ey2d))

board3d = [[0 for _ in range(3*m)] for _ in range(3*m)]
# 동@@
for i in range(2*m, 3*m):
    temp = list(map(int, input().split()))
    cnt = 0
    for j in range(2*m-1, m-1, -1):
        board3d[j][i] = temp[cnt]
        cnt += 1
# 서@@
for i in range(m-1, -1, -1):
    temp = list(map(int, input().split()))
    cnt = 0
    for j in range(m, 2*m):
        board3d[j][i] = temp[cnt]
        cnt += 1
# 남
for i in range(2*m, 3 * m):
    temp = list(map(int, input().split()))
    for j in range(m, 2*m):
        board3d[i][j] = temp[j-m]

# 북 @@
for i in range(m-1, -1, -1):
    temp = list(map(int, input().split()))
    cnt = 0
    for j in range(2*m-1, m-1, -1):
        board3d[i][j] = temp[cnt]
        cnt += 1

# 위
for i in range(m, 2 * m):
    temp = list(map(int, input().split()))
    for j in range(m, 2*m):
        board3d[i][j] = temp[j-m]
        if temp[j-m] == 2:
            start = (i, j)

fire = [[] for _ in range(f)]
for i in range(f):
    r, c, v, d = list(map(int, input().split()))
    board2d[r][c] = -1
    fire[i] = [r, c, v, d]

###################
current = start
# 3차원 탈출경로 확인
route3d = bfs3d(start, (ex3d, ey3d))

cnt = 1
#3d 탈출 전
fail = False
while cnt < len(route3d):
    # 확신 (독립적)
    for fi in fire:
        if cnt % fi[3] == 0:
            d = fi[2]
            nx = fi[0] + dx[d]
            ny = fi[1] + dy[d]
            if check((nx, ny), n) and board2d[nx][ny] not in [1, 3, 4]:
                board2d[nx][ny] = -1
                fi[0] = nx
                fi[1] = ny

    if board2d[ex2d][ey2d] == -1:
        print(-1)
        fail = True
        break
    # 이동
    current = route3d[cnt]
    cnt += 1
    answer += 1
    
if not fail:
    # 3d to 2d
    for fi in fire:
        if cnt % fi[3] == 0:
            d = fi[2]
            nx = fi[0] + dx[d]
            ny = fi[1] + dy[d]
            if check((nx, ny), n) and board2d[nx][ny] not in [1, 4]:
                board2d[nx][ny] = -1
                fire[0] = nx
                fire[1] = ny
    
    if board2d[ex2d][ey2d] == -1:
        print(-1)
        fail = True
    
    current = (ex2d, ey2d)
    cnt += 1
    answer += 1


    done = False

    board2d_bkup = board2d[:]
    cnt_bkup = cnt
    answer_bkup = answer
    fire_bkup = fire

    while not done:
        current = (ex2d, ey2d)
        route2d = bfs2d((ex2d, ey2d), goal)
        board2d = board2d_bkup
        cnt = cnt_bkup
        fire = fire_bkup
        mv = 1
        answer = answer_bkup
        while True:
            # 확산
            for fi in fire:
                if cnt % fi[3]== 0:
                    d = fi[2]
                    nx = fi[0] + dx[d]
                    ny = fi[1] + dy[d]
                    if check((nx, ny), n) and board2d[nx][ny] not in [1, 4]:
                        board2d[nx][ny] = -1
                        fi[0] = nx
                        fi[1] = ny
            # 이동
            nx, ny = route2d[mv]
            if board2d[nx][ny] != -1:
                current = route2d[mv]
                answer += 1
            else:
                break

            if current == goal:
                done = True
                break
            cnt += 1
            mv += 1
    print(answer)
