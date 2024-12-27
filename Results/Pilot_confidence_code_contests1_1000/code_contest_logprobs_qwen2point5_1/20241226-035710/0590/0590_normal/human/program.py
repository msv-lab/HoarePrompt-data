array_buffer = []
n, m = map(int, raw_input().split())
array = map(int, raw_input().split())
array = [(array[i], i + 1) for i in range(n)]
array.sort()
for i in range(n):
    if m - array[i][0] >= 0:
        array_buffer.append(array[i][1])
        m -= array[i][0]
print(len(array_buffer))
print(' '.join(str(i) for i in array_buffer))