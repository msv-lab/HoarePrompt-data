m = int(input())
essay = input().split()
n = int(input())
synonyms = {}
for _ in range(n):
    x, y = input().split()
    x = x.lower()
    y = y.lower()
    if x in synonyms:
        synonyms[x].add(y)
    else:
        synonyms[x] = set([y])

min_r = float('inf')
min_length = float('inf')

def count_r(word):
    return word.lower().count('r')

def replace_word(word):
    if word.lower() in synonyms:
        options = synonyms[word.lower()]
        for option in options:
            replaced_word = option
            r_count = count_r(replaced_word)
            if r_count < min_r:
                return replaced_word, r_count
            elif r_count == min_r:
                return replaced_word, r_count
    return word, count_r(word)

new_essay = []
for word in essay:
    new_word, r_count = replace_word(word)
    new_essay.append(new_word)
    min_r = min(min_r, r_count)
    min_length = min(min_length, len(new_essay))

print(min_r, min_length)