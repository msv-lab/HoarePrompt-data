def func_1(n):
    magic_words = []
    for _ in range(n):
        length = random.randint(1, 30 * n)
        word = ''.join((random.choice(['X', 'O']) for _ in range(length)))
        magic_words.append(word)
    return magic_words

def func_2(s):
    substrings = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.add(s[i:j])
    return len(substrings)

def func_3(magic_words, power):
    for i in range(len(magic_words)):
        for j in range(len(magic_words)):
            spell = magic_words[i] + magic_words[j]
            if func_2(spell) == power:
                return (i + 1, j + 1)
    return (-1, -1)
n = int(input())
magic_words = func_1(n)
for word in magic_words:
    print(word)
print(flush=True)
q = int(input())
for _ in range(q):
    power = int(input())
    (u, v) = func_3(magic_words, power)
    print(u, v)
    print(flush=True)