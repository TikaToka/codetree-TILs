pdx = (-1, 0, 1, 0)
pdy = (0, -1, 0, 1)

def tcountMonster(node):
    cnt = 0
    where = []
    for i in range(len(monster)):
        if monster[i] == node and tActivate[i] == 2:
            cnt += 1
            where.append(i)
    return cnt, where

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

board = [[0 for _ in range(5)] for _ in range(5)]

# replicate
m, t = map(int, input().split())
px, py = map(int, input().split())

monster = []
mWay = []
activate = [] # 1 live # 0 egg # -1 dead
mdx = (-1, -1, 0, 1, 1, 1, 0, -1)
mdy = (0, -1, -1, -1, 0, 1, 1, 1)

for i in range(m):
    r, c, d = map(int, input().split())
    monster.append((r, c))
    mWay.append(d-1)
    activate.append(2) # live


# print(monster)
# print(activate)

for turn in range(t):
    # print('turn',  turn)
    # egg
    for i in range(len(monster)):
        if activate[i] == 2:
            monster.append(monster[i])
            mWay.append(mWay[i])
            activate.append(1) 
    for i in range(len(monster)):
        done = False
        if activate[i] == 2: # 살아있는 것만
            (x, y) = monster[i]
            for d in range(8):
                nx, ny = x + mdx[(mWay[i] + d) % 8], y + mdy[(mWay[i] + d) % 8]
                if check((nx, ny)) and (nx, ny) != (px, py): # 안벗어났거나 팩맨 없음
                    for j in range(len(monster)): # 시체 없음
                        if not (monster[j] == (nx, ny) and activate[j] < 0 ):
                            monster[i] = (nx, ny)
                            mWay[i] = (mWay[i] + d) % 8
                            done = True
                            break
                if done:
                    break

    # print(monster)
    # print(activate)

    # pacman move
    maxval = -1
    pMove = [-1, -1, -1]
    for a in range(4):
        ax, ay = px + pdx[a], py + pdy[a]
        if not check((ax, ay)):
            continue
        temp = countMonster((ax, ay))[0]
        for b in range(4):
            bx, by = ax + pdx[b], ay + pdy[b]
            if not check((bx, by)):
                continue
            # if (bx, by) != (px, py):
            #     temp += countMonster((bx, by))[0]
            temp += countMonster((bx, by))[0]
            for c in range(4):
                cx, cy = bx + pdx[c], by + pdy[c]
                if not check((cx, cy)):
                    continue
                if (cx, cy) not in [(ax, ay), (bx, by)]:
                    temp += countMonster((cx, cy))[0]
                # temp += countMonster((cx, cy))[0]
                if temp > maxval:
                    maxval = temp
                    pMove = [a, b, c]
                if (cx, cy) not in [(ax, ay), (bx, by)]:
                    temp -= countMonster((cx, cy))[0]
                # if (cx, cy) != (px, py):
                #     temp -= countMonster((cx, cy))[0]
                # temp -= countMonster((cx, cy))[0]
            # if (bx, by) != (px, py):
            #     temp -= countMonster((bx, by))[0]
            temp -= countMonster((bx, by))[0]

    # print(pMove)

    for i in pMove:
        px += pdx[i]
        py += pdy[i]
        where = countMonster((px, py))[1]
        for w in where:
            activate[w] = -3

    # print(px, py)
    
    # print(monster)
    # print(activate)

    # hatch and remain 
    for i in range(len(monster)):
        if activate[i] == 1:
            activate[i] = 2
        elif activate[i] < 0: # 시체 생명
            activate[i] += 1

    # print(monster)
    # print(activate)


answer = 0
for i in activate:
    if i == 2:
        answer += 1

print(answer)