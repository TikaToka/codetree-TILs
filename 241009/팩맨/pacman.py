pdx = (-1, 0, 1, 0)
pdy = (0, -1, 0, 1)

def countMonster(node):
    cnt = 0
    where = []
    for i in range(len(monster)):
        if monster[i] == node:
            cnt += 1
            where.append(monster[i])
    return cnt, where

def check(node):
    (x, y) = node
    return 1<=x<5 and 1<=y<5

# replicate
m, t = map(int, input().split())
px, py = map(int, input().split())

monster = []
mWay = []

egg = []
eWay = []

dead = []
dTime = []

mdx = (-1, -1, 0, 1, 1, 1, 0, -1)
mdy = (0, -1, -1, -1, 0, 1, 1, 1)

cBoard = [[0 for _ in range(5)] for _ in range(5)]

for i in range(m):
    r, c, d = map(int, input().split())
    monster.append((r, c))
    cBoard[r][c] += 1
    mWay.append(d-1)

for turn in range(t):
    # print(turn, 'turn')
    # print('turn',  turn)
    # egg
    for i in range(len(monster)):
        egg.append(monster[i])
        eWay.append(mWay[i])

    # print([row[1:] for row in cBoard[1:]])
    # print(mWay)
    # print(dead)
    

    for i in range(len(monster)):
        (x, y) = monster[i]
        for d in range(8):
            nx, ny = x + mdx[(mWay[i] + d) % 8], y + mdy[(mWay[i] + d) % 8]
            if check((nx, ny)) and (nx, ny) != (px, py) and (nx, ny) not in dead: # 안벗어났거나 팩맨 없음 시체없음
                cBoard[x][y] -= 1
                monster[i] = (nx, ny)
                cBoard[nx][ny] += 1
                mWay[i] = (mWay[i] + d) % 8
                break
    # print(mWay)
    # print("AA")
    # print([row[1:] for row in cBoard[1:]])

    maxval = -1
    pMove = [-1, -1, -1]
    for a in range(4):
        ax, ay = px + pdx[a], py + pdy[a]
        if not check((ax, ay)):
            continue
        temp = cBoard[ax][ay]
        for b in range(4):
            bx, by = ax + pdx[b], ay + pdy[b]
            if not check((bx, by)):
                continue
            bb = cBoard[bx][by]
            temp += bb
            for c in range(4):
                cx, cy = bx + pdx[c], by + pdy[c]
                if not check((cx, cy)):
                    continue
                if (cx, cy) != (ax, ay):
                    cc = cBoard[cx][cy]
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
        where = countMonster((px, py))[1]
        for j in range(len(monster)-1, -1, -1):
            if monster[j] == (px, py):
                monster.pop(j)
                mWay.pop(j)
                cBoard[px][py] -= 1
                dead.append((px, py))
                dTime.append(-3)

    # print(egg)
    # print([row[1:] for row in cBoard[1:]])

    # print(px, py)

    # hatch
    monster += egg
    mWay += eWay
    for (x, y) in egg:
        cBoard[x][y] += 1
    egg = []
    eWay = []

    # trash
    for i in range(len(dead)-1, -1, -1):
        dTime[i] +=1
        if dTime[i] == 0:
            dTime.pop(i)
            dead.pop(i)

    # print(dead)
    # print(monster)
    # print(mWay)

print(len(monster))

# a b c d e f g h

# h d c f b a e g

# h d f g