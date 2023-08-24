n = int(input())
words = []
for _ in range(n):
    word = input()
    words.append(word)

count = {}
for word in words:
    distinct_letters = set(word)
    num_distinct_letters = len(distinct_letters)
    if num_distinct_letters in count:
        count[num_distinct_letters].append(word)
    else:
        count[num_distinct_letters] = [word]

max_length = 0
if 1 in count:
    max_length += sum(len(word) for word in count[1])

if 2 in count:
    max_length += sum(len(word) for word in count[2])

print(max_length)