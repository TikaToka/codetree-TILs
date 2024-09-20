n = int(input())
numbers = input().split()

numbers = [int(x) for x in numbers]
answer = sum(numbers * n)
for i in range(n):
    temp = 0
    for j in range(n):
        temp += abs(j-i) * numbers[j]

    answer  = min(answer, temp)

print(answer)