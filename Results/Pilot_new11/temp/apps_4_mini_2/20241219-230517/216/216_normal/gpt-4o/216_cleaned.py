n = int(input())
s = input()
max_count = 0
current_set = set()
current_count = 0
for char in s:
    if char.islower():
        if char not in current_set:
            current_set.add(char)
            current_count += 1
    else:
        max_count = max(max_count, current_count)
        current_set.clear()
        current_count = 0
max_count = max(max_count, current_count)
print(max_count)