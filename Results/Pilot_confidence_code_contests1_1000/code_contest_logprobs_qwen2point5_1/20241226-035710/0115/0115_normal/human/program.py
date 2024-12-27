n = input()
s = raw_input()
s += "#"

ans = []
tmp = [s[0]]
for i in range(n + 1):
    if (i == 0):
        continue
    if (s[i] != s[i - 1]):
        if (tmp[0] == "a" or tmp[0] == "e" or tmp[0] == "i" or tmp[0] == "o" or tmp[0] == "u" or tmp[0] == "y"):
            if ((tmp[0] == "e" or tmp[0] == "o") and len(tmp) == 2):
                ans.extend(tmp)
            else:
                ans.append(tmp[0])
        else:
            ans.extend(tmp)
        tmp = [s[i]]
    else:
        tmp.append(s[i])

print(''.join(ans))
