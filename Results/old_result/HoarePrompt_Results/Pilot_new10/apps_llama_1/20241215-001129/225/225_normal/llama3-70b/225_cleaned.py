s = input()
vowels = 'AEIOUY'
n = len(s)
max_jump = 0
last_vowel = -1
for i in range(n):
    if s[i] in vowels:
        if last_vowel == -1:
            max_jump = max(max_jump, i + 1)
        else:
            max_jump = max(max_jump, (i - last_vowel) // 2 + 1)
        last_vowel = i
if last_vowel != n - 1:
    max_jump = max(max_jump, (n - last_vowel) // 2 + 1)
print(max_jump)