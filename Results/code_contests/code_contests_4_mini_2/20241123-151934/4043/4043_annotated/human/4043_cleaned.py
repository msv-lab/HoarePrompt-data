def func_1(startIndex, branchLength):
    print('{0} {1}'.format(1, startIndex))
    for i in xrange(startIndex, startIndex + branchLength - 1):
        print('{0} {1}'.format(i, i + 1))
    return startIndex + branchLength
(n, k) = map(int, stdin.readline().split())
minLength = (n - 1) // k
r = (n - 1) % k
maxDistance = minLength * 2 + (2 if r >= 2 else r)
print(maxDistance)
minLengthCount = k - r
startIndex = 2
for _ in xrange(0, minLengthCount):
    startIndex = func_1(startIndex, minLength)
for _ in xrange(0, r):
    startIndex = func_1(startIndex, minLength + 1)