a = raw_input()
b = raw_input()
c = raw_input()

def func_1(word):
    table = defaultdict(int)
    for char in word:
        table[char] += 1
    return table
ta = func_1(a)
tb = func_1(b)
tc = func_1(c)
maxb = min([ta[char] / tb[char] for char in tb])
ans = maxb
bocc = maxb
for i in range(1, maxb + 1):
    maxc = min([(ta[char] - tb[char] * i) / tc[char] for char in tc])
    if maxc + i > ans:
        ans = maxc + i
        bocc = i
for i in range(bocc):
    sys.stdout.write(b)
for i in range(ans - bocc):
    sys.stdout.write(c)
for char in ta:
    rem = ta[char] - bocc * tb[char] - (ans - bocc) * tb[char]
    for i in range(rem):
        sys.stdout.write(char)