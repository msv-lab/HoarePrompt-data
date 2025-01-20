n = int(input().strip())
s = input().strip()
moves = (n - 11) // 2
count_8 = s[:n - 11].count('8')
if count_8 > moves:
    print('YES')
else:
    print('NO')