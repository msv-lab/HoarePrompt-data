s = raw_input()
n = 100
letters = {}
for x in s:
    if x in letters:
        letters[x] += 1
    else:
        letters[x] = 1

s = ''
for x in letters:
    if letters[x] > 1:
        s += x * (letters[x] / 2)
    if len(s) == n / 2:
        break

if len(s) == n / 2:
    print(s + s[::-1])
else:
    for x in letters:
        if letters[x] % 2:
            s += x
            break
    print(s + s[:-1][::-1])
