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
            if A <= value <= B:
                count += 1
            next_value = value + reverse(value)
            if next_value > B:
                break
            value = next_value
            col += 1
        row += 1
        if reverse(row) > B:
            break
    return count

Q = int(input())
queries = []
for _ in range(Q):
    A, B = map(int, input().split())
    queries.append((A, B))

for A, B in queries:
    print(count_appearances(A, B))