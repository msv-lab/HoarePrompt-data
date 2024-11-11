(n, m, k) = map(int, input().split())
(a, b) = map(int, input().split())
a_floor = (a - 1) % m + 1
a_block = (a - 1) // (m * k) + 1
b_floor = (b - 1) % m + 1
b_block = (b - 1) // (m * k) + 1
min_block_time = min(abs(a_block - b_block), n - abs(a_block - b_block)) * 15
if a_floor > b_floor:
    min_floor_time = (a_floor - b_floor) * 5 + 10
else:
    min_floor_time = (b_floor - a_floor) * 5 + 10
print(min_block_time + min_floor_time)