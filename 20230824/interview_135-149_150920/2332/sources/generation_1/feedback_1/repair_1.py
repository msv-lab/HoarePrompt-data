# Bug 1: Correct input handling
# Split the input by newlines and then split each line by spaces to extract the integers
n, k, m = map(int, input().split())
words = input().split()
costs = list(map(int, input().split()))
groups = []
for _ in range(k):
    group = list(map(int, input().split()[1:]))
    groups.append(group)

message = input().split()

# Bug 2: Correct word index building
# Build the index using the word itself as the key, not its position
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
        # Bug 3: Correct calculation of the minimum cost
        # Find the cheapest word in the group and replace the current word's cost
        cheapest_word_cost = float('inf')
        for index in group:
            if costs[index] < cheapest_word_cost:
                cheapest_word_cost = costs[index]
        
        min_cost -= costs[word_index]
        min_cost += cheapest_word_cost

print(min_cost)