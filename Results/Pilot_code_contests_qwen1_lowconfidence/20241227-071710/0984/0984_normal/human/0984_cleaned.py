n = int(raw_input())
s = raw_input()
d = {}
for i in s:
    d[i] = []
for i in range(len(s)):
    d[s[i]].append(i)
p = d['R']
q = d['G']
r = d['B']
p1 = len(p)
q1 = len(q)
r1 = len(r)
z = 0
for i in range(len(p)):
    for j in range(len(q)):
        l = sorted([p[i], q[j]])
        to = bisect.bisect_left(r, l[1])
        isTrue = bisect.bisect_left(r[to:], 2 * l[1] - l[0])
        try:
            if r[to:][isTrue] == 2 * l[1] - l[0]:
                z += r1 - to - 1
            else:
                z += r1 - to
        except:
            z += r1 - to
for i in range(len(q)):
    for j in range(len(r)):
        l = sorted([q[i], r[j]])
        to = bisect.bisect_left(p, l[1])
        isTrue = bisect.bisect_left(p[to:], 2 * l[1] - l[0])
        try:
            if p[to:][isTrue] == 2 * l[1] - l[0]:
                z += p1 - to - 1
            else:
                z += p1 - to
        except:
            z += p1 - to
for i in range(len(p)):
    for j in range(len(r)):
        l = sorted([p[i], r[j]])
        to = bisect.bisect_left(q, l[1])
        isTrue = bisect.bisect_left(q[to:], 2 * l[1] - l[0])
        try:
            if q[to:][isTrue] == 2 * l[1] - l[0]:
                z += q1 - to - 1
            else:
                z += q1 - to
        except:
            z += q1 - to
print(z)