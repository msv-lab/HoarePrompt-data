
n, k, m = map(int, input().split())
words = input().split()
costs = list(map(int, input().split()))
groups = []
for _ in range(k):
    group = list(map(int, input().split()[1:]))
    groups.append(group)

message = input().split()

word_indices = {}
for i in range(n):
    word_indices[words[i]] = i

min_cost = 0
for word in message:
    word_index = word_indices[word]
    min_cost += costs[word_index]

    group_index = -1
    for i in range(k):
        if word_index in groups[i]:
            group_index = i
            break

    if group_index != -1:
        group = groups[group_index]
        for index in group:
            if costs[index] < costs[word_index]:
                min_cost -= costs[word_index]
                min_cost += costs[index]
                break

print(min_cost)