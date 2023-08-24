n = int(input())
array = list(map(int, input().split()))

swaps = []
for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if array[j] < array[min_index]:
            min_index = j
    if min_index != i:
        swaps.append((i, min_index))
        array[i], array[min_index] = array[min_index], array[i]

print(len(swaps))
for swap in swaps:
    print(swap[0], swap[1])