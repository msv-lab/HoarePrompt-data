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
        replaced_word = word
        r_count = count_r(replaced_word)
        for option in options:
            new_word = word.replace(word, option)
            new_r_count = count_r(new_word)
            if new_r_count < r_count:
                replaced_word = new_word
                r_count = new_r_count
            elif new_r_count == r_count and len(new_word) < len(replaced_word):
                replaced_word = new_word
                r_count = new_r_count
        return replaced_word, r_count
    return word, count_r(word)

new_essay = []
for word in essay:
    new_word, r_count = replace_word(word)
    new_essay.append(new_word)
    min_r = min(min_r, r_count)
    min_length += len(new_word)

print(min_length, min_r)