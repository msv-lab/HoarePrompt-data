def no():
    print("Impossible")
    exit(0)


names = [raw_input() for _ in xrange(input())]
before = {a: set() for a in "abcdefghijklmnopqrstuvwxyz"}

for i in xrange(len(names) - 1):
    prev_name = names[i]
    curr_name = names[i + 1]
    length = min(len(names[i]), len(names[i + 1]))
    j = 0
    ok = False
    while j < length:
        if prev_name[j] == curr_name[j] or prev_name[j] in before[curr_name[j]]:
            j += 1
        else:
            before[curr_name[j]].update(before[prev_name[j]])
            before[curr_name[j]].add(prev_name[j])
            for b in before[curr_name[j]]:
                if curr_name[j] in before[b]:
                    no()
            ok = True
            break
    if not ok and len(prev_name) > len(curr_name):
        no()

ans = ""

for i in xrange(26):
    for b in before:
        if len(before[b]) == 0:
            break
    ans += b
    before.pop(b)
    for c in before.values():
        if b in c:
            c.remove(b)

print(ans)
