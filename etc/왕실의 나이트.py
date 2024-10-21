import sys
input = sys.stdin.readline

location = input()
row = int(location[1])
col = int(ord(location[0])) - int(ord('a')) + 1
result = 0

move = [(-1, -2), (-2, -1),  (-1, +2), (-2, +1), (+1, -2), (+2, -1), (+1, +2), (+2, +1)]

for i in move:
    nextRow = row + i[0]
    nextCol = col + i[1]

    if nextRow >= 1 and nextRow <= 8 and nextCol >= 1 and nextCol <= 8:
        result += 1
    
print(result)
        