n = int(stdin.readline())
one = {}
two = {}
ans = []
challengers = []
for i in range(n):
    (a, b, c) = map(int, stdin.readline().split())
    challengers.append((a, b, c))
    first = (max(a, b), min(a, b))
    second = (max(a, c), min(a, c))
    third = (max(b, c), min(b, c))
    if first in two:
        if two[first] < one[first][0] + c:
            ans.append((one[first][0] + c, first[0], first[1], one[first][1], i))
            two[first] = one[first][0] + c
    elif first in one:
        two[first] = one[first][0] + c
        ans.append((one[first][0] + c, first[0], first[1], one[first][1], i))
    if second in two:
        if two[second] < one[second][0] + c:
            ans.append((one[second][0] + b, second[0], second[1], one[second][1], i))
            two[second] = one[second][0] + b
    elif second in one:
        two[second] = one[second][0] + b
        ans.append((one[second][0] + b, second[0], second[1], one[second][1], i))
    if third in two:
        if two[third] < one[third][0] + c:
            ans.append((one[third][0] + a, third[0], third[1], one[third][1], i))
            two[third] = one[third][0] + a
    elif third in one:
        two[third] = one[third][0] + a
        ans.append((one[third][0] + a, third[0], third[1], one[third][1], i))
    if first not in one or one[first][0] < c:
        one[first] = (c, i)
    if second not in one or one[second][0] < b:
        one[second] = (b, i)
    if third not in one or one[third][0] < a:
        one[third] = (a, i)
label = 0
cnt = 0
for (a, b, c, ind1, ind2) in ans:
    if min(min(a, b), c) > cnt:
        label = 2
        cnt = min(min(a, b), c)
        first = ind1
        second = ind2
for i in range(n):
    (a, b, c) = challengers[i]
    if min(min(a, b), c) > cnt:
        label = 1
        cnt = min(min(a, b), c)
        first = i
if label == 1:
    stdout.write('1' + '\n' + str(first + 1))
else:
    stdout.write('2' + '\n' + str(first + 1) + ' ' + str(second + 1))