def func_1(encoded):
    r = ''.join(sorted(set(encoded)))
    mapping = {r[i]: r[-(i + 1)] for i in range(len(r))}
    return ''.join((mapping[char] for char in encoded))
input = sys.stdin.read
data = input().split()
index = 0
t = int(data[index])
index += 1
results = []
for _ in range(t):
    n = int(data[index])
    index += 1
    b = data[index]
    index += 1
    results.append(func_1(b))
print('\n'.join(results))