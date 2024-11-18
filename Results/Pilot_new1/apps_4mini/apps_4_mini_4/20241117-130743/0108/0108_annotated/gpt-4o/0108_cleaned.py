s = input()
target = 'abcdefghijklmnopqrstuvwxyz'
target_len = len(target)
(i, j) = (0, 0)
while i < len(s) and j < target_len:
    if s[i] == target[j]:
        j += 1
    i += 1
if j == target_len:
    print(target)
else:
    print(-1)