s = input()
r, b, y, g = 0, 0, 0, 0
for c in s:
    if c == '!':
        if s[s.index(c)-1] == 'R':
            r += 1
        elif s[s.index(c)-1] == 'B':
            b += 1
        elif s[s.index(c)-1] == 'Y':
            y += 1
        elif s[s.index(c)-1] == 'G':
            g += 1
print(r, b, y, g)
