n = int(input())
strings = []
for _ in range(n):
    t, k, *positions = input().split()
    strings.append((t, [int(x) for x in positions]))

result = []
max_position = 0

for string in strings:
    t, positions = string
    for i in range(len(t)):
        if i >= len(result):
            result.append(t[i])
        else:
            if t[i] != result[i]:
                break
    else:
        max_position = max(max_position, positions[-1])

for i in range(len(result), max_position):
    result.append('a')

print(''.join(result))