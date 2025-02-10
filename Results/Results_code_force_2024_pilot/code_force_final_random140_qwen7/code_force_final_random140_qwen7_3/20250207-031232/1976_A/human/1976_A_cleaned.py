def func_1(t, test_cases):
    results = []
    for (n, password) in test_cases:
        letters = ''
        digits = ''
        for ch in password:
            if ch.isalpha():
                letters += ch
            elif ch.isdigit():
                digits += ch
        if list(letters) != sorted(letters) or list(digits) != sorted(digits):
            results.append('NO')
            continue
        if letters and digits and (password.index(letters[-1]) > password.index(digits[0])):
            results.append('NO')
        else:
            results.append('YES')
    return results
t = int(input('Number of test cases, t = '))
test_cases = []
for _ in range(t):
    n = int(input('Length of password, n: '))
    password = input('enter passowrd: ').strip()
    test_cases.append((n, password))
results = func_1(t, test_cases)
for result in results:
    print(result)