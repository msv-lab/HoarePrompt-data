t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    if n % 2 == 0:
        pk = n // 2
    else:
        pk = n // 2
    sl = list(s)
    o = sl.count('1')
    z = sl.count('0')
    (zero, one) = (0, 0)
    lst = []
    mini = pow(10, 8)
    for i in range(n - 1):
        if s[i] == '0':
            zero += 1
        else:
            one += 1
        zero_perc = math.ceil(zero * 100 / (i + 1))
        one_perc = math.ceil((o - one) * 100 / (n - i - 1))
        if zero_perc >= 50 and one_perc >= 50:
            lst.append(i + 1)
    for ele in lst:
        mini = min(mini, abs(pk - ele))
    final = []
    for elem in lst:
        if abs(pk - elem) == mini:
            final.append(elem)
    final.sort()
    if len(final) == 0:
        c1 = o * 100 // n
        if c1 >= 50:
            final.append(0)
        else:
            final.append(n)
    print(final[0])