import sys

input = sys.stdin.readline
N, M = map(int, input().split())

result = []

for i in range(N):
    data = list(map(int, input().split()))
    minValue = min(data)
    result.append(minValue)

answer = max(result)

print(answer)
