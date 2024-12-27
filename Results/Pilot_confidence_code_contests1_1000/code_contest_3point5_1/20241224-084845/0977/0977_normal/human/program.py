n, k, q = [int(x) for x in raw_input().split()]

recipes = []
for i in xrange(n):
    recipes.append([int(x) for x in raw_input().split()])

recipes.sort()
recipes.append([2 * 10**5 + 2, 2 * 10**5 + 2])
times = [0] * (2 * 10**5 + 1)

start = recipes[0][0]
curr = start
i, j = 0, 0
num = 0
flag = False
for x in range(start, 2 * 10**5 + 1):
    while i != n - 1 and curr == recipes[i][0]:
        num += 1
        i += 1
        
    if i == n - 1:
        if not flag and x == recipes[i][0]:
            num += 1
            flag = True
            
    while curr > recipes[j][1]:
        num -= 1
        j += 1
    times[x] = num
    curr = x + 1


good = []
for x in times:
    if x >= k:
        good.append(1)
    else:
        good.append(0)

        
sums = []
s = 0
for l in good:
    s += l
    sums.append(s)

    
for i in range(q):
    l, r = [int(x) for x in raw_input().split()]
    print(sums[r] - sums[l - 1])