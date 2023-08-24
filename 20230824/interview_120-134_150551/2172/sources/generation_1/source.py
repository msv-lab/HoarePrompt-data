n, m = map(int, input().split())
word_dict = {}
for _ in range(m):
    lang1, lang2 = input().split()
    word_dict[lang1] = lang2 if len(lang2) < len(lang1) else lang1

lecture = input().split()
notes = [word_dict[word] for word in lecture]
print(' '.join(notes))