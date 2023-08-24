import math

def reverse(num):
    return int(str(num)[::-1])

def count_appearances(A, B):
    count = 0
    row = 1
    while True:
        value = row
        col = 1
        while True:
            if A <= value and value <= B:
                count += 1
            next_value = value + reverse(value)
            if next_value > B or next_value < A:
                break
            value = next_value
            col += 1
        row += 1
        if reverse(row) >= B:
            break
    return count

Q = int(input())

for _ in range(Q):
    A, B = map(int, input().split())
    print(count_appearances(A, B))