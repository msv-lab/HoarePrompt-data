def func_1(encoded):
    unique_chars = sorted(set(encoded))
    char_map = {}
    len_unique = len(unique_chars)
    for i in range(len_unique):
        char_map[unique_chars[i]] = unique_chars[len_unique - 1 - i]
    decoded = ''.join((char_map[ch] for ch in encoded))
    return decoded
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
for result in results:
    print(result)