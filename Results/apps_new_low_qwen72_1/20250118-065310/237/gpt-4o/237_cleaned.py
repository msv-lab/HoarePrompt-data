s = input().strip()
pearl_count = s.count('o')
link_count = s.count('-')
if pearl_count == 0 or pearl_count == 1:
    print('YES')
elif link_count % pearl_count == 0:
    print('YES')
else:
    print('NO')