def dist(cord1, cord2):
    return abs(cord1[0]-cord2[0]) + abs(cord1[1] - cord2[1]) <= 3

def check(cord, n):
    return 0 < cord[0] <= n and 0 < cord[1] <= n

answer = 0
n, m, h, k = map(int, input().split(' '))
#runner
runner = []
tree = []
#catcher
catcher = [int(n//2)+1, int(n//2)+1]
tick = 0
multiplier = 1
idx = 0
way = 0
tickmove =[[(-1, 0), (0, 1), (1, 0), (0, -1)], [(1, 0), (0, 1), (-1, 0), (0, -1)]]
# Setting
for i in range(m):
    x, y, d= map(int, input().split())
    if d == 1:
        runner.append([[x, y], [0, 1]])
    elif d == 2:
        runner.append([[x, y], [1, 0]])

for i in range(h):
    x, y= map(int, input().split())
    tree.append([x, y])

# for each turn 
for i in range(k):
    # runner
    for run in runner:
        # under 3
        if dist(catcher, run[0]):
            temp = [a + b for a, b in zip(run[0], run[1])]
            # out of grid
            if not check(temp, n):
                run[1] = [x * -1 for x in run[1]]
                temp = [a + b for a, b in zip(run[0], run[1])]
            if temp != catcher:
                run[0] = temp

    #catcher
    # return check
    if multiplier == n and catcher == [1, 1]:
        way = 1
        idx = 0
    elif multiplier == 1 and catcher == [int(n//2)+1, int(n//2)+1]:
        way = 0
        idx = 0

    temp = [a + b * multiplier for a, b in zip(catcher, tickmove[way][idx])]
    if not check(temp, n):
        mulcam = multiplier - 1
        temp = [a + b * mulcam for a, b in zip(catcher, tickmove[way][idx])]
        if temp == [n, 1]:
            multiplier -= 1
        tick = -1
    catcher = temp    
    
    # set for next catcher move
    tick += 1
    if tick >= 2:
        if way == 0:
            multiplier += 1
        else:
            if multiplier > 1:
                multiplier -= 1
        tick = 0
    idx += 1
    if idx > 3:
        idx -= 4

    #catch
    temp = []
    cand = catcher
    temp.append(cand)

    for _ in range(2):
        cand = [a + b for a, b in zip(cand, tickmove[way][idx])]
        if check(cand, n):
            temp.append(cand)
        else:
            break
    cnt = 0
    # print(catcher, runner, temp)
    for j in range(len(runner)-1, -1, -1):
        if runner[j][0] in temp and runner[j][0] not in tree:
            runner.pop(j)
            cnt += 1
    # print(i+1, cnt)
    answer += (i+1) * cnt

print(answer)