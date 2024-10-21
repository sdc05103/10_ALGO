import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
firstMax = data[-1]
secondMax = data[-2]
sum = 0

while True:
    for i in range(K):
        if M == 0:
            break
        
        sum += firstMax
        M -= 1
    
    if M == 0:
        break

    sum += secondMax
    M -= 1

print(sum)
    
    
