def dfs(graph, start, exits):
    tovisit = []
    visited = set()
    row = 0
    tovisit.append(start)
    iterate = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    while tovisit:
        node = tovisit.pop()
        visited.add((node[0], node[1]))
        row = max(row, node[0])
        if row == len(graph):
            return row
        for dx, dy in iterate:
            tempx, tempy = node[0] + dx, node[1] + dy
            if not (0 <= tempx < r and 0 <= tempy < c):
                continue
            if (node[0], node[1]) in exits:
                if graph[tempx][tempy] != graph[node[0]][node[1]] and  graph[tempx][tempy] != 0 and (tempx, tempy) not in visited:
                    tovisit.append([tempx, tempy])
                elif graph[tempx][tempy] == graph[node[0]][node[1]] and (tempx, tempy) not in visited:
                    tovisit.append([tempx, tempy])
            else:
                if graph[tempx][tempy] == graph[node[0]][node[1]] and (tempx, tempy) not in visited:
                    tovisit.append([tempx, tempy])
    return row + 1

def check(curr, look, graph):
    if look == [1, 0]: # S
        todo = [[1, 0], [0, 1], [0, -1]]
    elif look == [0, -1]: # W
        todo = [[1, 0], [0, -1], [-1, 0]]
    elif look == [0, 1]: # E
        todo = [[1, 0], [0, 1], [-1, 0]]
    for dx, dy in todo:
        tx, ty = (curr[0] + dx, curr[1] + dy)
        if tx < 0:
            continue
        if not (tx < r and 0 <= ty < c):
            return False
        elif graph[tx][ty] != 0:
            return False
    return True


answer = 0
r, c, k = map(int, input().split())
graph = [[0 for _ in range(c)] for _ in range(r)]
exits = set()
for v, i in enumerate(range(k)):
    ci, di = map(int, input().split())
    curr = [-2, ci-1]
    look = [1, 0]
    while True:
        if curr[0] == r-2:
            break
        # S
        cand = [a + b for a, b in zip(curr, look)]
        if check(cand, look, graph):
            curr = cand
        else: # W
            look = [0, -1]
            cand = [a + b for a, b in zip(curr, look)]
            if check(cand, look, graph):
                # S
                look = [1, 0]
                cand = [a + b for a, b in zip(cand, look)]
                if check(cand, look, graph):
                    curr = cand
                    di = di - 1 if di - 1 >= 0  else di + 3
                else: # E
                    look = [0, 1]
                    cand = [a + b for a, b in zip(curr, look)]
                    if check(cand, look, graph):# S
                        look = [1, 0]
                        cand = [a + b for a, b in zip(cand, look)]
                        if check(cand, look, graph):
                            curr = cand
                            di = di + 1 if di + 1 < 4 else di - 3
                        else:
                            break
                    else:
                        break
            else: # E
                look = [0, 1]
                cand = [a + b for a, b in zip(curr, look)]
                if check(cand, look, graph):# S
                    look = [1, 0]
                    cand = [a + b for a, b in zip(cand, look)]
                    if check(cand, look, graph):
                        curr = cand
                        di = di + 1 if di + 1 < 4 else di -3
                    else:
                        break
                else:
                    break

    x, y = curr
    # print(x+1, y+1, di)
    test = True
    for idx, (dx, dy) in enumerate([[-1, 0], [0, 1], [1, 0], [0, -1], [0, 0]]):
        tempx , tempy = (x + dx, y + dy)
        if not (0 <= x + dx < r and 0 <= y + dy < c):
            graph = [[0 for _ in range(c)] for _ in range(r)]
            exits = set()
            test = False
            break
        if idx == di:
            exit = [tempx, tempy]
            exits.add((exit[0], exit[1]))
        graph[tempx][tempy] = v+1
    if test:
        answer += dfs(graph, exit, exits)

print(answer)