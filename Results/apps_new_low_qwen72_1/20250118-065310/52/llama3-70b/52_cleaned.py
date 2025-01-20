t = input()
for i in range(1, len(t)):
    if t[i:] == t[:len(t) - i]:
        print('YES')
        print(t[:len(t) - i])
        exit()
print('NO')