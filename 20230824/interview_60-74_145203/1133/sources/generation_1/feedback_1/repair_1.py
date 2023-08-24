n = int(input())
words = []
for _ in range(n):
    word = input()
    words.append(word)

count = {}
for word in words:
    distinct_characters = set(char for char in word if char.isalpha())  # Fix: Filter out non-letter characters
    num_distinct_characters = len(distinct_characters)  # Fix: Correctly count distinct characters

    if num_distinct_characters in count:
        count[num_distinct_characters] = max(count[num_distinct_characters], len(word))  # Fix: Update the max length for that number of distinct characters
    else:
        count[num_distinct_characters] = len(word)

max_length = sum(count.values())  # Fix: Calculate the sum of max lengths

print(max_length)