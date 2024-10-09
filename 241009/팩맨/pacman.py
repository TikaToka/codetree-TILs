pdx = (-1, 0, 1, 0)
pdy = (0, -1, 0, 1)

def countMonster(node):
    cnt = 0
    where = []
    for i in range(len(monster)):
        if monster[i] == node and activate[i] == 2:
            cnt += 1
            where.append(i)
    return cnt, where

def check(node):
    (x, y) = node
    return 1<=x<5 and 1<=y<5

# replicate
m, t = map(int, input().split())
px, py = map(int, input().split())

monster = []
mWay = []
activate = []

egg = set()

dead = set()

mdx = (-1, -1, 0, 1, 1, 1, 0, -1)
mdy = (0, -1, -1, -1, 0, 1, 1, 1)

cBoard = [[0 for _ in range(5)] for _ in range(5)]

for i in range(m):
    r, c, d = map(int, input().split())
    monster.append((r, c))
    cBoard[r][c] += 1
    mWay.append(d-1)
    activate.append(2) # live


for turn in range(t):
    # print('turn',  turn)
    # egg
        
    for i in range(len(monster)):
        if activate[i] == 2:
            monster.append(monster[i])
            mWay.append(mWay[i])
            activate.append(1) 

    for i in range(len(monster)):
        if activate[i] == 2: # 살아있는 것만
            done = False
            (x, y) = monster[i]
            for d in range(8):
                nx, ny = x + mdx[(mWay[i] + d) % 8], y + mdy[(mWay[i] + d) % 8]
                if check((nx, ny)) and (nx, ny) != (px, py): # 안벗어났거나 팩맨 없음
                    thereis = False
                    for j in range(len(monster)): # 시체 없음
                        if i != j: # 같은 놈은 고려 안하기
                            if monster[j] == (nx, ny): # 이동 한 좌표 같은데서 
                                if activate[j] < 0: # 좀비가 있으면
                                    thereis = True
                        # if not (i != j and monster[j] == (nx, ny) and activate[j] < 0 ):
                        #     print(nx,ny)
                    if not thereis:
                        cBoard[monster[i][0]][monster[i][1]] -= 1
                        monster[i] = (nx, ny)
                        cBoard[nx][ny] += 1
                        mWay[i] = (mWay[i] + d) % 8
                        done = True

                if done:
                    break

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
                # temp += countMonster((cx, cy))[0]
                if temp > maxval:
                    maxval = temp
                    pMove = [a, b, c]
                if (cx, cy) != (ax, ay):
                    temp -= cc
            temp -= bb

    # print(pMove)

    for i in pMove:
        px += pdx[i]
        py += pdy[i]
        where = countMonster((px, py))[1]
        for w in where:
            activate[w] = -3
            cBoard[monster[w][0]][monster[w][1]] -= 1
    

    # hatch and remain 
    for i in range(len(monster)-1, -1, -1):
        if activate[i] == 1:
            activate[i] = 2
            cBoard[monster[i][0]][monster[i][1]] += 1
        elif activate[i] < 0: # 시체 생명
            activate[i] += 1
            if activate[i] == 0:
                monster.pop(i)
                activate.pop(i)
                mWay.pop(i)



answer = 0
for i in activate:
    if i == 2:
        answer += 1

print(answer)

# a b c d e f g h

# h d c f b a e g

# h d f g