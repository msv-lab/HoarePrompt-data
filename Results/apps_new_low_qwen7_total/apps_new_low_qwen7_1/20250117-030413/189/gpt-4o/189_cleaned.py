input = sys.stdin.read
data = input().split()
n = int(data[0])
k = int(data[1])
groups = list(map(int, data[2:]))
max_pairs_per_row = 4 * n
total_pairs_needed = 0
for soldiers in groups:
    total_pairs_needed += (soldiers + 1) // 2
if total_pairs_needed <= max_pairs_per_row:
    print('YES')
else:
    print('NO')