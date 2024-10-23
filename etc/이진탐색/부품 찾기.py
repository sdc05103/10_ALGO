import sys
input = sys.stdin.readline

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end)//2 

        if array[mid] == target:
            return mid
    
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
        
    return None


N = int(input())
items = list(map(int, input().split()))

M = int(input())
request = list(map(int, input().split()))

items.sort()

for i in request:
    result = binary_search(items, i, 0, N-1)

    if result != None:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')

