answer = 0
N = int(input())
cows = [int(x) for x in input().split()]
for i in range(N):
    for j in range(i+1, N):
        if cows[i] <= cows[j]:
            for k in range(j+1, N):
                if cows[j] <= cows[k]:
                    answer += 1
print(answer)