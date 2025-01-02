from sys import stdin

rints = lambda: [int(x) for x in stdin.readline().split()]
rstr = lambda: list(stdin.readline().strip())

n, k = rints()
s = rstr()

for i, j in enumerate(s[:-1]):
    if not k:
        break

    if ''.join(s[i:i + 2]) == '47':
        tem = '77' if i % 2 else '44'

        if tem == '44':
            if i < len(s) - 2 and s[i + 2] == '7':
                s[i:i + 3] = ['4', '4', '7'] if k % 2 else ['4', '7', '7']
                k = 0
            else:
                k -= 1
                s[i:i + 2] = ['4', '4']

        else:
            if i and s[i - 1] == '4':
                s[i - 1:i + 2] = ['4', '7', '7'] if k % 2 else ['4', '4', '7']
                k = 0
            else:
                k -= 1
                s[i:i + 2] = ['7', '7']

print(''.join(s))
