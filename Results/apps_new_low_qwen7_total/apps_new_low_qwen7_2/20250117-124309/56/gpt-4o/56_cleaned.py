def func_1(n, k):
    if k > n:
        return 'No'
    bits = []
    for i in range(60, -1, -1):
        if n >> i & 1:
            bits.append(i)
    if len(bits) > k:
        return 'No'
    while len(bits) < k:
        smallest = bits.pop()
        bits.append(smallest - 1)
        bits.append(smallest - 1)
    bits.sort(reverse=True)
    return 'Yes\n' + ' '.join(map(str, bits))
input = sys.stdin.read
data = input().strip().split()
n = int(data[0])
k = int(data[1])
print(func_1(n, k))