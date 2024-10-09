import copy

pdx = (-1, 0, 1, 0)
pdy = (0, -1, 0, 1)

def check(node):
    (x, y) = node
    return 1<=x<5 and 1<=y<5

# replicate
m, t = map(int, input().split())
px, py = map(int, input().split())

monster = [[[] for _ in range(5)] for _ in range(5)]

dead = [[[] for _ in range(5)] for _ in range(5)]


mdx = (-1, -1, 0, 1, 1, 1, 0, -1)
mdy = (0, -1, -1, -1, 0, 1, 1, 1)

for i in range(m):
    r, c, d = map(int, input().split())
    monster[r][c].append(d-1)
    # cBoard[r][c] += 1
    # mWay.append(d-1)

for turn in range(t):
    # print(turn, 'turn')
    # egg
    egg = copy.deepcopy(monster)
    egg = [[[] for _ in range(5)] for _ in range(5)]
    for i in range(1, 5):
        for j in range(1, 5):
            egg[i][j] = monster[i][j][:]

    temp = [[[] for _ in range(5)] for _ in range(5)]

    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(len(monster[i][j])-1, -1, -1):
                for d in range(8):
                    nx, ny = i + mdx[(monster[i][j][k] + d) % 8], j + mdy[(monster[i][j][k] + d) % 8]
                    if check((nx, ny)) and (nx, ny) != (px, py) and len(dead[nx][ny]) == 0: # 안벗어났거나 팩맨 없음 시체없음
                        temp[nx][ny].append((monster[i][j][k] + d) % 8)
                        monster[i][j].pop(k)
                        break

    for i in range(1, 5):
        for j in range(1, 5):
            monster[i][j] += temp[i][j]
    # print(mWay)

    maxval = -1
    pMove = [-1, -1, -1]
    for a in range(4):
        ax, ay = px + pdx[a], py + pdy[a]
        if not check((ax, ay)):
            continue
        temp = len(monster[ax][ay])
        for b in range(4):
            bx, by = ax + pdx[b], ay + pdy[b]
            if not check((bx, by)):
                continue
            bb = len(monster[bx][by])
            temp += bb
            for c in range(4):
                cx, cy = bx + pdx[c], by + pdy[c]
                if not check((cx, cy)):
                    continue
                if (cx, cy) != (ax, ay):
                    cc = len(monster[cx][cy])
                    temp += cc
                if temp > maxval:
                    maxval = temp
                    pMove = [a, b, c]
                if (cx, cy) != (ax, ay):
                    temp -= cc
            temp -= bb

    # print(pMove)
    #kill
    for i in pMove:
        px += pdx[i]
        py += pdy[i]
        dead[px][py].extend([-3 for _ in range(len(monster[px][py]))])
        monster[px][py] = []

    # print(egg)
    # print([row[1:] for row in cBoard[1:]])

    # print(px, py)
    # print('egg', [row[1:] for row in egg[1:]])
    # hatch
    for i in range(1, 5):
        for j in range(1, 5):
            monster[i][j].extend(egg[i][j])
        
    # trash
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(len(dead[i][j])-1, -1, -1):
                dead[i][j][k] += 1
                if dead[i][j][k] == 0:
                    dead[i][j].pop(k)

    # print([row[1:] for row in dead[1:]])
    # print('.')
    # print([row[1:] for row in monster[1:]])
answer = 0
for i in range(1, 5):
    for j in range(1, 5):
        answer += len(monster[i][j])

print(answer)