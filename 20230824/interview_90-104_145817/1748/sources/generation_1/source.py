n = int(input())
initial_sizes = list(map(int, input().split()))
temperatures = list(map(int, input().split()))

melted_volumes = []
for i in range(n):
    total_melted = 0
    for j in range(i):
        total_melted += max(0, initial_sizes[j] - temperatures[j])
    melted_volumes.append(total_melted)
    initial_sizes[i] = max(0, initial_sizes[i] - temperatures[i])

melted_volumes.append(sum(initial_sizes))
print(" ".join(map(str, melted_volumes)))