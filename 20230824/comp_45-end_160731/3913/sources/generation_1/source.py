def count_possible_letters(n, revealed_letters, m, words):
    possible = 0
    for i in range(n):
        if revealed_letters[i] == '*':
            revealed = set()
            for word in words:
                revealed.add(word[i])
            if len(revealed) > 1:
                possible += 1
    return possible

n = int(input())
revealed_letters = input()
m = int(input())
words = []
for i in range(m):
    word = input()
    words.append(word)

result = count_possible_letters(n, revealed_letters, m, words)
print(result)