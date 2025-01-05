from sys import stdin
 
 
def place_wizards(r):
    wizards = list(range(n))
    x = 1
    prev_y = 1
    result = [None] * n
    where = [1] * n
    wizards.sort(key=lambda w: -r[w])
    if r[wizards[-1]] == 0:
        w0 = wizards[-1]
        result[w0] = (x, 1)
        where[w0] += w0
        wizards.pop()
        x += 1
        prev_w = w0
    elif n >= 3 and [r[w] for w in wizards[:-4:-1]] == [1, 2, 3]:
        one, two, three = wizards[:-4:-1]
        wizards[-3:] = []
        result[three] = (x, 2)
        result[two] = (x + 1, 1)
        result[one] = (x + 2, 1)
        where[three] += one
        where[two] += three
        where[one] += two
        x += 3
        prev_w = one
    else:
        for a, b in zip(wizards, wizards[1:]):
            if r[a] == r[b]:
                break
        else:
            # print(r)
            # print("tail", [r[w] for w in range(-1, -4, -1)])
            # print(wizards)
            # print([r[w] for w in wizards])
            assert False
        wizards.remove(a)
        wizards.remove(b)
        result[a] = (x, r[a])
        result[b] = (x + 1, 1)
        where[a] += b
        where[b] += a
        x += 2
        prev_w = b
    prev_y = 1
    
    for w in wizards:
        if r[w] == 0:
            result[w] = (x, 1)
            where[w] += w
        else:
            if prev_y - r[w] + 1 >= 1:
                y = prev_y - r[w] + 1
            else:
                y = prev_y + r[w] - 1
                assert y <= n
            result[w] = (x, y)
            where[w] += prev_w
        prev_y = result[w][-1]
        prev_w = w
        x += 1
    return result, where
 
n = int(stdin.readline())
r = list(map(int, stdin.readline().split()))
if n == 2 and sorted(r) == [1, 2]:
    print("NO")
else:
    positions, where = place_wizards(r)
    print("YES")
    for x, y in positions:
        print(x, y)
    print(*where)
