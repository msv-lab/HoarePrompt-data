N = int(raw_input())
A = list(map(int, raw_input().split(' ')))

cnt = 0
for a in A:
    cnt += 1 if a & 1 == 1 else 0

print('YES' if cnt % 2 == 0 else 'NO')