q1 = raw_input().split()
q2 = raw_input().split()
q3 = raw_input().split()
s1 = int(q2[0])
s2 = int(q3[0])
f = 0
p1 = 0
p2 = 0
a1 = int(q1[0])
a2 = int(q1[1])
while p1 < a1 and p2 < a2:
    if s1 == s2:
        s1 = 0
        s2 = 0
        f = f + 1
        p1 = p1 + 1
        p2 = p2 + 1
    if s1 < s2:
        p1 = p1 + 1
        s1 = s1 + int(q2[p1])
    if s1 > s2:
        p2 = p2 + 1
        s2 = s2 + int(q3[p2])
print(f)