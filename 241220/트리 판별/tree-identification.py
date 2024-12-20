MAX_N = 10000

# 변수 선언 및 입력:
m = int(input())
root = 0
deg = [0] * (MAX_N + 1)
edges = [[] for _ in range(MAX_N + 1)]
used = [False] * (MAX_N + 1)
visited = [False] * (MAX_N + 1)
is_tree = True

# n개의 간선 정보를 입력받습니다.
for _ in range(m):
    x, y = tuple(map(int, input().split()))

    # 간선 정보를 인접리스트에 넣어줍니다.
    edges[x].append(y)

    # 해당 번호가 그래프에 있는 정점 번호인지 판단합니다.
    used[x] = True
    used[y] = True

    # 정점 별 들어오는 간선의 개수를 저장합니다.
    deg[y] += 1


# DFS를 통해 루트로부터 갈 수 있는 모든 정점을 탐색합니다.
def dfs(x):
    for y in edges[x]:
        # 이미 방문한 노드는 스킵합니다.
        if visited[y]: 
            continue

        visited[y] = True  
        dfs(y)

    return


# 루트 노드를 찾습니다. 들어오는 간선이 하나도 없는 노드가 여러개면 트리가 아닙니다.
for i in range(1, MAX_N + 1):
    if used[i] and deg[i] == 0:
        # 이미 선정된 루트가 있다면 
        # 루트가 여러 개인 것이므로 트리가 아닙니다.
        if root != 0: 
            is_tree = False
        root = i

# 루트 노드가 없으면 트리가 아닙니다.
if root == 0: 
    is_tree = False

# 루트 노드를 제외한 노드는 모두 들어오는 간선이 1개씩 있습니다. 그렇지 않으면 트리가 아닙니다.
for i in range(1, MAX_N + 1):
    if used[i] and i != root and deg[i] != 1:
        is_tree = False

if is_tree and root != 0:
    # root 정점으로부터 모든 정점을 갈 수 있는지 판단합니다.
    visited[root] = True
    dfs(root)

# root 정점으로부터 탐색해 도달하지 못하는 정점이 있으면 트리가 아닙니다.
for i in range(1, MAX_N + 1):
    if used[i] and not visited[i]:
        is_tree = False

if is_tree: 
    print(1)
else:
    print(0)