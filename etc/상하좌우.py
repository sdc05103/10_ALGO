import sys
input = sys.stdin.readline

N = int(input())
x, y = 1, 1 # 현재 위치
plans = input().split()

dx = [0, 0, -1, 1] 
dy = [-1, 1, 0, 0]

moves = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(moves)): # 각각의 움직임 확인
        if plan == moves[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > N or ny > N:    # 경계를 벗어나면 반영x 
        continue

    x, y = nx, ny

print(x, y)