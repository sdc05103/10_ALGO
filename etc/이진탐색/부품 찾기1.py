import sys
input = sys.stdin.readline

N = int(input())
items = list(map(int, input().split()))

M = int(input())
request = list(map(int, input().split()))

flag = True

for i in range(M):
    for j in range(N):
        if items[j] == request[i]:
            flag = True
            print("yes", end = " ")
            break
        else:
            flag = False
            continue
    if flag == False:
        print("no", end = " ")
