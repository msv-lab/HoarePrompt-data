def func_1(n, password):
    letters = []
    digits = []
    for ch in password:
        if ch.isdigit():
            digits.append(ch)
        else:
            letters.append(ch)
    if letters != sorted(letters):
        return 'NO'
    if digits != sorted(digits):
        return 'NO'
    for i in range(len(password) - 1):
        if password[i].isalpha() and password[i + 1].isdigit():
            return 'NO'
    return 'YES'
t = int(input())
for _ in range(t):
    n = int(input())
    password = input().strip()
    print(func_1(n, password))