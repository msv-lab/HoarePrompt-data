def func_1(encoded):
    unique_chars = sorted(set(encoded))
    r = ''.join(unique_chars)
    char_map = {char: r[-i - 1] for (i, char) in enumerate(r)}
    decoded = ''.join((char_map[char] for char in encoded))
    return decoded
input = sys.stdin.read
data = input().split()
t = int(data[0])
index = 1
results = []
for _ in range(t):
    n = int(data[index])
    index += 1
    encoded = data[index]
    index += 1
    results.append(func_1(encoded))
print('\n'.join(results))