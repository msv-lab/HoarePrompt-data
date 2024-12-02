s = input()
n = len(s)
is_spalindrome = True
for i in range(n // 2):
    if s[i] != s[n - i - 1]:
        is_spalindrome = False
        break
print('TAK' if is_spalindrome else 'NIE')