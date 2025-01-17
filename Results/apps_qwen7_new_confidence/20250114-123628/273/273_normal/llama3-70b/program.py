s = input()
t = input()
n = len(s)

if s == t:
    print(0)
elif any(s.count(ch) != t.count(ch) for ch in set(s)):
    print(-1)
else:
    used = set()
    res = []
    for x, y in zip(s, t):
        if x != y and x not in used and y not in used:
            used.add(x)
            used.add(y)
            res.append(' '.join(sorted(x + y)))
        elif x != y:
            print(-1)
            break
    else:
        print(len(res))
        print('\n'.join(res))