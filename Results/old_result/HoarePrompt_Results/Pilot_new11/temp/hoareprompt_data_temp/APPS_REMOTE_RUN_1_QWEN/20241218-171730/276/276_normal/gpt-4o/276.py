def golden_system_value(s):
    q = (5 ** 0.5 + 1) / 2
    value = 0
    n = len(s)
    for i in range(n):
        if s[i] == '1':
            value += q ** (n - i - 1)
    return value

s1 = input().strip()
s2 = input().strip()

value1 = golden_system_value(s1)
value2 = golden_system_value(s2)

if value1 > value2:
    print(">")
elif value1 < value2:
    print("<")
else:
    print("=")
